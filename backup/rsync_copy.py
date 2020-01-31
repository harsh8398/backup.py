import hashlib
import sys
import io

# Reference: https://rsync.samba.org/tech_report/tech_report.html
# TODO: use pipelining for better performance as described in https://rsync.samba.org/tech_report/node5.html
class Rsync(object):
    def __init__(self, patchedstream, instream, outstream, BUFFER_SIZE=4096):
        super().__init__()
        self.patchedstream = patchedstream
        self.instream = instream
        self.outstream = outstream
        self.BUFFER_SIZE = BUFFER_SIZE

    def rolling_checksums(self, stream):
        # create weak checksum
        window = stream.read(self.BUFFER_SIZE)
        a = b = 0
        for k in range(len(window)):
            a = (a + window[k]) % (1 << 16)
            b = (b + (len(window) - k) * window[k]) % (1 << 16)
        yield a | (b << 16)
        # now generate rolling checksum
        k = 0
        next_char = stream.read(1)
        while next_char:
            a = (a - window[k] + next_char) % (1 << 16)
            b = (b - len(window) * window[k] + a) % (1 << 16)
            yield a | (b << 16)
            next_char = stream.read(1)

    def strong_checksums(self, stream):
        window = stream.read(self.BUFFER_SIZE)
        while window:
            yield hashlib.md5(window).hexdigest()
            window = stream.read(self.BUFFER_SIZE)

    def create_lookup(self):
        self.lookup = {}
        for block_index, (weak_checksum, strong_checksum) in enumerate(
            zip(self.rolling_checksums(self.instream), self.strong_checksums(self.instream))
        ):
            if not weak_checksum in self.lookup:
                self.lookup[weak_checksum] = {}
            self.lookup[weak_checksum][strong_checksum] = block_index

    def delta(self):
        self.create_lookup()
        i = 0
        window = self.patchedstream.read(self.BUFFER_SIZE)
        while window:
            matching_value = self.lookup.get(next(self.rolling_checksums(io.BytesIO(window))))
            if matching_value:
                block_index = matching_value.get(
                    self.lookup.get(next(self.strong_checksums(io.BytesIO(window))))
                )
                if block_index:
                    yield block_index
            yield window[0:1]
            i += 1
            self.patchedstream.seek(i)
            window = self.patchedstream.read(self.BUFFER_SIZE)

    def rsync_copy(self):
        for data in self.delta():
            print(data)
            if isinstance(data, int):
                self.instream.seek(data * self.BUFFER_SIZE)
                data = self.instream.read(self.BUFFER_SIZE)
            self.outstream.write(data)

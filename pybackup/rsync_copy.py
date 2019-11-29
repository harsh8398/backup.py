import hashlib
import sys

# XXX: have singleton metaclass for this class
class Rsync(object):
    def __init__(self):
        super().__init__()
        self.BUFFER_SIZE = 4096

    def gen_weak_checksums(self, instream):
        # https://rsync.samba.org/tech_report/node3.html
        # create weak checksum
        window = instream.read(self.BUFFER_SIZE)
        a = b = 0
        for k in range(len(window)):
            a = (a + window[k]) % (1 << 16)
            b = (b + (len(window) - k) * window[k]) % (1 << 16)
        yield a | (b << 16)
        # now generate rolling checksum
        k = 0
        while True:
            next_char = instream.read(1)
            if not next_char:
                break
            a = (a - window[k] + next_char) % (1 << 16)
            b = (b - len(window) * window[k] + a) % (1 << 16)
            yield a | (b << 16)

    def gen_strong_checksums(self, instream):
        while True:
            window = instream.read(self.BUFFER_SIZE)
            if not window:
                break
            yield hashlib.md5(window).hexdigest()

    def create_lookup(self, instream):
        weak_checksums = self.gen_weak_checksums(instream)
        strong_checksums = self.gen_strong_checksums(instream)
        self.lookup = {}
        for block_number, (weak_checksum, strong_checksum) in enumerate(
            zip(weak_checksums, strong_checksums)
        ):
            self.lookup[weak_checksum][strong_checksum] = block_number

    def delta(self, remotestream, local_stream):
        self.create_lookup(remotestream)
        for i in range(len(local_stream)):
            window = local_stream.read(self.BUFFER_SIZE)
            matching_value = self.lookup.get(next(self.gen_weak_checksums(window)))
            if matching_value:
                block_index = matching_value.get(
                    self.lookup.get(next(self.gen_strong_checksums(window)))
                )
                if block_index:
                    yield block_index
            local_stream.seek(i)
            yield window[0]
    
    def copy(self, remotestream, local_stream, outstream):
        for data in self.delta(remotestream, local_stream):
            if isinstance(data, int):
                # TODO: write block
                outstream.write()
            else:
                outstream.write(data)
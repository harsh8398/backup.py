class InvalidMetadataError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class NoFilesToBackUpError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
class PostData:
    def __init__(self, cm: str, mentions: int, created_on: int):
        self.crypto_mentioned = cm
        self.mentions = mentions
        self.created_on = created_on

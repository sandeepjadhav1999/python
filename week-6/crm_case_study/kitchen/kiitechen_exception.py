class InvalidLocationException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class InvalidNameException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

class IteamNotFoundException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg = msg

class InvalidPriceException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg = msg

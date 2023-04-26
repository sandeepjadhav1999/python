class InvalidQuntityException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class InvalidNameException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

class InvalidTotalPriceException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg = msg



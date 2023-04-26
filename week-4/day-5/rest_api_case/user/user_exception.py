class InvalidUserNameException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)
        self.msg = msg


class InvalidPasswordException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)
        self.msg = msg


class InvalidRoleException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)
        self.msg = msg


class InvalidUserException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)
        self.msg = msg

class InvalidAmountException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)
        self.msg = msg


class InvalidDetailsException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)
        self.msg = msg


class InvalidStatusException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(str)
        self.msg = msg
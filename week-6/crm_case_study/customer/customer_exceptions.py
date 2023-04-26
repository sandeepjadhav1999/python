class InvalidCustomerMobileException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class InvalidCustomerNameException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

class InvalidCustomerEmailException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

class InvalidCustomerDOBException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

class InvalidCustomerLocException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

class InvalidCustomerStatusException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

class UserNotFoundException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg = msg


class InActiveUserException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg = msg


class UserAlreadyActivatedException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg = msg


class UnAuthorizedOperationException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg = msg

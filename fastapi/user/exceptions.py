from fastapi import HTTPException, status


class UserNotFoundOrInactiveException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="User not found or is inactive")


class InValidCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")

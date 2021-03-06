from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str) -> str:
    # Hashes the user password
    return pwd_context.hash(password)


def verify(plain_password: str, hashed_password: str):
    # Verifies password during login
    return pwd_context.verify(plain_password, hashed_password)

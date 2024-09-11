from passlib.context import CryptContext

hashing_context = CryptContext(
    schemes=[
        'argon2'
    ],
    deprecated='auto'
)
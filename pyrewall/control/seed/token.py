from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from pathlib import Path

from ...core.config import PYREWALL_CONFIG_DIR

def generate_token_rsa():
    private_key_file = f'{PYREWALL_CONFIG_DIR}private_key.pem'
    key_file_path = Path(private_key_file)

    if key_file_path.is_file():
        return
    
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open(private_key_file, 'wb') as f:
        f.write(private_pem)

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(f'{PYREWALL_CONFIG_DIR}public_key.pem', 'wb') as f:
        f.write(public_pem)

def seed_token(dev: bool):
    generate_token_rsa()
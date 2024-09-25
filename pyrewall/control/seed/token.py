from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec, ed25519
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from pathlib import Path

from ...core.config import PYREWALL_CONFIG_DIR

# def generate_token_rsa():
#     private_key_file = f'{PYREWALL_CONFIG_DIR}private_key.pem'
#     key_file_path = Path(private_key_file)

#     if key_file_path.is_file():
#         return
    
#     private_key = rsa.generate_private_key(
#         public_exponent=65537,
#         key_size=4096,
#         backend=default_backend()
#     )
#     public_key = private_key.public_key()

#     private_pem = private_key.private_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PrivateFormat.PKCS8,
#         encryption_algorithm=serialization.NoEncryption()
#     )

#     with open(private_key_file, 'wb') as f:
#         f.write(private_pem)

#     public_pem = public_key.public_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PublicFormat.SubjectPublicKeyInfo
#     )
#     with open(f'{PYREWALL_CONFIG_DIR}public_key.pem', 'wb') as f:
#         f.write(public_pem)

def generate_token_key_ed25519():
    private_key_file = f'{PYREWALL_CONFIG_DIR}token_ed25519.key'
    public_key_file = f'{PYREWALL_CONFIG_DIR}token_ed25519.pem'
    private_key_file_path = Path(private_key_file)
    public_key_file_path = Path(public_key_file)


    if private_key_file_path.is_file() and public_key_file_path.is_file():
        return
    
    if not private_key_file_path.is_file():
        private_key = ed25519.Ed25519PrivateKey.generate()
        private_key_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(private_key_file, 'wb') as f:
            f.write(private_key_bytes)
    else:
        with open(private_key_file, 'rb') as f:
            private_key = ed25519.Ed25519PrivateKey.from_private_bytes(f.read())
    
    public_key = private_key.public_key()
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open(public_key_file, 'wb') as f:
        f.write(public_key_bytes)

def generate_token_key_ecdsa():
    private_key_file = f'{PYREWALL_CONFIG_DIR}token_ecdsa.key'
    public_key_file = f'{PYREWALL_CONFIG_DIR}token_ecdsa.pem'
    private_key_file_path = Path(private_key_file)
    public_key_file_path = Path(public_key_file)


    if private_key_file_path.is_file() and public_key_file_path.is_file():
        return
    
    if not private_key_file_path.is_file():
        private_key = ec.generate_private_key(
            curve=ec.BrainpoolP256R1(),
            backend=default_backend()
        )
        private_key_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(private_key_file, 'wb') as f:
            f.write(private_key_bytes)
    else:
        with open(private_key_file, 'rb') as f:
            private_key = serialization.load_pem_private_key(f.read())
    
    public_key = private_key.public_key()
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open(public_key_file, 'wb') as f:
        f.write(public_key_bytes)

def seed_token(dev: bool):
    generate_token_key_ecdsa()
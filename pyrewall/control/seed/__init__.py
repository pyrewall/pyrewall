from .auth import seed_auth
from .token import seed_token

def seed(args):
    seed_auth(args.dev)
    seed_token(args.dev)
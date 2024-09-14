import sys

from argparse import ArgumentParser

from pprint import pprint

from .seed import seed

from pyrewall.core.dependency_injection import di

def main(argv: list[str] = None):
    if argv is None:
        argv = sys.argv[1:]
    
    arg_parser = ArgumentParser('pyrectl')

    sub_arg_parsers = arg_parser.add_subparsers()

    seed_args = sub_arg_parsers.add_parser('seed')
    seed_args.add_argument('--dev', action='store_true')
    seed_args.set_defaults(func=seed)

    args = arg_parser.parse_args(argv)
    if hasattr(args, 'func'):
        with di.di_scope():
            args.func(args)
    else:
        arg_parser.print_usage()

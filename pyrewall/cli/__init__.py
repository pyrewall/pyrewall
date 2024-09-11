from .operational import OperationalCli


def run_cli():
    cli = OperationalCli()
    cli.cmdloop()
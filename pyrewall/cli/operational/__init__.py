from typing import IO
from os import environ as env, system

from ..pyrewall_cmd import PyrewallCmd
from ..configuration import ConfigurationCli

class OperationalCli(PyrewallCmd):
    def __init__(self, completekey: str = "tab", stdin: IO[str] | None = None, stdout: IO[str] | None = None) -> None:
        super().__init__(completekey, stdin, stdout)

        # TODO get user
        username = env.get('USER', '<missing>')
        hostname = env.get('HOSTNAME', '<missing>')

        self.prompt = f'{username}@{hostname}> '

    def do_ping(self, args):
        system(f'ping {args}')
    
    def help_ping(self):
        system('ping -h')

    def do_shell(self, args):
        if len(args) == 0:
            system("bash")
        else:
            system(args)
    
    def do_show(self, args):
        pass

    def do_configuration(self, args):
        config = ConfigurationCli()
        config.cmdloop()

    def do_exit(self, args):
        return True
    
    def do_shutdown(self, args):
        system()

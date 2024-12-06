from typing import IO
from os import environ as env, system

from ..pyrewall_cmd import PyrewallCmd

class ConfigurationCli(PyrewallCmd):
    def __init__(self, completekey: str = "tab", stdin: IO[str] | None = None, stdout: IO[str] | None = None) -> None:
        super().__init__(completekey, stdin, stdout)

        # TODO get user
        username = env.get('USER', '<missing>')
        hostname = env.get('HOSTNAME', '<missing>')

        self.prompt = f'{username}@{hostname}(config)# '


    def do_exit(self, args):
        return True
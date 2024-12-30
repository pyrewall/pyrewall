from cmd import Cmd

from pyrewall.core.dependency_injection import di

class PyrewallCmd(Cmd):
    
    # def onecmd(self, line: str) -> bool:
    #     return super().onecmd(line)

    def default(self, line):
        cmd, arg, line = self.parseline(line)

        cmds = list(filter(lambda f: f.startswith(f'do_{cmd}'), self.get_names()))

        if len(cmds) == 1:
            func = getattr(self, cmds[0])
            return func(arg)
        
        if len(cmds) > 1:
            print(f'Ambugous command: {line}')
            print('Did you mean?')
            print(f'  {'  '.join([s[3:] for s in cmds])}')

        return super().default(line)
    
    # def precmd(self, line: str) -> str:
    #     di._scope_cache.setup_cache()
    #     return super().precmd(line)
    
    # def onecmd(self, line: str) -> bool:
    #     try:
    #         return super().onecmd(line)
    #     finally:
    #         pass

    # def postcmd(self, stop: bool, line: str) -> bool:
    #     di._scope_cache.del_cache()
    #     return super().postcmd(stop, line)
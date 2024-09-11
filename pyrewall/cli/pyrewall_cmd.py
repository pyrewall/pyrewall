from cmd import Cmd

from pyrewall.core.dependency_injection import di

class PyrewallCmd(Cmd):
    
    def onecmd(self, line: str) -> bool:
        
        return super().onecmd(line)

    pass
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
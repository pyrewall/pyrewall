from enum import IntFlag, auto

class FirewallState(IntFlag):
    NoState = 0
    Invalid = auto()
    New = auto()
    Established = auto()
    Related = auto()
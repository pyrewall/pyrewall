from enum import auto
from strenum import SnakeCaseStrEnum

class FirewallAction(SnakeCaseStrEnum):
    Pass = auto()
    Block = auto()
    Reject = auto()
from typing import Tuple
from abc import ABC, abstractmethod
class CheckStep(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass
    
    @abstractmethod
    def pre(self) -> Tuple[bool, str]:
        pass
    
    @abstractmethod
    def run(self) -> bool:
        pass
from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self, device="cpu", *agf, **karg):
        pass
    
    @abstractmethod
    def __call__(self, *args, **kwds):
        pass
    
"""
Created to understand ControlAirbrakes branch, where file is Saturn/Modules/COntrolAlgos
"""
from abc import ABC, abstractmethod

class Base(ABC):
    _list: dict[str,:ABC] = {}
    _numb_list = []
    number:int

    def __init__(self,str_):
        self.string_ = str_
        pass

    def __init_subclass__(cls,number) -> None:
        """
        this class determines what to include in the subclasses
        """
        cls.number = number
        class_name = cls.__name__.lower()

        if not class_name in Base._list:
            Base._list[class_name] = cls
        else:
            print("{} is already present in _list".format(class_name))

        Base._numb_list.append(number)

        super().__init_subclass__()

    """
    __init_subclass__ --> only runs when a subclass of a class is created
    allows the parent to determine how subclasses are initialised
    """
    

class LQR(Base,number =1): #since Base/init_subclass specifies arg: number
    def __init__(self,str_,extra):
        super().__init__(str_) #youre importing all attributes from Base and passing the required inputs into that
        self.extra = extra

    def __call__(self):
        return '{}.called'.format(self.name)
        

class LUT(Base,number =2):
    def __init__(self):
        pass

    def __call__(self):
        return '{}.called'.format(self.name)

class Static(Base,number =3):
    def __init__(self):
        pass

    @classmethod
    def class_name(cls):
        return cls.__name__.lower()

        
    def __call__(self,string_):
        return '{}.called with string:{}' .format(self.class_name(),string_)

A = Static()
B = LQR("LQR_string","extra_lqr")
C = LUT()

print(Base._list, Base._numb_list)
    

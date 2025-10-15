from dataclasses import dataclass
from typing import Iterator
@dataclass
class Employee:
    id: int
    name: str
    
class EmployeeRepo:
    def __init__(self, employees: list[Employee]):
        self.__employees = employees.copy()
    def __iter__(self) -> Iterator[Employee]:
        return iter(self.__employees)    
        
repo: EmployeeRepo = EmployeeRepo([Employee(1243, "Vasya"), Employee(1245, "Petya")])
names: list[str] = [e.name for e in repo] 
print(names)      
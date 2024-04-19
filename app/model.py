
from typing import List


class Student:
    def __init__(self, uwaID:str, name:str) -> None:
        self.uwaID:str = uwaID
        self.name:str = name

class Group:
    def __init__(self, students:List[Student]) -> None:
        self.students:List[Student] = students
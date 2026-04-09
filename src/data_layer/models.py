from dataclasses import dataclass


@dataclass
class Student:
    id: int #primary
    first_name: str
    last_name: str
    major: str
    email: str
    student_year: str

@dataclass
class Professor:
    id: int #primary
    first_name: str
    last_name: str
    email: str


@dataclass
class Course:
    id: int #primary
    p_id: int #foreign
    name: str

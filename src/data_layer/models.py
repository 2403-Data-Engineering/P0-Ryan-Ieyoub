from dataclasses import dataclass


@dataclass
class Student:
    id: int #primary
    first_name: str
    last_name: str
    major: str
    email: str
    year: str

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

professors = [
    Professor(1, "John", "Smith", "jsmith@college.edu"),
    Professor(2, "Emily", "Clark", "eclark@college.edu"),
    Professor(3, "David", "Johnson", "djohnson@college.edu"),
    Professor(4, "Laura", "Miller", "lmiller@college.edu"),
    Professor(5, "James", "Wilson", "jwilson@college.edu"),
    Professor(6, "Karen", "Taylor", "ktaylor@college.edu"),
    Professor(7, "Michael", "Brown", "mbrown@college.edu"),
    Professor(8, "Sarah", "Davis", "sdavis@college.edu"),
    Professor(9, "Robert", "Anderson", "randerson@college.edu"),
]

students = [
    Student(1, "Alice", "Brown", "Computer Science", "alice.brown@college.edu", "Sophomore"),
    Student(2, "Bob", "Davis", "Mathematics", "bob.davis@college.edu", "Freshman"),
    Student(3, "Charlie", "Evans", "Physics", "charlie.evans@college.edu", "Junior"),
    Student(4, "Diana", "Foster", "Chemistry", "diana.foster@college.edu", "Senior"),
    Student(5, "Ethan", "Garcia", "Biology", "ethan.garcia@college.edu", "Sophomore"),
    Student(6, "Fiona", "Harris", "Computer Science", "fiona.harris@college.edu", "Freshman"),
    Student(7, "George", "Ibrahim", "Mathematics", "george.ibrahim@college.edu", "Junior"),
    Student(8, "Hannah", "Jones", "Physics", "hannah.jones@college.edu", "Sophomore"),
    Student(9, "Ian", "King", "Chemistry", "ian.king@college.edu", "Senior"),
    Student(10, "Julia", "Lee", "Biology", "julia.lee@college.edu", "Freshman"),
    Student(11, "Kevin", "Moore", "Computer Science", "kevin.moore@college.edu", "Junior"),
    Student(12, "Laura", "Nelson", "Mathematics", "laura.nelson@college.edu", "Sophomore"),
    Student(13, "Mason", "Owens", "Physics", "mason.owens@college.edu", "Senior"),
    Student(14, "Nina", "Parker", "Chemistry", "nina.parker@college.edu", "Junior"),
    Student(15, "Owen", "Quinn", "Biology", "owen.quinn@college.edu", "Sophomore"),
]

courses = [
    Course(1, 1, "Introduction to Programming"),
    Course(2, 1, "Data Structures"),
    Course(3, 2, "Calculus I"),
    Course(4, 2, "Linear Algebra"),
    Course(5, 3, "Physics I"),
    Course(6, 3, "Quantum Mechanics"),
    Course(7, 4, "Organic Chemistry"),
    Course(8, 4, "Inorganic Chemistry"),
    Course(9, 5, "Biology I"),
    Course(10, 5, "Genetics"),
    Course(11, 6, "Software Engineering"),
    Course(12, 6, "Database Systems"),
    Course(13, 7, "Statistics"),
    Course(14, 8, "Environmental Science"),
    Course(15, 9, "Astronomy"),
]
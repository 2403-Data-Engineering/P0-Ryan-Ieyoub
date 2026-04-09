from data_layer.course_dao import (
    get_all_courses as dao_get_all_courses,
    create_course,
    update_course,
    delete_course,
    get_students_by_course,
    get_course_by_id
)

class CourseService:
    def get_all_courses(self):
        return dao_get_all_courses()

    def create_new_course(self, name, professor_id):
        create_course(name, professor_id)

    def update_existing_course(self, id, name, professor_id):
        update_course(id, name, professor_id)

    def delete_existing_course(self, id):
        delete_course(id)

    def get_course_students(self, course_id: int):
        return get_students_by_course(course_id)

    def get_course_by_id(self, course_id: int):
        return get_course_by_id(course_id)
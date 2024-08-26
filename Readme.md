150141-Patrick Kamatu
151436-Zaheer Abdulalim
151438- Dylan Matibe
151101- Doras Kiptoo
151887 -Eva Gathoni

      1. Models and Relationships
Student
Fields:

user: A ForeignKey to Django's built-in User model.
date_of_birth: A DateField for the student's date of birth.
address: A CharField for the student's address.
phone_number: A CharField for the student's phone number.
enrollment_date: A DateField indicating when the student was enrolled.
Relationships:

The Student model has a one-to-many relationship with the Enrollment model.
Course
Fields:

title: A CharField for the course title.
description: A TextField for a detailed course description.
start_date: A DateField indicating when the course starts.
end_date: A DateField indicating when the course ends.
capacity: An IntegerField for the maximum number of students that can enroll.
Relationships:

The Course model has a one-to-many relationship with the Enrollment model.
Lecturer
Fields:

name: A CharField for the lecturer's name.
email: An EmailField for the lecturer's email.
phone_number: A CharField for the lecturer's phone number.
courses: A ManyToManyField linking lecturers to courses.
Relationships:

A Lecturer is linked to multiple Course objects through a many-to-many relationship.

Enrollment
Fields:

student: A ForeignKey to the Student model.
course: A ForeignKey to the Course model.
enrollment_date: A DateField indicating when the enrollment took place.
Relationships:

Enrollment links students and courses, creating a many-to-many relationship between Student and Course.

Grade
Fields:

student: A ForeignKey to the Student model.
course: A ForeignKey to the Course model.
grade: A CharField for the student's grade in the course.
Relationships:

Grade links Student and Course and holds information about the grade received.

2. Views/Viewsets and Their Roles
StudentViewSet: Manages CRUD operations for students. It handles requests to list, create, retrieve, update, and delete students.
CourseViewSet: Manages CRUD operations for courses. It handles requests to list, create, retrieve, update, and delete courses.
LecturerViewSet: Manages CRUD operations for lecturers. It handles requests to list, create, retrieve, update, and delete lecturers.
EnrollmentViewSet: Manages CRUD operations for enrollments. It handles requests to list, create, retrieve, update, and delete enrollments.
GradeViewSet: Manages CRUD operations for grades. It handles requests to list, create, retrieve, update, and delete grades.
Each viewset is connected to its corresponding model and is responsible for interacting with the database, performing the necessary operations, and returning the appropriate HTTP responses from the HTTP requests

3. Serializers and Validation Rules
StudentSerializer: Converts Student model instances to JSON format and vice versa. Validation rules ensure that date_of_birth, address, and phone_number are provided and properly formatted.
CourseSerializer: Converts Course model instances to JSON format and vice versa. Validation rules ensure that title, start_date, and end_date are provided and valid.
LecturerSerializer: Converts Lecturer model instances to JSON format and vice versa. Validation rules ensure that email is a valid email format and name and phone_number are provided.
EnrollmentSerializer: Converts Enrollment model instances to JSON format and vice versa. Validation rules ensure that student, course, and enrollment_date are provided and that the student is not already enrolled in the course.
GradeSerializer: Converts Grade model instances to JSON format and vice versa. Validation rules ensure that student, course, and grade are provided.

4. URL Patterns and Their Purpose
The URL patterns are defined to route HTTP requests to the appropriate viewsets:

students/

GET: List all students.
POST: Create a new student.
GET students/<id>/: Retrieve, update, or delete a specific student.
courses/

GET: List all courses.
POST: Create a new course.
GET courses/<id>/: Retrieve, update, or delete a specific course.
lecturers/

GET: List all lecturers.
POST: Create a new lecturer.
GET lecturers/<id>/: Retrieve, update, or delete a specific lecturer.
enrollments/

GET: List all enrollments.
POST: Create a new enrollment.
GET enrollments/<id>/: Retrieve, update, or delete a specific enrollment.
grades/

GET: List all grades.
POST: Create a new grade.
GET grades/<id>/: Retrieve, update, or delete a specific grade.
These URL patterns ensure that each resource (students, courses, lecturers, enrollments, grades) is accessible via a RESTful API, following best practices for endpoint design.
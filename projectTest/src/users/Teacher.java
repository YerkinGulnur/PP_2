package users;

import java.util.List;

public class Teacher extends Employee {
    private String teacherId;
    private TeacherTitle title;
    private List<Course> coursesTaught;
    private double rating;

    public Teacher(int id, String email, String password, String fullName, int employeeId, String department, String teacherId, TeacherTitle title, List<Course> coursesTaught, double rating) {
        super(id, email, password, fullName, employeeId, department);
        this.teacherId = teacherId;
        this.title = title;
        this.coursesTaught = coursesTaught;
        this.rating = rating;
    }

    public void viewCourses() {
        System.out.println("Courses taught by " + fullName + ":");
        for (Course course : coursesTaught) {
            System.out.println("- " + course.getName());
        }
    }

    public void sendComplaint(User receiver, String content, UrgencyLevel urgency) {
        Complaint complaint = new Complaint(this, receiver, content, urgency);
        complaint.send();
    }
}

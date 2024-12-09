package users;

public class Student extends User {
    private String studentID;
    private String degree;
    private String faculty;
    private int year;
    private double gpa;
    private int credits;
    private Transcript transcript;
    private String organization;
    private String organizationRole;
    private boolean granted;

    public Student(int id, String email, String password, String fullName, String studentID, String degree, String faculty, int year, double gpa, int credits, Transcript transcript, String organization, String organizationRole, boolean granted) {
        super(id, email, password, fullName);
        this.studentID = studentID;
        this.degree = degree;
        this.faculty = faculty;
        this.year = year;
        this.gpa = gpa;
        this.credits = credits;
        this.transcript = transcript;
        this.organization = organization;
        this.organizationRole = organizationRole;
        this.granted = granted;
    }

    public void registerForCourse(Course course) {
        System.out.println(fullName + " registered for course " + course.getName());
    }

    public void viewTranscript() {
        System.out.println(fullName + "'s transcript: " + transcript.getDetails());
    }
}

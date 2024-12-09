package users;

import java.util.ArrayList;
import java.util.List;

public class Course {
    private String courseCode;
    private String name;
    private int credits;
    private String type;
    private String description;
    private String faculty;
    private List<Teacher> instructors;

    public Course(String courseCode, String name, int credits, String type, String description, String faculty) {
        this.courseCode = courseCode;
        this.name = name;
        this.credits = credits;
        this.type = type;
        this.description = description;
        this.faculty = faculty;
        this.instructors = new ArrayList<>();
    }

    public void addInstructor(Teacher teacher) {
        instructors.add(teacher);
    }

    public List<Teacher> getInstructors() {
        return instructors;
    }

    public String getName() {
        return name;
    }

    public boolean isMajorCourse() {
        return "Major".equalsIgnoreCase(type);
    }
}

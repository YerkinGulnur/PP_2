package users;

public abstract class Employee extends User {
    protected int employeeId;
    protected String department;

    public Employee(int id, String email, String password, String fullName, int employeeId, String department) {
        super(id, email, password, fullName);
        this.employeeId = employeeId;
        this.department = department;
    }

    public void sendMessage() {
        System.out.println(fullName + " sent a message.");
    }
}
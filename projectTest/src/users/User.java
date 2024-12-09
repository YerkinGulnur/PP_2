package users;

public abstract class User {
    protected int id;
    protected String email;
    protected String password;
    protected String fullName;

    public User(int id, String email, String password, String fullName) {
        this.id = id;
        this.email = email;
        this.password = password;
        this.fullName = fullName;
    }

    public void login() {
        System.out.println(fullName + " logged in.");
    }

    public void logout() {
        System.out.println(fullName + " logged out.");
    }
}

package users;

public class Complaint {
    private User sender;
    private User receiver;
    private String content;
    private UrgencyLevel urgency;

    public Complaint(User sender, User receiver, String content, UrgencyLevel urgency) {
        this.sender = sender;
        this.receiver = receiver;
        this.content = content;
        this.urgency = urgency;
    }

    public void send() {
        System.out.println("Complaint sent from " + sender.fullName + " to " + receiver.fullName);
    }

    public String view() {
        return "From: " + sender.fullName + "\nTo: " + receiver.fullName + "\nContent: " + content + "\nUrgency: " + urgency;
    }
}
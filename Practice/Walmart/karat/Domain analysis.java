import java.util.*;

class Book {
    private int id;
    private String title;
    private String author;
    private String genre;
    private String status;  // "available", "borrowed"
    private Date dueDate;

    public Book(int id, String title, String author, String genre) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.genre = genre;
        this.status = "available";
        this.dueDate = null;
    }

    // Getter and Setter methods
    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public String getGenre() {
        return genre;
    }

    public String getStatus() {
        return status;
    }

    public Date getDueDate() {
        return dueDate;
    }

    // Methods to update book details and manage its state
    public void updateDetails(String title, String author, String genre) {
        this.title = title;
        this.author = author;
        this.genre = genre;
    }

    public void borrow() {
        this.status = "borrowed";
    }

    public void returnBook() {
        this.status = "available";
        this.dueDate = null;
    }

    public void renew() {
        // Renew the book (extend due date)
        this.dueDate = new Date(System.currentTimeMillis() + 7 * 24 * 60 * 60 * 1000L);  // Add 7 days to the current time
    }
}

class User {
    private int id;
    private String name;
    private String email;
    private String status;  // "active", "inactive"

    public User(int id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.status = "active";
    }

    // Getter and Setter methods
    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public String getStatus() {
        return status;
    }

    // Methods to manage user actions
    public void register() {
        // Code to register user
    }

    public void updateInfo(String name, String email) {
        this.name = name;
        this.email = email;
    }

    public void deactivateAccount() {
        this.status = "inactive";
    }

    public void borrowBook(Book book) {
        book.borrow();
    }

    public void returnBook(Book book) {
        book.returnBook();
    }

    public void renewBook(Book book) {
        book.renew();
    }
}

class Loan {
    private int userId;
    private int bookId;
    private Date loanDate;
    private Date dueDate;

    public Loan(int userId, int bookId, Date loanDate, Date dueDate) {
        this.userId = userId;
        this.bookId = bookId;
        this.loanDate = loanDate;
        this.dueDate = dueDate;
    }

    // Getter and Setter methods
    public int getUserId() {
        return userId;
    }

    public int getBookId() {
        return bookId;
    }

    public Date getLoanDate() {
        return loanDate;
    }

    public Date getDueDate() {
        return dueDate;
    }

    // Extend the due date for the loan
    public void extendDueDate() {
        this.dueDate = new Date(this.dueDate.getTime() + 7 * 24 * 60 * 60 * 1000L);  // Extend 7 more days
    }
}

class Library {
    private List<Book> books;
    private List<User> users;
    private List<Loan> loans;

    public Library() {
        this.books = new ArrayList<>();
        this.users = new ArrayList<>();
        this.loans = new ArrayList<>();
    }

    // Methods to manage books
    public void addBook(Book book) {
        books.add(book);
    }

    public void removeBook(Book book) {
        books.remove(book);
    }

    public List<Book> searchBooks(String query) {
        List<Book> result = new ArrayList<>();
        for (Book book : books) {
            if (book.getTitle().toLowerCase().contains(query.toLowerCase()) || book.getAuthor().toLowerCase().contains(query.toLowerCase())) {
                result.add(book);
            }
        }
        return result;
    }

    // Recommend books to the user (this can be improved with more sophisticated logic)
    public List<Book> recommendBooks(User user) {
        // For simplicity, we recommend all available books
        List<Book> recommendedBooks = new ArrayList<>();
        for (Book book : books) {
            if (book.getStatus().equals("available")) {
                recommendedBooks.add(book);
            }
        }
        return recommendedBooks;
    }
}

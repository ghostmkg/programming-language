package CMS;

import java.util.ArrayList;

public class Faculty extends Person
{
    private String employeeID;
    private long salary;
    private Date dateOfBirth;
    private Date hiringDate;
    private ArrayList<Course> ecourses = new ArrayList<>();

    public Faculty(String name, String cnic, String contact, String address,String employeeID, long salary, ArrayList<Course> ecourses , Date dateOfBirth, Date hiringDate) 
    {
        super(name, cnic, contact, address);
        this.employeeID = employeeID;
        this.salary = salary;
        this.ecourses = ecourses;
        this.dateOfBirth = dateOfBirth;
        this.hiringDate = hiringDate;
    }

    public String getEmployeeID() {
        return employeeID;
    }

    public void setEmployeeID(String employeeID) {
        this.employeeID = employeeID;
    }

    public long getSalary() {
        return salary;
    }

    public void setSalary(long salary) {
        this.salary = salary;
    }

    public ArrayList<Course> getCourses() 
    {
        return ecourses;
    }

    public void setCourses(ArrayList<Course> ecourses) 
    {
        this.ecourses = ecourses;
    }

    

    public Date getDateOfBirth() 
    {
        return dateOfBirth;
    }

    public void setDateOfBirth(Date dateOfBirth) 
    {
        this.dateOfBirth = dateOfBirth;
    }

    public Date getHiringDate() {
        return hiringDate;
    }

    public void setHiringDate(Date hiringDate) {
        this.hiringDate = hiringDate;
    }

    public String account()
    {
        return "Abstract of faculty";
    }
    public String toString() {
        return String.format("Employee ID                   Salary%n%-30s%-19s%nBitrh Date : %s%nHiring Date : %s%s", employeeID, salary, dateOfBirth, hiringDate,
        "\n==============================================================\n                        Employee's courses\n\nCourse Name                   Course code        Credit hours",getCourses(),account());
    }

}

package CMS;

import java.util.ArrayList;

public class Student extends Person{
    // private String name;
    private String regNo;
    private String semester;
    private Course course1;
    private Course course2;
    private Course course3;
    private Date birthDate;
    private Date admissionDatee;

    private ArrayList<Course> courses = new ArrayList<>();

    public Student(String name, String cnic, String contact, String address,String regNo, String semester, Course course1, Course course2, Course course3, ArrayList<Course> courses, Date birthDate , Date admissionDatee) {
        super(name, cnic, contact , address);
        this.regNo = regNo;
        this.semester = semester;
        this.course1 = course1;
        this.course2 = course2;
        this.course3 = course3;
        this.courses = courses;
        this.birthDate = birthDate;
        this.admissionDatee = admissionDatee;
    }

    
    
    public void setregNo(String regNo) {
        this.regNo = regNo;
    }

    public String getregNo() {
        return regNo;
    }

    public void setsemester(String semester) {
        this.semester = semester;
    }

    public String getsemester() {
        return semester;
    }

    public void setcourse1() {
        this.course1 = course1;
    }

    public Course getcourse1() {
        return course1;
    }

    public void setcourse2(Course course2) {
        this.course2 = course2;
    }

    public Course getcourse2() {
        return course2;
    }

    public Course getCourse3() {
        return course3;
    }

    public void setCourse3(ArrayList<Course> courses) 
    {
        this.courses = courses;
    }

    public void setcourses(ArrayList<Course> courses) 
    {
        this.courses = courses;
    }

    public ArrayList<Course> getcourses() {
        return courses;
    }


    
    public Date getBirthDate() {
        return birthDate;
    }

    public void setBirthDate(Date birthDate) {
        this.birthDate = birthDate;
    }

    public Date getAdmissionDatee() {
        return admissionDatee;
    }

    public void setAdmissionDatee(Date admissionDatee) {
        this.admissionDatee = admissionDatee;
    }

    // public void addCourse (Course courses){
    //     if (!courses.contain(Course))
    //     courses.add(Course);
    //     else
    //     System.out.println("already enrolled");
    // }
    public void addCourse(Course course)
    {
        if (!courses.contains(course)) 
        {
            courses.add(course);
        } 
        else 
        {
            System.out.println("already enrolled");
        }
    }


    public void removeCourse (Course course)
    {
        if (courses.contains(course))
        {
            
        }
    }

    @Override
    public  String account()
    {
        return "abstratct method";
    }

    public String toString() {
        return String.format("=============================================================\nName                          Registration no.   Semester %n%-30s%-19s%s%nBirth date : %s%nAdmission Date: %s%n=============================================================\n%s%n%s",
        super.toString(), regNo, semester,birthDate,admissionDatee, "                        Student's courses\n\nCourse Name                   Course code        Credit hours", getcourses());
    }
}
// cant create object of an abstract class
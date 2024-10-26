package CMS;

public class Course 
{
    private String courseName;
    private String coursecode;
    private int credithours;

    public Course(String courseName, String courseCode , int creditHours)
    {
        this.courseName = courseName;
        this.coursecode = courseCode;
        this.credithours = creditHours;
    }


    public void setcourseName(String courseName)
    {
        this.courseName = courseName;
    }
     public String getcourseName()
    {
        return courseName;
    }


    public void setcoursecode(String coursecode)
    {
        this.coursecode = coursecode;
    }
    public String getcoursecode()
    {
        return coursecode;
    }

    
    public void setCredithours(int credithours) 
    {
        this.credithours = credithours;
    }
    public int getCredithours() 
    {
        return credithours;
    }

    public String toString()
    {
        // return String.format("Course Name                   Course code        Credit hours%n%-30s%-19s%s", courseName, coursecode, credithours);
        return String.format("%-30s%-19s%s", courseName, coursecode, credithours);
    }


    


}

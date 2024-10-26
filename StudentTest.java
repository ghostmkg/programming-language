package CMS;
import java.util.ArrayList;

public class StudentTest 
{
    public static void main(String[] args) 
    {
        ArrayList<Course>courses = new ArrayList<>();//to store student courses
        ArrayList<Course>teacher = new ArrayList<>();//to store faculty courses

        /* Declaring objects for courses */
        Course course1 = new Course("Object Oriented Programming", "CS-111", 4);
        Course course2 = new Course("DLD", "CS-121", 3);
        Course course3 = new Course("Linear Algebra", "CS-131", 3);
        Course course4 = new Course("Artificial intelligence", "CS-xyz", 3);
        
        /* Declaring Date Classe's objects */
        Date birthDay = new Date(29, 10, 2002);
        Date birthDay2 = new Date(30, 3, 1985);
        Date admissionDate = new Date(1, 11, 2023);
        Date hiringDate = new Date(1, 3, 2019);
        

        /* Decalring student's object */
        Student Student1 = new Student("Wasiq", "!4301 01 473647", "4353463456", "koaht", "cs213235", "2nd semester", course1, course2, course3, courses, birthDay2, admissionDate);
        
        /* Decalring faculty's object */
        Faculty Teacher = new Faculty(null, null, null, null, null, 0, courses, birthDay, hiringDate);
        
        
        /* adding courses to array named courses */
        courses.add(new Course("Linear Algebra", "CS-203", 3));
        courses.add(course1);
        courses.add(course2);
        courses.add(course3);
        courses.add(course4);
        
        
        /* adding courses to array named teacher */
        Course teacher1 = new Course("Object oriented Programming", "CS-xyz", 4);
        Course teacher2 = new Course("Data Structures", "CS-xyz", 3);
        teacher.add(teacher1);
        teacher.add(teacher2);
        
        /* Display students info */
        System.out.println(Student1);
        // System.out.println(course1);
        //System.out.println("==============================================================");
        for(Course c: courses)
        System.out.println(c);
        System.out.println("==============================================================");
        System.out.println(Teacher);
        System.out.println(teacher1);
        System.out.println(teacher2);
        /* PROBLEM
         * doesnt display courses properly while using for each loop
         */
        // for(Course t: teacher)
        // System.out.println(teacher);

    }    
}

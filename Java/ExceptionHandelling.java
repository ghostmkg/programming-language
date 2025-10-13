import java.io.*;

class Exceptionhandelling {
    public static void main(String[] args) {
      
        // String s set an empty string and calling getLength()
        String s = "";
      
        try {
            System.out.println(getLength(s));
        }
        catch (IllegalArgumentException e) {
            System.out.println(
                "IllegalArgumentException caught");
        }

        // String s set to a value and calling getLength()
        s = "GeeksforGeeks";
      
        try {
            System.out.println(getLength(s));
        }
        catch (IllegalArgumentException e) {
            System.out.println(
                "IllegalArgumentException caught");
        }

        // Setting s as null and calling getLength()
        s = null;
      
        try {
            System.out.println(getLength(s));
        }
        catch (IllegalArgumentException e) {
            System.out.println(
                "IllegalArgumentException caught");
        }
    }

    public static int getLength(String s)
    {
        if (s == null)
            throw new IllegalArgumentException(
                "The argument cannot be null");
      
        return s.length();
    }
}
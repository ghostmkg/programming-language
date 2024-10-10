import java.io.*;
import java.util.*;
class Ternary
{
    public static void main(String args[])
    {
        int a,b,large;
       
        Scanner s=new Scanner(System.in);
    
        System.out.println("Enter the Number A:");
        a=s.nextInt();
        System.out.println("Enter the Number B:");
        b=s.nextInt();

        large = (a>b) ? a:b;
        System.out.println("Largest Number is:"+large);

    }
    
}
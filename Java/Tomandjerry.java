// Tom and Jerry are playing a game with an integer N that doesn't contain any zeros in its 
// decimal representation. Tom starts first and, on his turn, he can swap any two digits of the integer 
// that are in different positions. Jerry follows by always removing the last digit of the integer.
//  The game continues in turns until there's only one digit left. Determine the smallest integer 
//  Tom can achieve at the end if he plays optimally.

//constraits:10 < N < 109

import java.util.Scanner;

public class Tomandjerry {
    public static void main(String[] args) {
       
         Scanner sc=new Scanner(System.in);
         long n=sc.nextLong();
         long min=Integer.MAX_VALUE;
         long num=n; 

         if(n<100)
           min= num%10;
         else{
           while(num>0){
            long res=num%10;
            if(res<min)min=res;
            num/=10;
        }
    }

    System.out.println(min);
    sc.close();
    }
}


import java.util.*;
class Spy_Recur
{
    int spy(int n,int s,int p)
    {
        int c=0;
        if(n==0)
          {
              if(s==p)
                 return 1;
                 return 0;
                }
            else
               {
                   c=n%10;
                   s=s+c;
                   p=p*c;
                   n=n/10;
                   return spy(n,s,p);
                }
    }
    public static void main()
    {
        Scanner sc=new Scanner(System.in);
        Spy_Recur ob=new Spy_Recur();
        int no,p;
        System.out.println("Enter a no.");
        no=sc.nextInt();
        p=ob.spy(no,0,1);
        if(p==1)
           System.out.print("Spy no.");
           else
              System.out.print("Not Spy");
    }
}
            
            
   
import java.util.*;
class TwinPrime
{
    static int a,b;
    public TwinPrime()
    {
        a=b=0;
    }
    void input()
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter two positive integers");
        a=sc.nextInt();
        b=sc.nextInt();
    }
    int isPrime(int n)
    {
        int c=0;
        for(int i=1;i<=n;i++)
           {
               if(n%i==0)
                  c++;
                }
        return c;
    }
    int twinCheck(int a,int b)
    {
        if(isPrime(a)==2 && isPrime(b)==2 && ((a-b)==2 || (b-a)==2))
           return 1;
           return 0;
    }
    public static void main()
    {
        TwinPrime ob=new TwinPrime();
        ob.input();
        if(ob.twinCheck(a,b)==1)
           System.out.print("Twin prime");
          else
             System.out.print("Not twin prime");
    }
}

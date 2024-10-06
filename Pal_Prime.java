import java.util.*;
class Pal_Prime
{
    int palin(int n)
    {
        int s=0,c;
        while(n>0)
        {
            c=n%10;
            s=s*10+c;
            n=n/10;
        }
        return s;
    }
    int prime(int n)
    {
        int i,c=0;
        for(i=1;i<=n;i++)
           {
               if(n%i==0)
                 c++;
                }
        return c;
        }
    void check(int l,int u)
    {
        int i;
        for(i=l;i<=u;i++)
           {
               if(i==palin(i) && prime(i)==2)
                 System.out.println(i);
                }
            }
    public static void main()
    {
        Scanner sc=new Scanner(System.in);
        Pal_Prime ob=new Pal_Prime();
        int a,b;
        System.out.println("Enter lower and upper range");
        a=sc.nextInt();
        b=sc.nextInt();
        ob.check(a,b);
    }
} 
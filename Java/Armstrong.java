import java.util.*;
class Armstrong
{
    int arm(int n)
    {
        int c,s=0;
        while(n>0)
        {
            c=n%10;
            s=s+(int)(Math.pow(c,3));
            n=n/10;
        }
        return s;
    }
    void range(int l,int u)
    {
        int i;
        for(i=l;i<=u;i++)
          {
              if(i==arm(i))
                System.out.println(i+" ");
            }
        }
    public static void main()
    {
        Scanner sc=new Scanner(System.in);
        Armstrong ob=new Armstrong();
        int lo,up;
        System.out.println("Enter the lower and the upper limits");
        lo=sc.nextInt();
        up=sc.nextInt();
        ob.range(lo,up);
    }
}
    
    
              
      
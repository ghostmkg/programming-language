import java.util.*;
class Perfect
{
    void check(int s,int k,int n)
    {
        if(k==n)
          {
              if(s==n)
                 System.out.print("perfect no.");
                 else
                    System.out.print("Not perfect");
              return;
            }
            else
              {
                  if(n%k==0)
                    {
                        s=s+k;
                        check(s,++k,n);
                    }
                  else
                     check(s,++k,n);
                    }
    }
    public static void main()
    {
        Scanner sc=new Scanner(System.in);
        Perfect ob=new Perfect();
        int no;
        System.out.println("Enter number");
        no=sc.nextInt();
        ob.check(0,1,no);
    }
}
              
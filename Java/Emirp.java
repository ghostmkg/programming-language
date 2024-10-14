import java.util.*;
class Emirp
{   
    public static void main()
    {
        Scanner sc=new Scanner(System.in);
        int n,c=0,c2=0,r=0,i,c1;
        System.out.println("Enter no.");
        n=sc.nextInt();
        
        for(i=1;i<=n;i++)
          {
              if(n%i==0)
                c++;
            }
        while(n>0)
        {
            c1=n%10;
            r=r*10+c1;
            n=n/10;
        }
        for(i=1;i<=r;i++)
          {
              if(r%i==0)
                c2++;
            }
        if(c==2 && c2==2)
          System.out.println("Yes Emirp");
        else
          System.out.println("Not Emirp");
    }
}
    
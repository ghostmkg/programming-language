import java.util.*;
public class creatingfactorial {
    public static void main(String[] args) {
        Scanner ttt = new Scanner(System.in);
        int factorial = 1;
        int n = ttt.nextInt();
        for(int i =1 ; i<=n ; i++){
            factorial = factorial*i;
        }
        System.out.println(factorial);
    }
}

package Cube_3D;

import java.util.*;
public class Patterns {
   public static void main(String[]args){
   
    System.out.println("1. Print The Pattern Of Solid Rectangle");

    Scanner sc = new Scanner(System.in);
    System.out.println("Please enter a total number of lines");
    int n = sc.nextInt();           //  4
    System.out.println("Please enter a total number of Stars");
    int m = sc.nextInt();           // 5

    for(int i=1;i<=4;i++){
        for(int j = 1;j <= 5;j++){
        System.out.print("*");
        }
        System.out.println("");   
    }
    System.out.println("Here We are Print 4 rows Star");
    for(int i =1;i<=4;i++){
        System.out.println("*");
    }



    System.out.println("2. Print The Pattern Of Hollow Rectangle");

    System.out.println("Please enter a total number of lines");
    n = sc.nextInt();           //  4
    System.out.println("Please enter a total number of Stars");
    m = sc.nextInt();           // 5

    for(int i = 1 ; i <= n ; i++){
        
        for(int j = 1 ; j <= m ; j++){
           if(i==1 || i==n || j==1 ||j==m){
             System.out.print("* ");
           }else{
                System.out.print("  ");
           }
            
            }
        System.out.println("");
    }




    System.out.println("3. Print The Pattern Of Half Pyramid");
  
    System.out.println("Please enter a total number of lines");
     n = sc.nextInt();       // 4 

    for(int i = 1;i <= n ; i++){
        for(int j = 1;j <= i ;j++){
            System.out.print("*");
        }
        System.out.print( "\n");
    }




    System.out.println("4. Print The Pattern Of Inverted Half Pyramid");
  
    System.out.println("Please enter a total number of lines");
     n = sc.nextInt();       // 4 

    for(int i = 1 ; i <= n ;i++ ){
        for(int j = n ; j >= i ;j--){
           System.out.print("*"); 
        }
        System.out.println( "");
    }



    System.out.println("5. Print The Pattern Of Half Pyramid Rotated By 180 degree");

    System.out.println("Please enter a total number of lines");
     n = sc.nextInt();       // 4 

    for(int i = 1 ; i <= n ;i++ ){
        for(int k = n-i ; k >= 1 ; k--){
             System.out.print(" ");
        }
            for(int j = 1 ; j <= i ;j++){
            System.out.print("*"); 
            }
        
        System.out.println( "");
    }



    System.out.println("6. Print The Pattern Of Half Pyramid with Numbers");

    System.out.println("Please enter a total number of lines");
     n = sc.nextInt();       // 4 

     for(int i = 1 ; i<=n ;i++){
        for(int j = 1; j <= i ;j++){
            System.out.print(j);
        }
        System.out.println("");
     }




    System.out.println("7. Print The Pattern Of Inverted Half Pyramid with Numbers");

    System.out.println("Please enter a total number of lines");
    n = sc.nextInt();       // 4 

    for (int i = n; i >= 1; i--) {
        for(int j = 1 ; j <= i ; j++){
            System.out.print(j);
        }
       System.out.println();   
      }



    System.out.println("8. Print The Pattern Of Floyd's Triangle");

    System.out.println("Please enter a total number of lines");
    n = sc.nextInt();       // 4 
    int num =1;
      for(int i = 1 ; i <= n ; i++){
        for(int j = 1 ; j <= i; j++ ){
            System.out.print(num+" ");
            num++;
        }
         
        System.out.println();
      }



    System.out.println("9. Print The Pattern Of 0 - 1  Triangle");

    System.out.println("Please enter a total number of lines");
    n = sc.nextInt();       // 4 
    
      for(int i = 1 ; i <= n ; i++){
        for(int j = 1 ; j <= i; j++ ){
            
            if((i+j)%2 == 0){
                System.out.print(1);
            }else
            System.out.print(0);
            
        }
         
        System.out.println();
      }


      // QUE 10 .  Print a solid rhombus.

                        // HOMEWORK -> LECTURE  4
    System.out.println("10. Print The Pattern Of solid rhombus");

    System.out.println("Please enter a total number of lines");
    n = sc.nextInt();  
    
    for(int i = 1 ;i <= n ; i++){
        for(int k = n-i; k >= 1  ;k--){
            System.out.print(" ");
        }
            for(int j = 1 ; j <= n ; j++){
                System.out.print("* ");
            }
        System.out.println( );
    }     




    //  QUE 11.       Print a number pyramid

    System.out.println("11. Print The Pattern Of Number Pyramid");

    System.out.println("Please enter a total number of lines");
    n = sc.nextInt();  
    int value = 1;
    for(int i = 1 ; i <= n ; i++){
        for(int k = n-i; k >= 1 ; k--){
            System.out.print(" ");
        }
        for(int j = 1 ; j <= i ; j++ ){
            System.out.print(value+" ");
        }
        value++;
        System.out.println( );
    }    
    
   



    //  QUE 12.  Print a palindromic number pyramid.

    System.out.println("12. Print The Pattern Of Palindromic Number Pyramid");

    System.out.println("Please enter a total number of lines");
    n = sc.nextInt();  
    System.out.println("Please enter a total number of Values");
    int values = sc.nextInt();           

    for(int i = 1 ; i <= n ; i++ ){
        for(int k = n-i ; k >= 1 ; k--){
            System.out.print(" ");
        }
        for(int j = i ; j >= 2; j-- ){
            System.out.print(j);
        }
        for(int  j = 1 ; j <= i ; j++){
            System.out.print(j);
        }
        
        System.out.println( );
    }




     //  QUE 13.  Print a Butterfly pattern.

    System.out.println("12. Print The Pattern Of Butterfly");

    Scanner s4 = new Scanner(System.in);
    System.out.println("Please enter a total number of lines");
    int n1 = s4.nextInt();  
     
    for(int i = 1 ;i <= n1 ; i++ ){
        for(int j = 1 ; j <= i ; j++){
            System.out.print("*");
        }
        for(int k = n1-i ; k >= 1 ;k--){
            System.out.print(" ");
        }
        for(int k = n1-i ; k >= 1 ;k--){
            System.out.print(" ");
        }
        for(int j = 1 ; j <= i; j++){
            System.out.print("*");
        }
        System.out.println();
    }

    for(int i = n1 ;i >= 1 ; i-- ){
        for(int j = 1 ; j <= i ; j++){
            System.out.print("*");
        }
        for(int k = n1-i ; k >= 1 ;k--){
            System.out.print(" ");
        }
        for(int k = n1-i ; k >= 1 ;k--){
            System.out.print(" ");
        }
        for(int j = 1 ; j <= i; j++){
            System.out.print("*");
        }
        System.out.println();
    }


    




   } 
}

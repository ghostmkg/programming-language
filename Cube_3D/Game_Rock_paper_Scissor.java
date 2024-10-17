package Cube_3D;

import java.util.Random;
import java.util.Scanner;

public class Game_Rock_paper_Scissor {
   
    public static void main(String [] args){
        
        // human chosses
        Scanner sc = new Scanner (System.in);
        
        System.out.println("Its Your Turn!");
       
        System.out.println("Hello ! Human Please Enter Your Choice For Playing\n\n\t\t\"Rock\tPaper\tScissor\"\n");
        System.out.println("0. For Scissor\t1. For Paper\t2. For Rock\t");
        
        int human = sc.nextInt(3);
        System.out.println("A Number Is Choose By Human Is: " + human);

        // computer chooses
        Random rnd = new Random();
        
        System.out.println("\nHello ! Computer Please Enter Your Choice For Playing\n\n\t\t\"Rock\tPaper\tScissor\"\n");
        System.out.println("0. For Scissor\t1. For Paper\t2. For Rock\t");
        
        int computer = rnd.nextInt(3);
        System.out.println(computer);
        System.out.println("A Number Is Choose By Computer Is: " + computer);
        
        // LOGIC FOR SHOW THE ACTIVITY !
        
        if(human == 0)
            System.out.println("\n Human Choose Scissor ");
        if(human == 1)
            System.out.println("\n Human Choose Paper ");
        if(human == 2)
            System.out.println("\n Human Choose Rock\n");
        
        if(computer == 0)
            System.out.println("\n Computer Choose Scissor ");
        if(computer == 1)
            System.out.println("\n Computer Choose Paper ");
        if(computer == 2)
            System.out.println("\n Computer Choose Rock ");
            
        // LOGIC FOR WON !
        
        if(human == 0 && computer == 1 || human == 1 && computer == 2 || human == 2 && computer == 0 ){
            System.out.println("\n Human is WIN !");
        }
        else if (human == computer){
             System.out.println("\n OOPS ! Game Is Tie Play Again..");
        }
        else 
            System.out.println("\n Computer is WIN !");
        
        
    }
}

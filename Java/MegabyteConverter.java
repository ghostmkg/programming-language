// Question is provided below The Actual Code.
// I am using main method because I'm using intellij-idea.

public class MegabyteConverter {
    public static void main(String[] args) {
        PrintMegaByteAndKiloByte(-1032); // insert different values and check if the program is working properly.
    }
    public static void PrintMegaByteAndKiloByte(int Kilobyte){
        int megaBytes=0;
        int kiloBytes=0;
        //invalid option
        if(Kilobyte <0){
            System.out.println("Invalid value");
        }else{
        //Calculation
            megaBytes = Kilobyte /1024;
            kiloBytes = Kilobyte % 1024;
            System.out.println(Kilobyte + " KB = " + megaBytes + " MB and " + kiloBytes + " KB " );
        }
    }
}


// Write a method called printMegabytesAndKiloBytes that has 1 parameter of type int with the name kiloBytes.
// 
// The method should not return anything (void) ans it nees to calculate the megabytes and remaining kilobytes from the kilobytes parameter.
//
// Then it needs to print a message in the format "XX KB = YY MB and ZZ KB".
//
// XX represents kiloBytes
// YY represents megabytes
// ZZ represents remaining kilobytes
//
// for example when the parameter kilobytes is 2500 it needs to print "2500 KB = 2 MB and 452 KB"
// if the parameter kiloBytes is less than 0 then print the text "Invalid Value"
//
// TIP : Use remainder operator
// TIP : Do not set kilobytes parameter value inside your method.
//
//
//
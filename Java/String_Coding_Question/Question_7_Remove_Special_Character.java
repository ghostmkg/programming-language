package programming;

public class Question_7_Remove_Special_Character {
     static String remove(String str){
         StringBuilder stringBuilder = new StringBuilder();
         for(int i =0;i<str.length();i++){
             int ascii = str.charAt(i);
             if((ascii>=65 && ascii<=90) || (ascii>=97 && ascii<=122)){
                 stringBuilder.append((char)(ascii));
             }
         }
         return stringBuilder.toString();
     }
    public static void main(String[] args) {
         String string ="12%@#$ Anmol12 %@#$";
        System.out.println(remove(string));

    }
}

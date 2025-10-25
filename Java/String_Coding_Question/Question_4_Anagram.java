package programming;

public class Question_4_Anagram {
     public static boolean isAnagram(String str1,String str2){
         str1 =str1.toLowerCase();
         str2 = str2.toLowerCase();
         int [] count = new int[256];
         if(str1.length()!=str2.length()){
             return false;
         }

         for(int i =0;i<str1.length();i++){
             char ch = str1.charAt(i);
             count[ch]++;
         }
         for(int i = 0;i<str2.length();i++) {
             char ch  = str2.charAt(i);
             count[ch]--;
         }
         for(int i =0;i<256;i++){
             if(count[i]!=0){
                 return false;
             }
         }
         return true;
     }
    public static void main(String[] args) {
         String str1 = "GauravSy";
         String str2 ="Sauravg";
        System.out.println(isAnagram(str1, str2));


    }
}

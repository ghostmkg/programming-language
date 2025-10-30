package programming;

public class Question_3_Remove_Vowel {
    static boolean isVowel(char ch){
        ch = Character.toLowerCase(ch);
        return ch=='a'|| ch=='e'||ch=='i'||ch=='o'||ch=='u';
    }
    static String remove(String str){
        StringBuilder stringBuilder = new StringBuilder();
        for(char ch : str.toCharArray()){
            if(!isVowel(ch)){
                stringBuilder.append(ch);
            }
        }
        return stringBuilder.toString();
    }
    public static void main(String[] args) {
        String s = "gaurav";
        System.out.println(remove(s));



    }
}

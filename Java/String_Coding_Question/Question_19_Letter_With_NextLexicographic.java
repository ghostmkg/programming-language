package programming;

public class Question_19_Letter_With_NextLexicographic {
    public static String Letter_With_NextLexicographic(String str){
        StringBuilder stringBuilder = new StringBuilder();
        for(int i =0;i<str.length();i++){
            int ascii = str.charAt(i);
            if(ascii==90){
                stringBuilder.insert(i,(char)(65));
            } else if (ascii==122) {
                stringBuilder.insert(i,(char)(97));
            }else if((ascii>=65 && ascii<90) ||(ascii>=97 && ascii<122)){
                stringBuilder.insert(i,(char)(ascii+1));
            }
        }
        return stringBuilder.toString();
    }
    public static void main(String[] args) {
        String s = "JAVA";
        String s1 = Letter_With_NextLexicographic(s);
        System.out.println(s1);

    }
}

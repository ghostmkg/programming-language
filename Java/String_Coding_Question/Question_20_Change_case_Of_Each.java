package programming;

public class Question_20_Change_case_Of_Each {
    public static  String Change_case_Of_Each(String str){
        StringBuilder stringBuilder = new StringBuilder();
        for(int i =0;i<str.length();i++){
            char ch = str.charAt(i);
            if (ch >= 'A' && ch <= 'Z') {
                // Uppercase to Lowercase
                stringBuilder.append(Character.toLowerCase(ch));
            } else if (ch >= 'a' && ch <= 'z') {
                // Lowercase to Uppercase
                stringBuilder.append(Character.toUpperCase(ch));
            } else {
                // Keep space as it is
                stringBuilder.append(ch);
            }
        }
        return stringBuilder.toString();
    }
    public static void main(String[] args) {
        String string ="jAVA IS A oBJECT pROGRAMMING";
        String s = Change_case_Of_Each(string);
        System.out.println(s);

    }
}

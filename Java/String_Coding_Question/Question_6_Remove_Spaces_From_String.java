package programming;

public class Question_6_Remove_Spaces_From_String {
    static String Remove(String str){
        StringBuilder stringBuilder = new StringBuilder();
        char[]arr = str.toCharArray();
        for(int i =0;i<str.length();i++){
            if(arr[i]!=' '){
                stringBuilder.append(arr[i]);
            }
        }
        return stringBuilder.toString();
    }
    public static void main(String[] args) {
        String string = "Take You Forword";
        System.out.println(Remove(string));

    }
}

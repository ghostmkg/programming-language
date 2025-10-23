package programming;

public class Question_14_Non_repeating {
    static String non_repeating(String str){
        str = str.toLowerCase();
        StringBuilder stringBuilder = new StringBuilder();
        int [] freq = new int[256];
        int i =0;
        while(i<str.length()){
            char ch = str.charAt(i);
            freq[ch]++;
            i++;
        }
        int j =0;
        while(j<str.length()){
            char ch = str.charAt(j);
            if(freq[ch]==1){
                stringBuilder.append(ch);
            }
            j++;
        }
        return stringBuilder.toString().trim();

    }
    public static void main(String[] args) {
        String string = "Google";
        String string1 = non_repeating(string);
        System.out.println(string1);


    }
}

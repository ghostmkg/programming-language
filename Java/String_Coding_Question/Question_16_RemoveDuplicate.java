package programming;

public class Question_16_RemoveDuplicate {
    static String RemoveDuplicate(String str){
        StringBuilder stringBuilder = new StringBuilder();
        int [] freq = new int[256];
        boolean [] visited = new boolean[256];
        int i =0;
        while(i<str.length()){
            char ch = str.charAt(i);
            freq[ch]++;
            i++;
        }
        int j = 0;
        while(j<str.length()){
            char ch = str.charAt(j);
            if(!visited[ch]){
                stringBuilder.append(ch);
                visited[ch]=true;
            }
            j++;
        }
        return stringBuilder.toString();
    }
    public static void main(String[] args) {
        String string = "bcabcf";
        String string1 = RemoveDuplicate(string);
        System.out.println(string1);

    }
}

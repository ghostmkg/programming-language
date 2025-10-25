package programming;

public class Question_13_Frequency_Of_Character {
    static String frequency(String str){
        StringBuilder stringBuilder = new StringBuilder();
        int [] freq = new int[256];
        int i =0;
        boolean[] visited = new boolean[256];
        while(i<str.length()){
            char ch = str.charAt(i);
            freq[ch]++;
            i++;
        }
        int j = 0;
        while(j<str.length()){
            char ch = str.charAt(j);
            if(!visited[ch]){
                stringBuilder.append(ch).append(freq[ch]).append(' ');
                visited[ch]=true;
            }
            j++;

        }
        return stringBuilder.toString().trim();
    }
    public static void main(String[] args) {
        String string = "takeyoyforword";
        String frequency = frequency(string);
        System.out.println(frequency);



    }
}

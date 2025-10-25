package programming;

public class Question_15_Maximum_Repeating_Character {
    static char Maximum_Repeating_Character(String str){
        char ans =' ';
        int max = 0;
        int [] count = new int[256];
        for(int i =0;i<str.length();i++){
            char ch = str.charAt(i);
            if(ch==' ') continue;
            count[ch]++;
            if(count[ch]>max){
                max=count[ch];
                ans=ch;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        String string = "Take u farword";
        char c = Maximum_Repeating_Character(string);
        System.out.println("Maximum repeating Character is : "+c);
    }
}

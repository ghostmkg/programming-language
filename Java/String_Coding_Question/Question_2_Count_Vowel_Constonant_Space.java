package programming;

public class Question_2_Count_Vowel_Constonant_Space {
    public static void count(String str){
        int vowel = 0;
        int constonant = 0;
        int space = 0;
        for(int i =0;i<str.length();i++){
            char ch = str.charAt(i);
            if(ch=='a'|| ch=='e'||ch=='i'||ch=='o'||ch=='u'){
                vowel++;
            }else if(ch>='a'&& ch<='z'){
                constonant++;
            }else if(ch==' '){
                space++;
            }
        }
        System.out.println("Total No. of Vowels "+vowel);
        System.out.println("Total No. of Constonant"+constonant);
        System.out.println("Total No. of Space"+space);

    }
    public static void main(String[] args) {
        String string = "Take u Farword is Awesome";
        count(string);
    }
}

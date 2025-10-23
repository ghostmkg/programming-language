package programming;

public class Question_11_Captiallize_First_And_Last_Character {
    String Capitallize(String str){
        StringBuilder  stringBuilder = new StringBuilder();
        stringBuilder.append(str);
        for(int i =0;i<str.length();i++){
            if(i==0 || i==(str.length()-1)){
                stringBuilder.setCharAt(i,Character.toUpperCase(str.charAt(i)));
            }else if(str.charAt(i)==' '){
                stringBuilder.setCharAt(i-1,Character.toUpperCase(str.charAt(i-1)));
                stringBuilder.setCharAt(i+1, Character.toUpperCase(str.charAt(i+1)));
            }

        }
        return stringBuilder.toString();
    }
    public static void main(String[] args) {
        String string = "take u forword";
        Question_11_Captiallize_First_And_Last_Character question11CaptiallizeFirstAndLastCharacter=new Question_11_Captiallize_First_And_Last_Character();
        String capitallize = question11CaptiallizeFirstAndLastCharacter.Capitallize(string);
        System.out.println("Before Capitallization :"+string);
        System.out.println("After Capitallization :"+capitallize);



    }
}

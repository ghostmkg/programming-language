package programming;

public class Question_9_Remove_Bracket_From_Algebric_expressio {
    String Remove(String str){
        StringBuilder stringBuilder = new StringBuilder();
        for(int i =0;i<str.length();i++){
            char ch = str.charAt(i);
            if(ch!='(' && ch!=')'){
                stringBuilder.append(ch);
            }
        }
        return stringBuilder.toString();
    }
    public static void main(String[] args) {
        String string = "a+(c-d)+b";
        Question_9_Remove_Bracket_From_Algebric_expressio question9RemoveBracketFromAlgebricExpressio=new Question_9_Remove_Bracket_From_Algebric_expressio();
        String remove = question9RemoveBracketFromAlgebricExpressio.Remove(string);
        System.out.println("Before :"+string);
        System.out.println("After :"+remove);


    }
}

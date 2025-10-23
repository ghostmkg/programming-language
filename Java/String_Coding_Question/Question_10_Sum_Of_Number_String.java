package programming;

public class Question_10_Sum_Of_Number_String {
    int Sum(String str){
        String temp ="0";
        int sum = 0;
        for(int i =0;i<str.length();i++){
            char ch = str.charAt(i);
            if(Character.isDigit(ch)){
                temp+=ch;
            }else{
                sum+=Integer.parseInt(temp);
                temp="0";
            }
        }
        return sum+Integer.parseInt(temp);
    }

    public static void main(String[] args) {
        String string ="1XYZ23";
        Question_10_Sum_Of_Number_String question10SumOfNumberString=new Question_10_Sum_Of_Number_String();
        int sum = question10SumOfNumberString.Sum(string);
        System.out.println("Before :"+string);
        System.out.println("After :"+sum);



    }
}

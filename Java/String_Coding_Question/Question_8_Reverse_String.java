package programming;

public class Question_8_Reverse_String {
    String reverse(String str){
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(str);
        stringBuilder.reverse();
        return stringBuilder.toString();
    }
    String Reverse(String str){
        char [] arr = str.toCharArray();
        int start =0;
        int end = arr.length-1;
        while(start<end){
            char temp = arr[start];
            arr[start] = arr[end];
            arr[end]=temp;
            start++;
            end--;
        }
        return new String(arr);
    }
    public static void main(String[] args) {
        String string ="Gaurav";
        Question_8_Reverse_String question8ReverseString = new Question_8_Reverse_String();
        String reverse = question8ReverseString.Reverse(string);
        String reverse1 = question8ReverseString.reverse(string);
        System.out.println("Before Reverse : "+string);
        System.out.println("After Reverse : "+reverse);
        System.out.println("After Reverse : "+reverse1);

    }
}

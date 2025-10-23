package programming;

public class Question_5_Reverse_Sentence {
    public static String reverseSentence(String str) {
        char [] arr = str.toCharArray();
        int start =0;
        int n =arr.length;
        // Pahle sabko Reverse Kar Lenge
        Reverse(arr,start,n-1);
        for(int end =0;end<n;end++){
            if(arr[end]==' '){
                Reverse(arr, start, end-1);
                start=end+1;
            }
        }
        // Jb space aa jayega phir Reverse kar denge aur start ko end+1 kar denge
        Reverse(arr, start, n-1);
        return new String(arr);


    }
    public static void Reverse(char[]arr,int start,int end){
        while(start<end){
            char temp = arr[start];
            arr[start]=arr[end];
            arr[end]=temp;
            start++;
            end--;
        }
    }

    public static void main(String[] args) {
        String string ="Hello World";
        System.out.println(reverseSentence(string));
        System.out.println("Reverse USing StringBuilder :"+reverseSentence(string) +": This is not correct");

    }
}

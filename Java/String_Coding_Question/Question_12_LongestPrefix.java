package programming;

import java.util.Arrays;

public class Question_12_LongestPrefix {
      static String LongestPrefix(String[]arr){
          StringBuilder stringBuilder = new StringBuilder();
          Arrays.sort(arr);
          char[]first = arr[0].toCharArray();
          char[]last =arr[arr.length-1].toCharArray();
          for(int i =0;i<first.length;i++){
              if(first[i]!=last[i]){
                  break;
              }
              stringBuilder.append(first[i]);
          }
          return stringBuilder.toString();

      }
    public static void main(String[] args) {
          String[]strings ={"Flower","Flow","Flight"};
        System.out.println(LongestPrefix(strings));

    }
}

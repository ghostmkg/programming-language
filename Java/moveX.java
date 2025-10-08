package recursion;

public class moveX {

    public static String revstr(String str, int idx){

        if(idx>=str.length()-1){
            return str;
        }

        if(str.charAt(idx)=='x'){

            char[] arr = str.toCharArray();

            char temp = arr[idx];
            arr[idx] = arr[idx+1];
            arr[idx+1] = temp;

            str=new String(arr);
            

        }
        return revstr(str, idx+1);
    }

    public static void main(String[] args) {
        

        String str = "xbcd";
        // int idx = 0;

        revstr(str,0);
        System.out.println(str);
    }
    
}

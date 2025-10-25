import java.util.*;

class Tripletrouble{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for (int i = 0; i < n; i++) {
            arr[i]=sc.nextInt();
        }
        HashMap <Integer, Integer> map=new HashMap<>();
        for (int i = 0; i < n; i++) {
            if(map.containsKey(arr[i])){
                int val=map.get(arr[i]);
                map.put(arr[i],val+1);
            }
            else
               map.put(arr[i],1);
        }

        for(int i:map.keySet()){
            if(map.get(i)<3){
                System.out.println(i);
            }
        }
        sc.close();
    }
}

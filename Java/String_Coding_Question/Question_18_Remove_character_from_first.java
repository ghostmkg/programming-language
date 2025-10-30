package programming;

import java.util.HashMap;

public class Question_18_Remove_character_from_first {
    public static String Remove_character_from_first(String str1,String str2){
        StringBuilder stringBuilder = new StringBuilder();
        HashMap<Character,Integer> map = new HashMap<>();
        for(char ch : str2.toCharArray()){
            map.put(ch,map.getOrDefault(ch, 0)+1);
        }
        for(char ch:str1.toCharArray()){
            if(!map.containsKey(ch)){
                stringBuilder.append(ch);
            }
        }
        return stringBuilder.toString();
    }
    public static void main(String[] args) {
        String string = "abcde";
        String string1 = "cefz";
        String solve = Remove_character_from_first(string, string1);
        System.out.println(solve);


    }
}

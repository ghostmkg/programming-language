public class Atoi {

    public static int aoi(String str) {
        int i = 0, sign = 1, result = 0;
        int n = str.length();

        // Skip leading spaces
        while (i < n && Character.isWhitespace(str.charAt(i))) {
            i++;
        }

        // Check for sign
        if (i < n && (str.charAt(i) == '+' || str.charAt(i) == '-')) {
            sign = (str.charAt(i) == '-') ? -1 : 1;
            i++;
        }

        // Convert digits
        while (i < n && Character.isDigit(str.charAt(i))) {
            result = result * 10 + (str.charAt(i) - '0');
            i++;
        }

        return sign * result;
    }

    public static void main(String[] args) {
        String input = "  +12345";
        System.out.println("Converted integer: " + aoi(input));
    }
}

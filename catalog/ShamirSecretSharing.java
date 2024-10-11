import org.json.JSONObject;
import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class ShamirSecretSharing {

    // Helper function to convert a number from a given base to decimal
    public static BigInteger decodeY(String base, String value) {
        return new BigInteger(value, Integer.parseInt(base));
    }

    // Function to perform Lagrange interpolation and get the constant term
    public static BigInteger lagrangeInterpolation(List<int[]> points) {
        BigInteger result = BigInteger.ZERO;
        for (int[] point1 : points) {
            BigInteger xi = BigInteger.valueOf(point1[0]);
            BigInteger yi = BigInteger.valueOf(point1[1]);

            BigInteger term = yi;

            for (int[] point2 : points) {
                if (point1 != point2) {
                    BigInteger xj = BigInteger.valueOf(point2[0]);
                    term = term.multiply(xj.negate()).divide(xi.subtract(xj));
                }
            }

            result = result.add(term);
        }
        return result;
    }

    public static void main(String[] args) throws Exception {
        // Step 1: Read the input JSON file
        String inputFile = "testcase.json"; // Replace with the path to your JSON file
        BufferedReader reader = new BufferedReader(new FileReader(inputFile));
        StringBuilder jsonStr = new StringBuilder();
        String line;

        while ((line = reader.readLine()) != null) {
            jsonStr.append(line);
        }

        JSONObject jsonObject = new JSONObject(jsonStr.toString());

        // Step 2: Extract n and k from keys
        JSONObject keys = jsonObject.getJSONObject("keys");
        int n = keys.getInt("n");
        int k = keys.getInt("k");

        // Step 3: Extract roots and decode them
        List<int[]> decodedPoints = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            if (jsonObject.has(String.valueOf(i))) {
                JSONObject root = jsonObject.getJSONObject(String.valueOf(i));
                int x = Integer.parseInt(String.valueOf(i));
                String base = root.getString("base");
                String value = root.getString("value");

                BigInteger y = decodeY(base, value);
                decodedPoints.add(new int[]{x, y.intValue()});
            }
        }

        // Step 4: Apply Lagrange interpolation using k points
        List<int[]> pointsToUse = decodedPoints.subList(0, k);
        BigInteger constantTerm = lagrangeInterpolation(pointsToUse);

        // Step 5: Print the constant term (the secret)
        System.out.println("The constant term (c) is: " + constantTerm);
    }
}
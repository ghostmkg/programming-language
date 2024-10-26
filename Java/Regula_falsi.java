import java.util.function.Function;

public class RegulaFalsi {

    public static double regulaFalsi(Function<Double, Double> func, double a, double b, double tol, int maxIter) {
        if (func.apply(a) * func.apply(b) >= 0) {
            System.out.println("Invalid initial guesses.");
            return Double.NaN;
        }

        double c = a;
        for (int i = 0; i < maxIter; i++) {
            c = b - (func.apply(b) * (b - a)) / (func.apply(b) - func.apply(a));

            if (Math.abs(func.apply(c)) < tol) {
                break;
            }

            if (func.apply(c) * func.apply(a) < 0) {
                b = c;
            } else {
                a = c;
            }
        }

        return c;
    }

    public static void main(String[] args) {
        Function<Double, Double> func = x -> x * x * x - x * x + 2;

        double a = -200, b = 300, tol = 1e-6;
        int maxIter = 1000;

        double root = regulaFalsi(func, a, b, tol, maxIter);
        System.out.println("The root is: " + root);
    }
}

public class TowerOfHanoi {

    // Recursive function to solve Tower of Hanoi puzzle
    public static void solve(int n, char fromRod, char toRod, char auxRod) {
        if (n == 1) {
            System.out.println("Move disk 1 from rod " + fromRod + " to rod " + toRod);
            return;
        }
        solve(n - 1, fromRod, auxRod, toRod);
        System.out.println("Move disk " + n + " from rod " + fromRod + " to rod " + toRod);
        solve(n - 1, auxRod, toRod, fromRod);
    }

    public static void main(String[] args) {
        int n = 3; // Number of disks
        System.out.println("Tower of Hanoi solution for " + n + " disks:");
        solve(n, 'A', 'C', 'B');  // A, B and C are names of rods
    }
}

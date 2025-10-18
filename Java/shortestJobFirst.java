import java.util.Arrays;

public class shortestJobFirst {

    // Function to calculate average
    // waiting time using Shortest
    // Job First algorithm
    static float shortestJobFirst(int[] jobs) {
        // Sort the jobs in ascending order
        Arrays.sort(jobs);

        // Initialize total waiting time
        float waitTime = 0;
        // Initialize total time taken
        int totalTime = 0;
        // Get the number of jobs
        int n = jobs.length;

        // Iterate through each job
        // to calculate waiting time
        for (int i = 0; i < n; ++i) {

            // Add current total
            // time to waiting time
            waitTime += totalTime;

            // Add current job's
            // time to total time
            totalTime += jobs[i];
        }

        // Return the average waiting time
        return waitTime / n;
    }

    public static void main(String[] args) {
        int[] jobs = {4, 3, 7, 1, 2};

        System.out.print("Array Representing Job Durations: ");
        for (int i = 0; i < jobs.length; i++) {
            System.out.print(jobs[i] + " ");
        }
        System.out.println();

        float ans = shortestJobFirst(jobs);
        System.out.println("Average waiting time: " + ans);
    }
}
                            

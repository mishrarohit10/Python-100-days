
import java.util.Arrays;
import java.util.Scanner;

public class Airport_Management {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        while(t-- > 0) {
            int n = in.nextInt();
            int[] arr = new int[n];
            int[] dep = new int[n];
            for(int i = 0; i < n; i++) {
                arr[i] = in.nextInt();
            }
            for(int i = 0; i < n; i++) {
                dep[i] = in.nextInt();
            }
            System.out.println(findPlatform(arr, dep));
        }
    }

    private static int findPlatform(int[] arr, int[] dep) {
        Arrays.sort(arr);
        Arrays.sort(dep);

        int result = 1;
        int arrivalndex = 1;
        int departureIndex = 0;
        int platform = 1;

        while(arrivalndex < arr.length && departureIndex < dep.length) {
            int currentArrivalTime = arr[arrivalndex];
            int currentDepartureTime = dep[departureIndex];

            if(currentArrivalTime <= currentDepartureTime) {
                platform++;
                arrivalndex++;
            } else {
                platform--;
                departureIndex++;
            }
            if(platform > result) {
                result = platform;
            }
        }
        return result;
    }
}
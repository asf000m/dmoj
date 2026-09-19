package ccc15j1;

import java.util.Scanner;

public class Problem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int month, day;

        month = sc.nextInt();
        day = sc.nextInt();

        if (month == 2) {
            if (day == 18)
                System.out.println("Special");
            else if (day < 18)
                System.out.println("Before");
            else
                System.out.println("After");
        }
        else if (month < 2)
            System.out.println("Before");
        else
            System.out.println("After");

        sc.close();
    }
}

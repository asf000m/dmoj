package ccc18j1;

import java.util.Scanner;

public class Problem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int digit1, digit2, digit3, digit4;
        boolean isTelemarketer;

        digit1 = sc.nextInt();
        digit2 = sc.nextInt();
        digit3 = sc.nextInt();
        digit4 = sc.nextInt();

        isTelemarketer = (
            (digit1 == 8 || digit1 == 9) &&
            (digit4 == 8 || digit4 == 9) &&
            (digit2 == digit3)
        );

        if (isTelemarketer)
            System.out.println("ignore");
        else
            System.out.println("answer");

        sc.close();
    }
}

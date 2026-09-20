package dmopc16c1p0;

import java.util.Scanner;

public class Problem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int width, extraCheese;
        String satisfaction;

        width = sc.nextInt();
        extraCheese = sc.nextInt();

        if (width == 3 && extraCheese >= 95)
            satisfaction = "absolutely";
        else if (width == 1 && extraCheese <= 50)
            satisfaction = "fairly";
        else
            satisfaction = "very";

        System.out.println("C.C. is " + satisfaction + " satisfied with her pizza.");

        sc.close();
    }
}

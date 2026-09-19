package ccc19j1;

import java.util.Scanner;

public class Problem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int apples1, apples2, apples3, apples;
        int bananas1, bananas2, bananas3, bananas;


        apples3 = sc.nextInt();
        apples2 = sc.nextInt();
        apples1 = sc.nextInt();
        bananas3 = sc.nextInt();
        bananas2 = sc.nextInt();
        bananas1 = sc.nextInt();

        apples = (apples3 * 3) + (apples2 * 2) + apples1;
        bananas = (bananas3 * 3) + (bananas2 * 2) + bananas1;

        if (apples > bananas)
            System.out.println("A");
        else if (apples < bananas)
            System.out.println("B");
        else
            System.out.println("T");

        sc.close();
    }
}

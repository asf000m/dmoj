package ccc13j1;

import java.util.Scanner;

public class Problem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int youngest, middle, oldest;

        youngest = sc.nextInt();
        middle = sc.nextInt();

        oldest = middle + (middle - youngest);

        System.out.println(oldest);

        sc.close();
    }
}

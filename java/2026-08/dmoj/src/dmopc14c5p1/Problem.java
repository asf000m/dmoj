package dmopc14c5p1;

import java.util.Scanner;

public class Problem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // radius r
        double radius = sc.nextDouble();
        // height h
        double height = sc.nextDouble();

        double volume = 1.0/3.0 * Math.PI * radius * radius * height;
//        volume = Math.round(volume);

        System.out.printf("%.2f", volume);

        sc.close();
    }
}

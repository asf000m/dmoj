package dmopc15c7p2;

import java.util.Scanner;

public class Problem {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();
        int length = input.split(" ").length;

        System.out.println(length);

        sc.close();
    }
}

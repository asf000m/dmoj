package wc16c1j1;

import java.util.Scanner;

public class Problem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // spookiness level
        int spookiness = sc.nextInt();

        String word = "sp" + "o".repeat(spookiness) + "ky";

        System.out.println(word);

        sc.close();
    }
}

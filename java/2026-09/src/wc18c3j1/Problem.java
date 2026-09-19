package wc18c3j1;

import java.util.Scanner;

public class Problem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int paint, cover, price, badges, paintLeft, selledBadges, totalEarned;

        paint = sc.nextInt();
        cover = sc.nextInt();
        price = sc.nextInt();

        badges = paint / cover;
        paintLeft = paint % cover;

        selledBadges = badges * price;

        totalEarned = selledBadges + paintLeft;

        System.out.println(totalEarned);
        
        sc.close();
    }
}

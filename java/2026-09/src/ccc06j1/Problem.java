package ccc06j1;

import java.util.Scanner;

public class Problem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int choice1, choice2, choice3, choice4;
        int totalCalories = 0;

        choice1 = sc.nextInt();
        choice2 = sc.nextInt();
        choice3 = sc.nextInt();
        choice4 = sc.nextInt();

        // Burger choices.
        switch (choice1) {
            case 1:
                totalCalories += 461;
                break;
            case 2:
                totalCalories += 431;
                break;
            case 3:
                totalCalories += 420;
                break;
            case 4:
                break;
        }

        // Side choices.
        switch (choice2) {
            case 1:
                totalCalories += 100;
                break;
            case 2:
                totalCalories += 57;
                break;
            case 3:
                totalCalories += 70;
                break;
            case 4:
                break;
        }

        // Drink choices.
        switch (choice3) {
            case 1:
                totalCalories += 130;
                break;
            case 2:
                totalCalories += 160;
                break;
            case 3:
                totalCalories += 118;
                break;
            case 4:
                break;
        }

        // Dessert choices.
        switch (choice4) {
            case 1:
                totalCalories += 167;
                break;
            case 2:
                totalCalories += 266;
                break;
            case 3:
                totalCalories += 75;
                break;
            case 4:
                break;
        }

        System.out.println("Your total Calorie count is " + totalCalories + ".");

        sc.close();
    }
}

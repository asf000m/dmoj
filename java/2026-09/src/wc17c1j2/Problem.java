package wc17c1j2;

import java.util.Scanner;

public class Problem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int celcius, fahrenheit;

        celcius = sc.nextInt(); 

        fahrenheit = (int) ((9.0 / 5.0) * celcius + 32);

        System.out.println(fahrenheit);

        sc.close();
    }
}

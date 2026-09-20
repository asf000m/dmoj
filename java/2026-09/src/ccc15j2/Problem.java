package ccc15j2;

import java.util.Scanner;

public class Problem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int idxStart = 0, idxEnd = 3;
        int happy = 0, sad = 0;
        String message, subStr;

        message = sc.nextLine();

        for (int i = 0; i < (message.length() - 2); i++) {
            subStr = message.substring(idxStart + i, idxEnd + i);
            
            if (":-)".equals(subStr))
                happy++;
            else if (":-(".equals(subStr))
                sad++;
        }

        if (happy == 0 && sad == 0)
            System.out.println("none");
        else {
            if (happy > sad)
                System.out.println("happy");
            else if (sad > happy)
                System.out.println("sad");
            else
                System.out.println("unsure");
        }

        sc.close();
    }
}

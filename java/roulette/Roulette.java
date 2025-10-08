import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class Roulette {
    
    public static void main(String[] args) 
    {
        //Betting
        int points = 20;
        int result = 0;
        Scanner sc = new Scanner(System.in);
        int inputOption = 0;
        int chosenNumber = 0;
        int bettingAmout = 0;
        final int FACTOR_SINGLE_WIN = 35;
        final int FACTOR_COLOR_WIN = 2;

        //Roulette board 
        final int MAX_NUMBERS = 37;
        final String RED = "Red";
        final String BLACK = "Black";
        final String GREEN = "Green";
        String[] colors = new String[MAX_NUMBERS];
        colors[0] = GREEN;

        for (int i = 1; i+1 < MAX_NUMBERS; i= i+2) 
        {
            colors[i] = RED;
            int j = i+1;
            colors[j] = BLACK;
        }

        while(true)
        {
            System.out.println("Enter (1) for single bet, (2) for Red and (3) for Black");

            //drawing result
            result = ThreadLocalRandom.current().nextInt(0, 37);

            //check against non-numbers
            inputOption = sc.nextInt();

            switch (inputOption) 
            {
                case 1: //Wager single bet
                    
                    System.out.println("On which number do you like to bet?");
                    chosenNumber = sc.nextInt();
                    
                    //Insert check for wager more then balance in all switch cases + check against non-numbers
                    System.out.println("How much do you like to wager? - " + "You have " + points + " points");
                    bettingAmout = sc.nextInt();
                    points = points - bettingAmout;

                    System.out.println("The winner is " + result + " " + colors[result] + "!");

                    if(chosenNumber == result)
                    {
                        System.out.println("You won " + (bettingAmout*FACTOR_SINGLE_WIN) + " points!");
                        points = points + (bettingAmout*FACTOR_SINGLE_WIN);
                        System.out.println("New balance: " + points + " points" );
                    }
                    else
                    {
                        System.out.println("What a bummer, you lost " + bettingAmout + " points..." + " Better luck next time!");
                    }
                    
                    break;
                case 2: //Wager Red
                    
                    System.out.println("How much do you like to wager? - " + "You have " + points + " points");
                    bettingAmout = sc.nextInt();
                    points = points - bettingAmout;

                    System.out.println("The winner is " + result + " " + colors[result] + "!");
                    if(colors[result].equals(RED))
                    {
                        System.out.println("You won " + (bettingAmout*FACTOR_COLOR_WIN) + " points!");
                        points = points + (bettingAmout*FACTOR_COLOR_WIN);
                        System.out.println("New balance: " + points + " points" );
                    }
                    else
                    {
                        System.out.println("What a bummer, you lost " + bettingAmout + " points..." + " Better luck next time!");
                    }
                    
                    break;
                case 3://Wager Black
                    
                    System.out.println("How much do you like to wager? - " + "You have " + points + " points");
                    bettingAmout = sc.nextInt();
                    points = points - bettingAmout;

                    System.out.println("The winner is " + result + " " + colors[result] + "!");

                    if(colors[result].equals(BLACK))
                    {
                        System.out.println("You won " + (bettingAmout*FACTOR_COLOR_WIN) + " points!");
                        points = points + (bettingAmout*FACTOR_COLOR_WIN);
                        System.out.println("New balance: " + points + " points" );
                    }
                    else
                    {
                        System.out.println("What a bummer, you lost " + bettingAmout + " points..." + " Better luck next time!");
                    }
                    break;

                default:
                System.out.println("Error, false input");
                    break;
            }

            //Insert check for balance = 0
            
            System.out.println("Wanna play again? - 1 = Yes | 2 = No");
            inputOption = sc.nextInt();
            
            if(inputOption == 2)
            {
                System.out.println("Have a nice day and come back soon <3");
                sc.close();
                break;
            }
        }
    }
}

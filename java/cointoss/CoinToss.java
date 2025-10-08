import java.util.Scanner ;
import java.util.concurrent.ThreadLocalRandom;

public class CoinToss
{
    public static void main(String[] args) 
    {
        
        System.out.println(basicVersion());
        
        advancedVersion();
        
    }

    public static String basicVersion(){

        int outcome = ThreadLocalRandom.current().nextInt(2);
        String heads = "Heads";
        String tails = "Tails";

        if(outcome == 0)
        {
            return heads;
        }
        else if(outcome == 1)
        {
            return tails;
        }
        else
        {
            return "Error";
        }
    }
    
    public static void advancedVersion(){
        
        Scanner sc = new Scanner(System.in);
        int outcome = 0;
        int bet = 0;

        System.out.println("Heads (1) or Tails (2) ?");
        
        try 
        {
            while (bet != 1  && bet != 2)
            {
                bet = sc.nextInt();
            }
        } 
        catch (Exception e) 
        {
            System.out.println("Error: "+e);
        }    
          
        outcome = (ThreadLocalRandom.current().nextInt(1,3));
        
        if (bet == outcome)
        {
            System.out.println("You win!");
        }
        else
        {
            System.out.println("You lose!");
        }
    }
}
import java.util.concurrent.ThreadLocalRandom;

public class DiceRoll {

    public static void main(String[] args) {
        
        System.out.println("Lets roll the dice!");

        int limit = 100000;
        int[] results = new int[6];

        //System.out.println(results.length);

        for(int i = 0; i < limit; i++){
            
            int outcome = 0;
            
            outcome = ThreadLocalRandom.current().nextInt(1,7);

            results[outcome-1]++;

            //System.out.print(outcome);
        }

        for(int i = 0; i < results.length; i++){
        
            System.out.println("Number " + (i+1) + ": " + results[i]);
        }

    }
    
}
class Main {
    public static void main(String[] args) {
        
        Thread t1 = new Thread (() ->{
            
           for(int i = 1; i <= 10; i++){
            try{
                Thread.sleep(1000);
            }
            catch(InterruptedException e){
                System.out.println("Thread wurde unterbrochen");
            }
            
             System.out.println(i);
             
            }
       });
        
        Thread t2 = new Thread (() ->{
            
            for(int j = 1; j <= 10; j++){
            try{
                Thread.sleep(500);
            }
            catch(InterruptedException e){
                System.out.println("Thread wurde unterbrochen");
            }
            
            int wieOft = 0;
            
                wieOft = wieOft + j;
                 System.out.println("warte");
            }
            
        });
        
        System.out.println("Threads fangen jetzt an");
        System.out.println("");
        
        t1.start();
        t2.start();
        
        try{
            t1.join();
            t2.join();
        }
        catch(InterruptedException e){
            System.out.println("Thread wurde unterbrochen");
        }
        System.out.println("");
        System.out.println("Threads beendet");
        
    }
}

import java.util.*;

public class app11 {
    public static void main(String[] args) {
        ArrayList<Integer> a = findPrime(100);
        for(int z = 0; z < a.size();z++){
            System.out.println(a.get(z));
        }
    }
    public static ArrayList<Integer> findPrime(int limit) {
        ArrayList<Integer> primes = new ArrayList<>(1);
        
        for(int i= 1;i< limit;i++){
            int numfact = 0;
            
            for(int y = i; y > 0; y= y- 1){
                
                if(i % y==0){
                    numfact++;
                    
                }
                
            }
            if(numfact == 2){
                primes.add(i);
            } 
            
        }
        
        
        
        return primes;


    }
}

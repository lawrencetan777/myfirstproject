



class app3 {
    public static void main( String[] args) {
        findFactors(10);
        
    }
    static void findFactors(int num){
        int[] factors = new int[num];
        int n = 0;
        for(int i = 1 ;i< num; ++i){
            
            if (num % i == 0 && contains(num/i , factors)== false){
                factors[n] = i;
                n++;
                factors[n] = num/i;
                n++;


            }
        }
        
        
        for(int z = 0;z< factors.length;z++){
            if (factors[0] == 1 && factors[1] == num && factors[2] == 0){
                System.out.println("prime");
                break;
            }
            if (factors[z] != 0){
            System.out.println(factors[z]);
            }else{
            
            break;
            }


        }

        
        
        

    }
    static boolean contains(int key, int[] list){
        boolean test = false;
        for (int element : list) {
            if (element == key) {
                test = true;
                break;
                
            }
        }
        return test;
    }
    
}

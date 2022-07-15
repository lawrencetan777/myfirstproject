package javaapps;


public class app10 {
    public static String[] newfunct(int limit){
        String[] res = new String[limit];
        for(int x = 0;x < limit; x++){
            if( x % 3  == 0){
                if(x % 5 == 0){
                    res[x] = "BuzzFizz";
                    continue;

                } else if (x % 5  != 0){
                    res[x] = "Fizz";
                    continue;
                }
            }
            else if( x % 5 == 0 && x % 3 != 0){
                res[x] = "Buzz";
                continue;
            }
            else{
                String a = Integer.toString(x);
                res[x] = a;
            }
        }
        
        
        return res;

    }
    public static void main(String[] args) {
        String[] a = newfunct(100);
        for(int z = 0; z< a.length; z++){
            System.out.println(a[z]);
        }
    }
    
}

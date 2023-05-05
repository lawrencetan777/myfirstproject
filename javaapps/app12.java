import java.util.Hashtable;

class app12 {

    public static void main(String[] args) {
        String word = "begin"; 
        int value = findValue(word);
        System.out.println(value);

    }
    static int findValue(String word){
        String alphabetKey = " abcdefghijklmnopqrstuvwxyz"; 
        Hashtable<String, Integer> alphabet = new Hashtable<String, Integer>();
        for(int i = 0 ; i < alphabetKey.length(); i++){
            alphabet.put(String.valueOf(alphabetKey.charAt(i)), i);
        }
        
        int value = 0;
        for(int i = 0 ; i < word.length(); i++){
            value += alphabet.get(String.valueOf(word.charAt(i)));
        }
        
        
        
        return value;
    }



}
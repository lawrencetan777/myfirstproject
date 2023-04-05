

public class app7 {
    public static void main(String[] args){
        Human aHuman =new Human("Bob", 25, "pasta");
        human_introduce(aHuman);
        Human anotherHuman =new PigLatinSpeaker("Joe", 35, "tacos");
        human_introduce(anotherHuman);

        Human audria =new Human("Audria", 13, "banana");
        human_introduce(audria);

        Human lawrence =new PigLatinSpeaker("Lawrence", 11, "noodles");
        human_introduce(lawrence);


        Athlete athlete = new Athlete("Robert" ,29,"noodles","soccer");
        human_introduce(athlete);
    }

    static void human_introduce( Human human){
        System.out.println(human.introduceYourself());
    }

    static class Human{
        String name;
        int age;
        String favoriteFood;

        Human(String name, int age, String favoriteFood){
            this.name = name;
            this.age = age;
            this.favoriteFood= favoriteFood;
        }

        public String introduceYourself(){
            return "My name is "+ name + " and I'm " + age + " my favorite food is " + favoriteFood + " Have a nice day goodnight";
        }
    }

    static class Athlete extends Human{
        String sport;
        public Athlete(String name, int age, String favoriteFood, String sport) {
            super(name, age, favoriteFood);
            this.sport = sport;
        }
        public String introduceYourself(){
            return "I am a " + sport + " player. Call me " + name + ".";
        }    
    }
    
    static class PigLatinSpeaker extends Human{
 
        public PigLatinSpeaker(String name, int age, String favoriteFood) {
            super(name, age, favoriteFood);
        }

        public String introduceYourself(){
            String msg = super.introduceYourself();
            return pigLatinize(msg);
        }

        private String pigLatinize(String msg) {
            String[] words = msg.split(" ");
            String s = "";
            for (String w : words) {
                s += pigLatinizeWord(w) + " ";
            }
            return s;
        }
        private String pigLatinizeWord(String word) {
            String vowels = "aeiou";
            if (vowels.indexOf(word.substring(0,1).toLowerCase()) >=0){
                // if start with vowel, add yay
                return word + "yay";
            } else {
                // count number of consecutive consonants
                int c=0;
                for (;c<word.length();c++) {
                    boolean isVowel = vowels.indexOf(word.substring(c,c+1).toLowerCase())>=0;
                    if (isVowel) {
                        break;
                    } else {
                        if (word.substring(c,c+1).toLowerCase().equals("y") && c > 0) {
                            break;
                        }
                    }
                }
                word = word.substring(c) + word.substring(0, c) + "ay";
            }

            return word;
        }

    }



}

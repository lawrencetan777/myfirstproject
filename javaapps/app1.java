package javaapps;


class imbored {

    public static void main(String args[]){
        double height1 = Math.random();
        height1 = height1 * 2;
        human bobmccaffery = new human( 24 , height1, 126, "bob mccaffery", "farmer" );
        double bobheight = bobmccaffery.findH();
        System.out.println(bobheight);




        
    }
    
}
class human {
    int age;
    double height;
    int weight;
    String name;
    String occupation;
    public human ( int newage, double newheight, int newweight, String newname, String newoccupation ){
        age = newage;
        height =newheight;
        weight = newweight;
        name = newname;
        occupation =newoccupation;
        
    }
    double findH (){
        return height; 
    }


}

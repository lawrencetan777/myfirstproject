package javaapps;



class student{
    String name;
    int id;
    public void setid(int x){
        id = x;
    }


}
class Collegestudent extends student{
    String course;
    
    public Collegestudent(){
        this.course = "blah";
        
    }
    public void setidb(int a){
        super.setid(a);
    }
}
class a{
    public static void main( String[] args) {
        Collegestudent one = new Collegestudent();
        one.setidb(2354);
        System .out.println(one.id);
    }
}
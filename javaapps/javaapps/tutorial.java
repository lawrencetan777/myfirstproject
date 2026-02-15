
package javaapps;
import java.util.Scanner;
//tells program what folder its in
class tutorial{
    //object and code is in this object

    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);

        System.out.println("press enter ");
        
        

        


    String[] stringlist = {"Hello,","Dear","Hi,","Greetings,"};

    int random = (int) Math.ceil(Math.random() * 3);

    scan.nextLine();
    System.out.println(stringlist[random]);

    scan.close();





    }

    
}
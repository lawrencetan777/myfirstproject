

class app4{
    public static void main(String[] args) {
        int[] arr = new int[] {1,7,23,45,60};
        int[] dep = new int[] {5,25,29,65,69};
        
        System.out.println(calcTrainPlat(arr,dep));
    }
    static int calcTrainPlat(int[] arrival, int[] departure){
        int plat = 0;
        int[] t1 = new int[70];
        int[] t2 = new int[70];
        int[] t3 = new int[70];
        int[] t4 = new int[70];
        int[] t5 = new int[70];
        for( int y1 = 0;y1<=69;y1++){
            if( y1 >= arrival[0] && y1 < departure[0]){
                t1[y1] = 1;

            }
            else{
                t1[y1] = 0;
            }
        }
        for( int y2 = 0;y2<=69;y2++){
            if( y2 >= arrival[1] && y2 < departure[1]){
                t2[y2] = 1;

            }
            else{
                t2[y2] = 0;
            }
        }
        for( int y3 = 0;y3<=69;y3++){
            if( y3 >= arrival[2] && y3 < departure[2]){
                t3[y3] = 1;

            }
            else{
                t3[y3] = 0;
            }
        }
        for( int y4 = 0;y4<=69;y4++){
            if( y4 >= arrival[3] && y4 < departure[3]){
                t4[y4] = 1;

            }
            else{
                t4[y4] = 0;
            }
        }
        for( int y5 = 0;y5<=69;y5++){
            if( y5 >= arrival[4] && y5 < departure[4]){
                t5[y5] = 1;

            }
            else{
                t5[y5] = 0;
            }
        }   
        int tra = 0;
        int mosttra =0;
        for(int z = 0;z <= 69;z++){
            tra = t1[z] + t2[z] + t3[z] + t4[z] + t5[z];
            if(tra > mosttra){
                mosttra = tra;
            }
        }
        plat = mosttra;

        
        
        return plat;

        
    } 

    
}





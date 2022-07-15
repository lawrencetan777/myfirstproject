package javaapps;

// create 2d grids
// given n and m as the dimension of the n x m grid, it returns
// 2d array with 1 around the edges, and 0 everywhere else
// eg.  3 x 4
// [ [ 1 1 1 ],
//   [1 0 1],
//   [1 0 1],
//   [1 1 1] ],

class app8{
    
    public static void main(String[] args) {
        int[][] s = a(2,3);
        
        int rows = s.length;
        int cols = s[0].length;
        for(int y2 = 0;y2 < rows;y2++){
            String a = "";    
            for(int x2 = 0; x2 < cols;x2++){
                a = a + s[y2][x2];
            }
            System.out.println(a);
        }
    }
    public static int[][] a(int n,int m){
        int[][] imarr = new int[n][m]; // create 2d array
        /*
            imarr = [ [ a1,a2,...,an ],  // n=0
                      [] ]     // n = rows
        */

        int x = 0;
        int y = 0;
        while( y < n){
            // fill sides of rows   
            imarr[y][0] = 1;    // for all rows in y = {0..n}, populate 1st row, and col y with 1
            imarr[y][m-1] = 1;

            if(y == 0 || y ==n-1){
                for(x = 0;x < m;x++){
                    imarr[y][x] = 1;
                }    
            }
            
            y++;
        }
        return imarr;
    } 


}
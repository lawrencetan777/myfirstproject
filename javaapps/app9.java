package javaapps;

// create 2d grids
// given n and m as the dimension of the n x m grid, it returns
// 2d array with increasing numbers downwards and rightwards.
// eg.  3 x 4
// [ [0 4 8],
//   [1 5 9],
//   [2 6 10],
//   [3 7 11] ],
public class app9 {
    public static void main(String[] args) {
        int[][] s = b(5,4);
        
        int rows = s.length;
        int cols = s[0].length;
        for(int y2 = 0;y2 < rows;y2++){
            String a = "";    
            for(int x2 = 0; x2 < cols;x2++){
                a = a + " " +  s[y2][x2];
            }
            System.out.println(a);
        }
    }
    public static int[][] b(int m,int n){
        int[][] newarr = new int[n][m];
        int x = 0;
        int y= 0;
        for(;y <n;y++){
            newarr[y][x] = y;
            for(;x<m;x++){
               newarr[y][x] = y + n*x; 
            }
            x = 0;
        }
        
        return newarr;

    }
    
}

import java.util.*;

class app4{
    public static void main(String[] args) {
        int[] arr = new int[] {0,1,7,23,45,60,61,67};
        int[] dep = new int[] {99,5,25,29,65,69,80,77};
        
        System.out.println(calcTrainPlat(arr,dep));
    }
    static int calcTrainPlat(int[] arr, int[] dep){
        Arrays.sort(arr);  //                  [0,5,6,7,10]
        Arrays.sort(dep);  // [3,10,7,9,12] => [3,7,9,10,12]

        // time             0   3  5  6  7    9  10   12 
        // num trains in  [ +1 -1 +1 +1  +1-1 -1 +1-1 -1]

        int maxP = 0;
        int platforms = 0;

        int arrIndex = 0;
        int depIndex = 0;

        while (arrIndex<arr.length && depIndex<dep.length) {
            if (arr[arrIndex] < dep[depIndex]) {
                platforms++;
                maxP = Math.max(platforms, maxP);
                arrIndex++;
            } else {
                platforms--;
                depIndex++;
            }
        }

        return maxP;
    } 

    
}





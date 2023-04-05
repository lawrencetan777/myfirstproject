

import java.util.*;

public class app5 {
    public static void main(String[] args){
        app5 app = new app5();

        List<Integer> powers = Arrays.asList(
            1,
            3,
            4
            );

        System.out.println("Answer " + app.calcServer(powers));

    }

    static final int MAX = 1000000007;
    
    public int calcServer(List<Integer> powers) {

        long[] sums = new long[powers.size()];
        sums[0] = powers.get(0);
        for (int i=1;i<powers.size();i++) {
            sums[i] = sums[i-1] + powers.get(i);
        }

        long result = 0;
        for(int i=0;i<powers.size();i++){
            result += calc(powers, i, i, sums, Integer.MAX_VALUE);
            result %= MAX;
        }

        return (int)result;
    }

    public int calc(List<Integer> powers, int i, int j, long[] sums, int prevMin) {
        int min = Math.min(prevMin, powers.get(j));
        long sum = getSum(sums, i, j);
        long result = min * sum;
        System.out.println("("+i+","+j+") = "+ result);

        if (j<powers.size()-1) {
            result += calc(powers, i, j+1, sums, min);
        }

        result = result % MAX;
        return (int)result;
    }

    public long getSum(long[] sums, int i, int j){
        if (i==0) {
            return sums[j];
        }
        return sums[j] - sums[i-1];
    }

}

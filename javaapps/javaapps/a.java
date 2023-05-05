package javaapps;

import java.lang.Math;

/**
 * 
 */
class a {
    
    public static void main(String[] args) {
        


    }

    static int findDistance(Graph a){
        int d = 0;
        return d; 
    }
    

    // generate a random graph with n nodes and p. For any pair of vertices, p is the probabily that an edge exists.
    static Graph generateRandom(int n, double p) {
        
        Graph a = new Graph();
        for(int z = 0; z < n; z++){
            for(int x = 0; x < n; x++){
                double r = Math.random();
                if(r <= p){
                    a.edges[z][x] = true;
                }else{
                    a.edges[z][x] = false;
                }
            }
        }
        for(int z = 0; z < n; z++){
            for(int x = 0; x < n; x++){
                while(a.distance[z][x] == 0){
                    int dist = 0;
                    if(a.edges[z][x] == true){
                        a.distance[z][x] = dist;
                    }

                }
            }

            
        }

        return a;
    }


    // print content of the graph
    static void print(Graph graph){

    }

    static class Graph {
        boolean[][] edges; // edges[i][j] = true if edge exists between i and j
        int[][] distance; //distance[1][2] = distance between node 1 and node 2
    }

}

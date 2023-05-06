package javaapps;

import java.lang.Math;
import java.util.ArrayList;


/**
 * 
 */
class a {
    
    public static void main(String[] args) {
        Graph test = generateRandom(5, .2);
        print(test);

    }

    
    

    // generate a random graph with n nodes and p. For any pair of vertices, p is the probabily that an edge exists.
    static Graph generateRandom(int n, double p) {
        
        Graph a = new Graph();
        a.maxPoint = n;
        for(int z = 0; z < n; z++){
            for(int x = 0; x < n; x++){
                double r = Math.random();
                if(r <= p){
                    a.edges[z][x] = true;
                    a.edges[x][z] = true;
                    int ar = (int) Math.random()*51;
                    a.distance[z][x] = ar;
                    a.distance[x][z] = ar;
                }else if( a.edges[z][x] != true){
                    a.edges[z][x] = false;
                }
            }
        }
        

        return a;
    }


    // print content of the graph
    static void print(Graph graph){
        ArrayList<Integer[]> edgeRecord = new ArrayList<>(1);
        Integer[] points = new Integer[2];
        for(int a = 0; a < graph.maxPoint;a++ ){
            for(int x = 0; x < graph.maxPoint;x++ ){
                points[0] = a;
                points[1] = x;
                if( graph.edges[a][x] == true && edgeRecord.contains(points) == false){
 
                    System.out.println("Length " + graph.distance[a][x] + " edge between nodes " + a + " and " + x );
                }
                
            }
        }
    }

    static class Graph {
        boolean[][] edges; // edges[i][j] = true if edge exists between i and j
        int[][] distance; //distance[1][2] = distance between node 1 and node 2
        int maxPoint; // max points. E.g. 5 means there are index from 0 - 4
    }

}

package javaapps;

import java.lang.Math;
import java.util.ArrayList; // List that's implemented from an array
import java.util.LinkedList; // List that's implemented from a linked list
import java.util.Set; // interface
import java.util.Stack;
import java.util.HashSet; // an implementation of the Set interface, driven by "Hash"
import java.util.LinkedHashSet; // another implement of the Set interface, driven by "hash" but also maintain order of insertion ("linked")
import java.util.List; // interface of a "list"

/**
 * 
 */
class a {
    
    public static void main(String[] args) {
        Graph test = generateRandom(50, .03);
        print(test);
        int islands = islands(test);
        System.out.println(islands);
        

    }
    static ArrayList<Integer> neighbors(Graph g, int i){
        ArrayList<Integer> neighbors = new ArrayList<>();
        for( int x = 0; x < g.maxPoint; x++){
            if(g.edges[i][x] == true){
                neighbors.add(x);
            }
        }
        return neighbors;
        
    }
    static Set<Integer> DFS(Graph g, int i){
        ArrayList<Integer> neighbors = new ArrayList<>();
        Set<Integer> visitedSet = new HashSet<Integer>();
        Stack<Integer> stack = new Stack<Integer>();

        stack.push(i);
        int v;
        while(stack.isEmpty() == false){
            v = stack.pop();
            visitedSet.add(v);
            neighbors = neighbors(g,v);
            for(int n = 0; n < neighbors.size(); n++){
                if(visitedSet.contains(neighbors.get(n)) == false){
                    stack.push(neighbors.get(n));
                }
            }
        }
        return visitedSet;
    }
    static int islands(Graph a){
        int islands = 0;

        Set<Integer> unvisited = new HashSet<>(); // Can check existence in O(1), can add or remove O(1)
        for(int i = 0; i < a.maxPoint; i++){
            unvisited.add(i);
        }



        for( int i = 0; i < a.maxPoint; i++){
            if (unvisited.contains(i)) {
                Set<Integer> visited = DFS(a,i);
                islands++;
                unvisited.removeAll(visited);
                
            }
        }
        return islands;
    }
    
    

    // generate a random graph with n nodes and p. For any pair of vertices, p is the probabily that an edge exists.
    static Graph generateRandom(int n, double p) {
        
        Graph a = new Graph();
        a.edges = new boolean[n][n];
        a.distance = new int[n][n];
        a.maxPoint = n;

        // 1 3 4 6 7
        // try to find all pairs that are unique
        // 13 14 16 17
        // 34 36 37
        // 46 47
        // 67

        

        for(int z = 0; z < n - 1; z++){
            for(int x = z + 1; x < n; x++){
                double r = Math.random();
                if(r <= p && z != x){
                    a.edges[z][x] = true;
                    a.edges[x][z] = true;
                    int ar = (int) (Math.random()*50);
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
        Integer[] points = new Integer[2];
        int edges=0;
        for(int a = 0; a < graph.maxPoint-1;a++ ){
            for(int x = a + 1; x < graph.maxPoint;x++ ){
                points[0] = a;
                points[1] = x;
                if( graph.edges[a][x] == true){ 
                    System.out.println("Length " + graph.distance[a][x] + " edge between nodes " + a + " and " + x );
                    edges++;
                }
            }
        }
        System.out.println("Points=" + graph.maxPoint + " edges="+edges);

    }

    static class Graph {
        boolean[][] edges; // edges[i][j] = true if edge exists between i and j
        int[][] distance; //distance[1][2] = distance between node 1 and node 2
        int maxPoint; // max points. E.g. 5 means there are index from 0 - 4
    }

}

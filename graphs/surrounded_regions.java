package graphs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

class surroundedJava {
    record Pair(int x, int y) {
    }

    public static List<Pair> getNeighbours(char[][] matrix, Pair coordinates) {
        List<Pair> neighbors = new ArrayList<>();

        int r = coordinates.x(); // Current row
        int c = coordinates.y(); // Current column

        int rows = matrix.length;
        int cols = matrix[0].length;

        // Direction arrays for Top, Bottom, Left, Right
        // (r-1, c) is Top
        // (r+1, c) is Bottom
        // (r, c-1) is Left
        // (r, c+1) is Right
        int[] dr = { -1, 1, 0, 0 };
        int[] dc = { 0, 0, -1, 1 };
        List<Integer> myList = List.of(-1, 1, 0, 0);

        // Loop through all 4 directions
        for (int i = 0; i < 4; i++) {
            int newRow = r + dr[i];
            int newCol = c + dc[i];

            // Boundary check: Ensure the new coordinate is inside the matrix
            if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
                neighbors.add(new Pair(newRow, newCol));
            }
        }

        return neighbors;
    }

    public static void dfsMarking(char[][] matrix, Pair startingPoint, boolean[][] visitedMatrix) {
        List<Pair> neigbours = getNeighbours(matrix, startingPoint);
        visitedMatrix[startingPoint.x()][startingPoint.y()] = true;
        for (Pair neighbour : neigbours) {
            if (matrix[neighbour.x()][neighbour.y()] == 'O')
                dfsMarking(matrix, neighbour, visitedMatrix);
        }
    }

    public static char[][] replaceSurroundedOswithXs(char[][] matrix) {
        // / Deep copy using streams
        char[][] deepCopy = Arrays.stream(matrix)
                .map(char[]::clone)
                .toArray(char[][]::new);
        boolean[][] visited = new boolean[matrix.length][matrix[0].length];
        List<Pair> boundaryElements = new ArrayList<>();
        for (int i = 0; i < matrix.length; i++) {
            if (matrix[i][0] == 'O') {
                boundaryElements.add(new Pair(i, 0));
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            if (matrix[i][matrix.length - 1] == 'O') {
                boundaryElements.add(new Pair(i, matrix.length - 1));
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            if (matrix[0][i] == 'O') {
                boundaryElements.add(new Pair(0, i));
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            if (matrix[matrix.length - 1][i] == 'O') {
                boundaryElements.add(new Pair(matrix.length - 1, i));
            }
        }
        for (Pair boundaryEle : boundaryElements) {
            dfsMarking(matrix, boundaryEle, visited);
        }
        for (int i = 0; i < visited.length; i++) {
            if (i != 0 && i != visited.length - 1) {
                for (int j = 0; j < visited[i].length; j++) {
                    if (j != 0 && j != visited[i].length - 1) {
                        if (!visited[i][j] && deepCopy[i][j] == 'O') {
                            deepCopy[i][j] = 'X';
                        }
                    }
                }
            }

        }
        return deepCopy;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("enter the lenth of the matrix");
        int n = scan.nextInt();
        System.out.println("enter the breadth of the matrix");
        int m = scan.nextInt();
        scan.nextLine();
        char[][] myMatrix = new char[n][m];
        System.out.println("Type your matrix row by row (space-separated):");
        for (int i = 0; i < n; i++) {
            // 1. Read the whole line (e.g., "X O X X")
            String line = scan.nextLine();

            // 2. Split it by spaces into an array of strings: ["X", "O", "X", "X"]
            String[] tokens = line.split(" ");

            for (int j = 0; j < m; j++) {
                // 3. Take the first character of each string token and store it
                myMatrix[i][j] = tokens[j].charAt(0);
            }
        }
        char[][] result = replaceSurroundedOswithXs(myMatrix);
        System.out.println("result matrix");
        Arrays.stream(result)
                .forEach(row -> {
                    // Now you can work with each row!
                    System.out.println(row);
                });
        scan.close();
    }
}
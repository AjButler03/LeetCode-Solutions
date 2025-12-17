public class Main {
    public static void main(String[] args) {

        System.out.println("Hello, World!\n");

//        Let's make a grid
        int width = 80;
        int height = 24;
        for (int i = 0; i < height; i++){
            for (int j = 0; j < width; j++){
                System.out.print("x");
            }
            System.out.println();
        }

        System.out.println("\nAll Done");
    }
}
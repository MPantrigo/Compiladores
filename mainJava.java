import java.util.Scanner;

public class MainClass{
    public static void main(String args[]){
        Scanner _key = new Scanner(System.in);
        a= _key.nextDouble();

        b= _key.nextDouble();

        c = 10;

        a = 1+2*3/b;

        if (c>b) {
            System.out.println(a);
            if (c>b) {
                System.out.println(b);
            }
        }

        while (b<c) {
            a = a+1;
            while (b<c) {
                b = b+1;
            }
        }

    }
}
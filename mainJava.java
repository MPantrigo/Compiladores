import java.util.Scanner;

public class MainClass{
    public static void main(String args[]){
        Scanner _key = new Scanner(System.in);
        a= _key.nextDouble();

        b= _key.nextDouble();

        c = 10;

        a = (1+2)*3/b;

        t1 = "Enquanto";

        t2 = t1;

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

        switch (a) {
            case 10:
                System.out.println(a);
                break;
            case 20:
                System.out.println("Eeee");
            case default :
                System.out.println("Deu certo");
        }
    }
}
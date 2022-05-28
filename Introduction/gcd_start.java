// run: javac gcd_start.java && java gcd_start
public class gcd_start {

    private static int gcd(int a, int b) {
        while(b != 0) {
            int temp = a;
            a = b;
            b = temp % b;
        }
        return a;
    }

    public static void main(String[] args) {
        System.out.print(gcd(60, 96));
        System.out.println();
        System.out.print(gcd(20, 8));
        System.out.println();
    }
}
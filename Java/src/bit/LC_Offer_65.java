package bit;

public class LC_Offer_65 {

    public int add(int a, int b) {
        int sum = a ^ b, carry = (a & b) << 1;
        int temp;
        while (carry != 0) {
            temp = sum;
            sum = sum ^ carry;
            carry = (temp & carry) << 1;
        }

        return sum;
    }

    public static void main(String[] args) {
        int a = 10, b = 15;
        LC_Offer_65 lc = new LC_Offer_65();
        System.out.println(lc.add(a, b));
    }

}

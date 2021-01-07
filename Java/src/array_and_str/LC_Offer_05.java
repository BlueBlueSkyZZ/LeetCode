package array_and_str;

public class LC_Offer_05 {
    public String replaceSpace(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                sb.append("%20");
            } else {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String s = "We are happy.";

        LC_Offer_05 solution = new LC_Offer_05();
        System.out.println(solution.replaceSpace(s));
    }
}

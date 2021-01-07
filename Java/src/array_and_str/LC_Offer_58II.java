package array_and_str;

public class LC_Offer_58II {

    public String reverseLeftWords(String s, int n) {
        StringBuilder sb = new StringBuilder(s);

        reverse(sb, 0, n-1);
        reverse(sb, n, sb.length()-1);
        reverse(sb, 0, sb.length()-1);

        return sb.toString();

    }

    private void reverse(StringBuilder sb, int start, int end) {
        while (start < end) {
            char temp = sb.charAt(start);
            sb.setCharAt(start, sb.charAt(end));
            sb.setCharAt(end, temp);
            start++;
            end--;
        }
    }

}

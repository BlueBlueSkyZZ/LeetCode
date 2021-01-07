package array_and_str;

public class LC_Offer_58I {

    public String reverseWords(String s) {
        s = s.trim();
        int i = s.length() - 1, j = s.length() - 1;
        StringBuilder result = new StringBuilder();

        while (i >= 0) {
            while (i >= 0 && s.charAt(i) != ' ') {
                i--;
            }
            result.append(s.substring(i+1, j+1));
            if (i+1 != 0) {
                result.append(' ');
            }
            while (i >= 0 && s.charAt(i) == ' ') {
                i--;
            }
            j = i;
        }
        return result.toString();
    }

}

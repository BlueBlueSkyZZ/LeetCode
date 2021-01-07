package hash;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

public class LC_Offer_50 {

    public char firstUniqChar(String s) {
        char res = ' ';
        LinkedHashMap<Character, Integer> hashMap = new LinkedHashMap<>();
        for (int i = 0; i < s.length(); i++) {

            if (!hashMap.containsKey(s.charAt(i))) {
                hashMap.put(s.charAt(i), 1);
            } else {
                hashMap.replace(s.charAt(i), hashMap.get(s.charAt(i))+1);
            }
        }

        for (Map.Entry<Character, Integer> entry: hashMap.entrySet()) {
            if (entry.getValue() == 1) {
                res = entry.getKey();
                break;
            }
        }
        return res;
    }

    public char firstUniqChar2(String s) {
        char res = ' ';
        int[] hashmap = new int[26];

        for (int i = 0; i < s.length(); i++) {
            hashmap[s.charAt(i)-'a'] += 1;
        }

        for (int i = 0; i < s.length(); i++) {
            if (hashmap[s.charAt(i)-'a'] == 1) {
                res = s.charAt(i);
                break;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        String s = "leetcode";
        LC_Offer_50 lc = new LC_Offer_50();
        System.out.println(lc.firstUniqChar2(s));
    }

}

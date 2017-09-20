import java.util.*;

public class LongestCommonPrefix {
    public static String longestCommonPrefix(String[] strs) {
        if (strs.length == 0)
            return "";

        // Find index of minimum length string
        int min = 0;
        for (int i = 1; i < strs.length; i++) {
            min = strs[min].length() < strs[i].length()  ? min : i;
        }

        int i = 0;
        int minLength = strs[min].length();
        while (i < minLength) {
            for (int j = 1; j < strs.length; j++) {
                if (strs[j].charAt(i) != strs[j-1].charAt(i)) {
                    return strs[0].substring(0, i);
                }
            }
            i++;
        }
        return strs[min];
    }
}

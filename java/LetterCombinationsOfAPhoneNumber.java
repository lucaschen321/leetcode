import java.util.*;

public class LetterCombinationsOfAPhoneNumber {

    static String[] keypad = { "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };

    public List<String> letterCombinations(String digits) {
        List<String> ans = new ArrayList<String>();
        if (digits.indexOf('0') != -1 || digits.indexOf('1') != -1 || digits.length() == 0) {
            return ans;
        }
        combinations("", digits, 0, ans);
        return ans;
    }

    public static void combinations (String prefix, String digits, int swap, List<String> list) {
        if (swap == digits.length()) {
            list.add(prefix);
            return;
        }

        int num = digits.charAt(swap) - '0';
        for (int i = 0; i < keypad[num].length(); i++) {
            combinations(prefix + keypad[num].charAt(i), digits, swap + 1, list);
        }
    }


    //  public static List<String> letterCombinations(String digits) {
    //         List<String> combinations = new ArrayList<String>();
    //         String[][] keypad = {{""}, {""}, {"a", "b", "c"}, {"d", "e", "f"}, {"g", "h", "i"}, {"j", "k","l"}, {"m", "n", "o"}, {"p", "q", "r", "s"}, {"t", "u", "v"}, {"w", "x", "y", "z"} };
    //
    //         if (digits.indexOf('0') != -1 || digits.indexOf('1') != -1 || digits.length() == 0) {
    //             return combinations;
    //         }
    //
    //         int num = digits.charAt(0) - '0';
    //         if (digits.length() == 1) {
    //             return Arrays.asList(keypad[num]);
    //         }
    //         for (int j = 0; j < keypad[num].length; j++) {
    //             List<String> result = letterCombinations(digits.substring(1));
    //             // for (String s : result) {
    //             //     s = keypad[num][j] + s;
    //             // }
    //             for (int k = 0; k < result.size(); k++) {
    //                 result.set(k, keypad[num][j] + result.get(k));
    //             }
    //             combinations.addAll(result);
    //         }
    //         return combinations;
    //     }



    // public static void main(String[] args) {
    //     String digits = "89";
    //     List<String> ans = letterCombinations(digits);
    //     System.out.print("[");
    //     for (String s: ans)
    //         System.out.print(s + ", ");
    //     System.out.print("]");
    // }
}


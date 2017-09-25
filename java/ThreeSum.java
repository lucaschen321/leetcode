import java.util.*;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if (nums == null || nums.length < 2)
            return ans;

        Arrays.sort(nums);
        int l, r, target, sum;
        for (int i = 0; i < nums.length - 2; i++) {
            if (i == 0 || (i > 0 && nums[i] != nums[i-1])) {
                l = i + 1;
                r = nums.length -1;
                while (l < r) {
                    target = 0 - nums[i];
                    sum = nums[l] + nums[r];
                    if (sum < target) {
                        l++;
                    } else if (sum > target) {
                        r--;
                    }
                    else {
                        ans.add(Arrays.asList(nums[i], nums[l], nums[r]));
                        l++;
                        r--;
                        while (nums[l] == nums[l - 1] && l < r) {
                            l++;
                        }
                        while (nums[r] == nums[r + 1] && l < r) {
                            r--;
                        }

                    }
                }
            }
        }
        return ans;
    }
}

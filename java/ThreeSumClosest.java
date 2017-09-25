import java.util.*;

public class ThreeSumClosest {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closest = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < nums.length - 2; i++) {
            int l = i + 1, r = nums.length - 1;
            while (l < r) {
                int sum = nums[l] + nums[r] + nums[i];
                if (Math.abs(target-sum)
                    < Math.abs(target - closest)) {
                    closest = sum;
                }
                if (sum < target ) {
                    l++;
                } else if (sum > target) {
                    r--;
                } else {
                    return closest;
                }
            }
        }
        return closest;
    }
}

#include <vector>

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        // int ind = 0;
        // for (auto it = nums.begin(); it < nums.end(); ) {
        if (target <= nums[0]) {
            return 0;
        }

        for (int i = 0; i < nums.size()-1; i++) {
            if (nums[i] == target) {
                return i;
            }
            if (nums[i] < target and target <= nums[i+1]) {
                return i+1;
            }
        }
        return nums.size();
    }
};
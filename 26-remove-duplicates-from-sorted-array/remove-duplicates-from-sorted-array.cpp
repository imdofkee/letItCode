class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        set<int> unique_nums;
        for (auto it = nums.begin(); it != nums.end();) {
            if (unique_nums.count(*it)) {
                it = nums.erase(it);

            }
            else {
                unique_nums.insert(*it);
                ++it;
            }
        }
        return nums.size();
    }
};


class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        int n = nums.size();
        
        // 1. Возводим в квадрат и сортируем
        for (int& x : nums) {
            x = x * x;
        }
        sort(nums.begin(), nums.end());
        
        // 2. Считаем сумму: сумма правой (большей) половины минус сумма левой (меньшей) половины
        long long positiveSum = accumulate(nums.begin() + n/2, nums.end(), 0LL);
        long long negativeSum = accumulate(nums.begin(), nums.begin() + n/2, 0LL);
        
        return positiveSum - negativeSum;
    }
};
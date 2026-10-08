class Solution {
public:
    int DijitSquare(int n) {
        int square = 0;
        int summ = 0;
        while (n > 0) {
            int d = n%10;
            square += d*d;
            n /= 10;
        }
        return square;
    }
    bool isHappy(int n) {
        int slow = n;
        int fast = DijitSquare(n);
        while (fast != 1 && fast != slow) {
            slow = DijitSquare(slow);
            fast = DijitSquare(DijitSquare(fast));
        }
        return fast == 1;
    }
};
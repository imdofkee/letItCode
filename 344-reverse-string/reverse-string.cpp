#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        s = {s.rbegin(), s.rend()};
    }
};
#include <iostream>
using namespace std;

class Solution {
public:
    int reverse(int x) {

    	int rev = 0;

    	while (x != 0) {
    		int remainer = x % 10;
    		// cout << remainer;
    		x = x / 10;

    		if ((rev > INT_MAX / 10) || (rev == INT_MAX / 10 && remainer > 7))
    			return 0;
    		if ((rev < INT_MIN / 10) || (rev == INT_MIN / 10 && remainer < -8))
    			return 0;
    		rev = rev * 10 + remainer;

    	}
    	return rev;
    }
};

int main(int argc, char const *argv[])
{
	Solution* solution = new Solution();
	cout << solution->reverse(-123);
	return 0;
}
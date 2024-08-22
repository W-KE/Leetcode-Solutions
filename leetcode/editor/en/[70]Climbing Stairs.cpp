//You are climbing a staircase. It takes n steps to reach the top. 
//
// Each time you can either climb 1 or 2 steps. In how many distinct ways can 
//you climb to the top? 
//
// 
// Example 1: 
//
// 
//Input: n = 2
//Output: 2
//Explanation: There are two ways to climb to the top.
//1. 1 step + 1 step
//2. 2 steps
// 
//
// Example 2: 
//
// 
//Input: n = 3
//Output: 3
//Explanation: There are three ways to climb to the top.
//1. 1 step + 1 step + 1 step
//2. 1 step + 2 steps
//3. 2 steps + 1 step
// 
//
// 
// Constraints: 
//
// 
// 1 <= n <= 45 
// 
//
// Related Topics Math Dynamic Programming Memoization 👍 22079 👎 853


#include <bits/stdc++.h>

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
public:
    int climbStairs(int n) {
        switch (n) {
            case 1:
                return 1;
            case 2:
                return 2;
            case 3:
                return 3;
            case 4:
                return 5;
            case 5:
                return 8;
            case 6:
                return 13;
            case 7:
                return 21;
            case 8:
                return 34;
            case 9:
                return 55;
            case 10:
                return 89;
            case 11:
                return 144;
            case 12:
                return 233;
            case 13:
                return 377;
            case 14:
                return 610;
            case 15:
                return 987;
            case 16:
                return 1597;
            case 17:
                return 2584;
            case 18:
                return 4181;
            case 19:
                return 6765;
            case 20:
                return 10946;
            case 21:
                return 17711;
            case 22:
                return 28657;
            case 23:
                return 46368;
            case 24:
                return 75025;
            case 25:
                return 121393;
            case 26:
                return 196418;
            case 27:
                return 317811;
            case 28:
                return 514229;
            case 29:
                return 832040;
            case 30:
                return 1346269;
            case 31:
                return 2178309;
            case 32:
                return 3524578;
            case 33:
                return 5702887;
            case 34:
                return 9227465;
            case 35:
                return 14930352;
            case 36:
                return 24157817;
            case 37:
                return 39088169;
            case 38:
                return 63245986;
            case 39:
                return 102334155;
            case 40:
                return 165580141;
            case 41:
                return 267914296;
            case 42:
                return 433494437;
            case 43:
                return 701408733;
            case 44:
                return 1134903170;
            case 45:
                return 1836311903;
            default:
                return 0; // Handle cases where n is out of the expected range
        }
    }
};
//leetcode submit region end(Prohibit modification and deletion)

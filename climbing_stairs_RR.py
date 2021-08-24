
Skip to content
Pull requests
Issues
Marketplace
Explore
@rohit8pix
P-Raj27 /
GEEK-FOR-GEEK-QUESTIONS

2
1

    0

Code
Issues
Pull requests
Actions
Projects
Wiki
Security

    Insights

GEEK-FOR-GEEK-QUESTIONS/climbing_stairs_RR.py /
@rohit8pix
rohit8pix Create climbing_stairs_RR.py
Latest commit eaee6ff 19 seconds ago
History
1 contributor
38 lines (31 sloc) 1.13 KB
# The best solution for this is using Dynamic Programming (Bottom up or Top Down)
# since , I am in the noob stage i implemented it but the time taken is more, but solution is accepted
# have to learn memoization 

########## My SOLUTION #########################   28 ms Runtime / memory 

class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n==2:
                return 2

            table = [None] * (n+1) 
            table[0] = 0        # base case 1, fib(0) = 0
            table[1] = 1
            table[2] = 2      # base case 2, fib(1) = 1
            # filling up tabulation table starting from 2 and going upto n
            for i in range(3,n+1):  
                table[i] = table[i-1] + table[i-2]
            return table[n]  
        ans = climb(n)
        return ans




############## faster solution ##################
class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 0, 1
        while n:
            curr, prev = curr + prev, curr
            n -= 1
        return curr

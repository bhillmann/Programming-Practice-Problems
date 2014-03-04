Marble Game
=============================
Input: Standard Input 
Output: Standard Output 
 
You and your friend are playing a game. The game field contains n boxes arranged in a circle. The boxes are numbered from 0 to n-1. The ith box has 2 adjacent boxes. Box (i+1) mod n is its neighbor in the clockwise direction while box (i-1+n) mod n is its neighbor in the counter-clockwise direction. In each move you and your friend each select a marble. You move your selected marble clockwise, while your friend moves her selected marble counter-clockwise. You both move at the same time. The goal of the game is to move all the marbles to a single cell. A cell is a valid destination if it is possible to move all the marbles to that cell by following the rules of the game. Also, for each valid destination there is a minimum number of moves you can take to move all the marbles to that destination. Your task is to calculate the sum of all these minimum number of moves. 
 
Input 
The first line of the input contains T(1≤T≤120), the number of test cases. Each test case contains 2 lines.  The first line of a test case contains n(1≤n≤50000), the number of boxes. The second line of a test case contains n non-negative integers. The ith integer denotes the number of marbles in box i. Each box can have at most 10000 marble initially. For each test case the total number of marbles is positive. 
 
Output 
For each test case the output should print 2 integers separated by a single space. The first integer is the number of valid destination cells and the second integer is sum of minimum number of moves to all these valid destinations. The input will be such that the second integer will fit in a 64 bit signed integer. 
 
Sample Input 

3<br>
3<br>
1 1 1<br>
4<br>
0 1 1 1<br>
4<br>
2 1 2 1<br>


Sample Output
 
3 3<br>
1 1<br>
2 6
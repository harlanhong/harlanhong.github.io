---
title: 'LeetCode'
date: 2012-08-14
permalink: /posts/2012/08/offerbook/
tags:
  - cool posts
  - plan
---

以下题目来自《剑指offer》or LeetCode

## 题目1：面试题59 - I. 滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
```
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

```

***Answer:*** 使用一个队列来存储当前最大值，从后面开始只记录非严格递增的数，窗口滑动时遇到队列第一个数，就去掉。
```py
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n==0 or n<k:
            return []
        queue = collections.deque([])
        for i in range(k):
            value = nums[i]
            while queue and queue[-1]<value:
                queue.pop()
            queue.append(value)
        res = []
        res.append(queue[0])
        for i in range(k,n):
            if queue[0] == nums[i-k]:
                queue.popleft()
            value = nums[i]
            while queue and queue[-1]<value:
                queue.pop()
            queue.append(value)
            res.append(queue[0])

        return res
```

## 题目2: 面试题64. 求1+2+…+n
要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
```py
输入: n = 3
输出: 6
```

***Answer:*** 利用bool操作的前判断性
```py
class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res
```

## 题目3：面试题38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
```py
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
```
***Answer:*** dfs+剪枝
```py
class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        if n < 2:
            return [s]
        self.res = []
        def helper(current,rest):
            if len(rest) == 0:
                if not current in self.res:
                    self.res.append(current)
            else:
                record = [] #记录是否已经被看过
                for i in range(len(rest)):
                    if rest[i] in record:
                        continue
                    helper(current+rest[i],rest[:i]+rest[(i+1):])
                    record.append(rest[i])
        helper('',s)
        return self.res
```

## 题目4：单词搜索 II
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
```py
输入: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
```

## 139. 单词拆分
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

```py
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
```
***Answer:*** 动态规划，判断dp[i] 表示s[0:i] 是否能拆分，则d[j] = d[k] && s[k,j] in dict
```py
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp=[False]*(n+1)
        dp[0] = True
        for i in range(n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]
```

## 剑指 Offer 67. 把字符串转换成整数
写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。



首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

```py
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
```

***Answer: ***
```py
class Solution:
    def strToInt(self, str: str) -> int:
        if len(str) == 0:
            return 0
        #delete the whitespace
        i = 0
        while i<len(str) and str[i] == " ":
            i+=1
        str = str[i:]
        if len(str) == 0:
            return 0
        #去掉第一个非空字符是字母
        if str[0]!='+' and str[0]!='-' and not (str[0]>='0' and str[0]<='9'):
            return 0
        #提取数字
        flag = 1
        i = 0
        if str[0] == '-':
            flag = -1
            i+=1
        elif str[0] == '+':
            flag = 1
            i+=1
        #去0
        while i<len(str) and str[i] == 0:
            i+=1
        num=''
        while i<len(str) and str[i]>='0' and str[i]<='9' :
            num+=str[i]
            i+=1
        print(num)
        if num=='':
            return 0
        if flag == -1:
            return max(pow(-2,31),int(flag*int(num)))
        else:
            return min(pow(2,31)-1,int(flag*int(num)))
```

## 剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

```py
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
```

***Answer: *** 动态规则， dp[k] = dp[k-1]+dp[k-2] if nums[k:k+2] in dict else dp[k-1]
```py
class Solution:
    def translateNum(self, num: int) -> int:
        strs = str(num)
        if len(strs) == 1:
            return 1
        a = 1
        b = 2 if '10'<=strs[:2] and strs[:2]<='25' else 1
        n = len(strs)
        for i in range(2,n):
            if '10'<=strs[i-1:i+1] and strs[i-1:i+1]<='25':
                k = a+b
            else:
                k = b
            a,b = b,k
        return b
```

## 剑指 Offer 44. 数字序列中某一位的数字
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。
```py
输入：n = 11
输出：0
```

***Answer: ***
```py
class Solution:
    def findNthDigit(self, n: int) -> int:
        #0-9 10
        #10-99  2*90 8*pow(10,k-1)+str('9'*k-1)
        #100-999 3*900
        #1000-9999 4*9000
        if n<10:
            return n
        else:
            n-=10
            k=1
            while n>=0:
                k+=1
                remain = n
                n = n-k*(9*pow(10,k-1))
            num = int(remain/k)+pow(10,k-1)
            return int(str(num)[remain%k])
```

## 剑指 Offer 34. 二叉树中和为某一值的路径
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
```py
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
Result
[
   [5,4,11,2],
   [5,8,4,5]
]
```
***Answer: *** dfs
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        self.res = []
        def dfs(node,_sum,res):
            if not node:
                return
            if not node.left and not node.right:
                if _sum+node.val == sum:
                    self.res.append(res+[node.val])
                    return
            else:
                dfs(node.left,_sum+node.val,res+[node.val])
                dfs(node.right,_sum+node.val,res+[node.val])
        dfs(root,0,[])
        return self.res
```

## 剑指 Offer 33. 二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
```py
     5
    / \
   2   6
  / \
 1   3
输入: [1,6,3,2,5]
输出: false
输入: [1,3,2,6,5]
输出: true
```

***Answer: *** 后序遍历的特点是[左子树，右子树，根]，其中根大于左子树，根小于右子根
```py
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        #最后一个元素是root
        def recur(i,j):
            if i>=j:
                print(i,j,postorder[i:j+1])
                return True
            p = i
            while postorder[p]<postorder[j]: p+=1
            m = p
            while postorder[p]>postorder[j]:p+=1
            return p==j and recur(i,m-1) and recur(m,p-1)
        flag = recur(0,len(postorder)-1)
        return flag
```
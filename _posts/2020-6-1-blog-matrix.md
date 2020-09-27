---
title: '算法刷题：矩阵系列'
date: 2020-6-01
permalink: /posts/2020/06/matrix/
tags:
  - matrix
  - algorithm
---

以下题目均来自LeetCode。


## 题目1： 01 矩阵
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。

```py
输入:
0 0 0
0 1 0
0 0 0
输出:
0 0 0
0 1 0
0 0 0
```
***Answer:***
思路：采用宽度优先搜索：
```py
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        if n==0:
            return []
        m = len(matrix[0])
        if m==0:
            return [[] for _ in range(n)]
        res = [[m+n]*m for i in range(n)]
        queue = collections.deque([])
        flag = [[-1]*m for i in range(n)]
        moves = [[-1,0],[1,0],[0,1],[0,-1]]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    queue.append([i,j,0])
                    flag[i][j]=1
                    res[i][j] = 0
        iterator = 0
        while len(queue)>0:
            iterator+=1
            k  = len(queue)
            for i in range(k):
                x,y,value = queue.popleft()
                for mv in moves:
                    if x+mv[0]>=0 and x+mv[0]<n and y+mv[1]>=0 and y+mv[1]<m and flag[x+mv[0]][y+mv[1]] == -1:
                        res[x+mv[0]][y+mv[1]] = value+1
                        queue.append([x+mv[0],y+mv[1],res[x+mv[0]][y+mv[1]]])
                        flag[x+mv[0]][y+mv[1]]=1
        return res
```

## 题目2：排序矩阵查找
给定M×N矩阵，每一行、每一列都按升序排列，请编写代码找出某元素。

```py
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
```

***Answer:***
思路：类似二分法：
```py
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        n = len(matrix)
        if n==0:
            return False
        m = len(matrix[0])
        if m==0:
            return False
        row = 0
        columns = m-1
        while columns!=-1 and row!=n:
            if matrix[row][columns]>target:
                columns-=1
            elif matrix[row][columns]<target:
                row+=1
            else:
                return True
        return False
```

## 题目3：矩阵区域和
给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 
-   i - K <= r <= i + K, j - K <= c <= j + K 
(r, c) 在矩阵内。
```py
输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]
```

***Answer:***
思路：可以预先计算出一个和矩阵，可以在快速查找
```py
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        p = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                p[i][j] = p[i-1][j]+p[i][j-1]-p[i-1][j-1]+mat[i-1][j-1]
        res = [[0]*m for _ in range(n)]
        def get(x,y):
            x = max(min(x,n),0)
            y = max(min(y,m),0)
            return p[x][y]
        for i in range(n):
            for j in range(m):
                res[i][j] =get(i+K+1,j+K+1)-get(i-K,j+K+1)-get(i+K+1,j-K)+get(i-K,j-K)
        return res 

```

## 题目4：螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
```py
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
```
***Answer:***
思路：考虑好转变方向的时候怎么处理就好
```py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n==0:
            return []
        m = len(matrix[0])
        flag = [[0]*m for _ in range(n)]
        count = n*m
        res = []
        x = 0
        y = 0
        directs = {0:[0,1],1:[1,0],2:[0,-1],3:[-1,0]}
        d = 0
        while count>0:
            res.append(matrix[x][y])
            count-=1
            flag[x][y] = 1
            [dx,dy] = directs[d]
            if x+dx>=0 and x+dx<n and y+dy>=0 and y+dy<m and flag[x+dx][y+dy] == 0:
                x+=dx
                y+=dy
            else:
                d=(d+1)%4
                [dx,dy] = directs[d]
                x+=dx
                y+=dy
        return res
```

## 题目5：零矩阵
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
```py
输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

***Answer:***记录下要消除的行和列就可以，为了防止重复，可以用字典来记录
```py
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row,column = {},{}
        n = len(matrix)
        if n==0:
            return
        m = len(matrix[0])
        if m==0:
            return 
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i]=1
                    column[j]=1
        rows = list(row.keys())
        columns = list(column.keys())
        for i in rows:
            for k in range(m):
                matrix[i][k]=0
        for i in columns:
            for k in range(n):
                matrix[k][i]=0
        return 
```

## 题目6：重塑矩阵
在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
```py
输入: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
输出: 
[[1,2,3,4]]
解释:
行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
```

***Answer:***按顺序填充，类似C++的指针
```py
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(nums)
        if n==0:
            return []
        m = len(nums[0])
        if n*m!=r*c:
            return nums
        res = [[0]*c for _ in range(r)]
        p=0
        for i in range(r):
            for j in range(c):
                res[i][j]=nums[int(p/m)][p%m]
                p+=1
        return res
```

## 题目7：单词矩阵
给定一份单词的清单，设计一个算法，创建由字母组成的面积最大的矩形，其中每一行组成一个单词(自左向右)，每一列也组成一个单词(自上而下)。不要求这些单词在清单里连续出现，但要求所有行等长，所有列等高。
如果有多个面积最大的矩形，输出任意一个均可。一个单词可以重复使用。
```py
输入: ["this", "real", "hard", "trh", "hea", "iar", "sld"]
输出:
[
   "this",
   "real",
   "hard"
]
```
***Answer:***此题超过100行代码，在面试时基本不会写这么长的代码，答案可以查看[这里](https://leetcode-cn.com/problems/word-rectangle-lcci/solution/trieshu-dfshui-su-by-kobe24o/)
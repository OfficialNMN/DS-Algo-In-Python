# check if it can be partitioned into two parts such that the sum of 
# elements in both parts is the same. 

# to approach this problem we will use SubsetSum problem so that difference of 2
# subarrays will be 0.

def equalPartition( N, arr):
   s=sum(arr)
   # if sum is even then only partition is possible
   if s%2==0:
      # calling for half the sum of total array since only then equal partition will occur
      return subset(N,arr,s//2)
   else:
      return 0

def subset(N,arr,sum):
   dp=[[0 for i in range(sum+1)] for _ in range(N+1)]
   # first row is 0 bcoz sum !> 0 when subset is empty
   for i in range(sum+1):
      dp[0][i]=0
   # first col is 1 bcoz empty subset gives sum=0
   for i in range(N+1):
      dp[i][0]=1
   for i in range(1,N+1):
      for j in range(1,sum+1):
          # case when arr element will be included 
         if arr[i-1]<=j:
            dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
          # when element will be skipped
         else:
            dp[i][j]=dp[i-1][j]
   
   return dp[N][sum]

print(equalPartition(4,[1,5,11,5]))
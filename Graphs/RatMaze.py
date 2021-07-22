def findPath(m, n):
    visited=[[False for _ in range(n)] for i in range(n)]
    ans=[]
    validpath(m,0,0,ans,'',visited)
    return ans

def validpath(m,row,col,ans,path,visited):
    if (row<0 or col<0 or row==len(m) or col==len(m[0]) or m[row][col]==0 or visited[row][col]==True):
        return 
    if (row==(len(m)-1) and col==(len(m[0])-1)):
        ans.append(path)
    visited[row][col]=True
    validpath(m,row+1,col,ans,path+'D',visited)
    validpath(m,row,col-1,ans,path+'L',visited)
    validpath(m,row,col+1,ans,path+'R',visited)
    validpath(m,row-1,col,ans,path+'U',visited)
    visited[row][col]=False
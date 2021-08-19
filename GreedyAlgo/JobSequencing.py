def JobScheduling(Jobs,n):
    # sorting according to profit
    Jobs=sorted(Jobs,key=lambda job :job.profit,reverse=True)
    slots=[0]*(n+1)
    profit=0
    count=0
    # traverse through all jobs
    for i in range(n):
        # will start traversing back from deadline till 1st slot
        j=min(n,Jobs[i].deadline)-1
        while j>=0:
            # when slot is available
            if slots[j]==0:
                slots[j]=Jobs[i].id
                profit+=Jobs[i].profit
                count+=1
                break
            else:
                # if slot is not available
                j=j-1
    return [count,profit]

print(JobScheduling([],4))
def minimumPlatform(n,arr,dep):
    arr.sort()
    dep.sort()
    platform=1
    result=1
    i=1
    j=0
    while(i<n and j<n):
        # if next train is arriving before departure of prev
        if arr[i]<=dep[j]:
            platform+=1
            # move to next arriving train
            i+=1
        else:
            # if prev train has departed before next arrival
            platform-=1
            # move to next departure
            j+=1
        # check and update result whenever platforms is required
        if platform>result:
            result=platform
    return result
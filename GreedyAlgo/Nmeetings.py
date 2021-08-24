def maximumMeetings(n,start,end):
    # zipping both start and end time of a meet together
    meet=zip(end,start)
    # sorting the meets on basis of ending time
    meet=sorted(meet)
    # end time of previous meet is set as -1
    prev=-1
    count=0
    # traversing through the meets
    for i in range(n):
        # if start time of a meet > end time of previous meet 
        if meet[i][1]>prev:
            count+=1
            # previous meet end time will be updated
            prev=meet[i][0]
    return count
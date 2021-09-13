def reverseWords(s):
    # traversing form back
    i=len(s)-1
    # answer string
    ans=""
    while(i>=0):
        # if space is encountered decreas i
        while(i>=0 and s[i]==' '):
            i-=1
        # initialise j = i to keep track of space
        j=i
        # for space at starting of string then ignore
        if i<0:
            break
        # if letter is encountered decrease i
        while(i>=0 and s[i]!=' '):
            i-=1
        # when ans is empty add the last word
        if len(ans)==0:
            ans += s[i+1:j+1]
        # when string is not empty
        # add next word with a space in between
        else:
            ans = " ".join([ans,s[i+1:j+1]])
    return ans
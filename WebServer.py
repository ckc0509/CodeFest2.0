with open("TWSP_large.txt","r") as ip, open("TWSP_largeOutput.txt","w") as op:
    N = int(ip.readline())
    lst = []
    for _ in range(N):
        lst.append(list(map(int,(filter(None,ip.readline().replace('\n','').split(" "))))))
    
    lst.sort(key = lambda x:(x[0],-x[1]))
    for ele in lst:
        ele = map(str,ele)
        s = ','.join(ele)
        op.write(s+'\n')
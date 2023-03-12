with open("ET_large.txt","r") as ip, open("ET_largeOutput.txt","w") as op:
    T = int(ip.readline())
    case = 1
    for _ in range(T):
        N = int(ip.readline())
        totalAccent = 0.0
        totalNormal = 0.0
        totalHours = 0.0
        for _ in range(N):
            B,R,S,H = map(int,ip.readline().split(','))
            totalAccent += (R*1.5) + (S*(4/3)*1.5) + (H*3)
            totalNormal += (R*4.5) + (S*((8/3)*2.25)) + (H*9)
            totalHours += (R*2.5) + (R*6.5) + (S*(4/3)*2.5) + (S*(8/3)*3.25) + (H*5) + (H*13)
        totalAccent = round(totalAccent,2)
        totalHours = round(totalHours,2)
        totalNormal = round(totalNormal,2)
        output = "Case #" + str(case) + ": {:0.2f}".format(totalHours) + ", {:0.2f}".format(totalAccent) + ", {:0.2f}".format(totalNormal) + "\n"
        case += 1
        op.write(output)
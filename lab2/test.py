capacity = 8
f, fault, pf = [], 0, 'No'
seq = list(range(8))
#s = list(map(int, input().strip().split()))
s = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,0,0,4,255,4,5,5,0,255,1,255,1,1,1,2,3,0,255,1,254,1,1,1,2,3,0,254,1,254,1,1,1,2,3,0,254,1,253,1,1,1,2,3,0,253,1,253,1,1,1,2,3,0,253,1,252,1,1,1,2,3,0,252,1,252,1,1,1,2,3,0,252,1,251,1,1,1,2,3,0,251,1,251,1,1,1,2,3,0,251,1,250,1,1,1,2,3,0,250,1,250,1,1,1,2,3,0,250,1,249,1,1,1,2,2,2,3,250,3,3,250,4,4,3,250,3,3,251,4,4,3,251,3,3,251,4,4,3,251,3,3,252,4,4,3,252,3,3,252,4,4,3,252,3,3,253,4,4,3,253,3,3,253,4,4,3,253,3,3,254,4,4,3,254,3,3,254,4,4,3,254,3,3,255,4,4,3,255,3,3,255,4,4,5,255,5,6,0,6]
print(s)
print("\nString|Frame →\t", end='')
for i in range(capacity):
    print(i, end=' ')
print("Fault\n   ↓\n")
occurance = [None for i in range(capacity)]
for i in range(len(s)):
    if s[i] not in f:
        if len(f) < capacity:
            f.append(s[i])
        else:
            for x in range(len(f)):
                if f[x] not in s[i+1:]:
                    f[x] = s[i]
                    print(x)
                    seq.append(x)
                    break
                else:
                    occurance[x] = s[i+1:].index(f[x])
            else:
                f[occurance.index(max(occurance))] = s[i]
                print(occurance.index(max(occurance)))
                seq.append(occurance.index(max(occurance)))
        fault += 1
        pf = 'Yes'
    else:
        pf = 'No'
    print("   %d\t\t" % s[i], end='')
    for x in f:
        print(x, end=' ')
    for x in range(capacity-len(f)):
        print(' ', end=' ')
    print(" %s" % pf)
print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" %
      (len(s), fault, (fault/len(s))*100))
print(seq)
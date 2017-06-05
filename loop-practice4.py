def countdown3(n):
    originaln = n
    while n>0:
        print n
        n = n - 1
    print "DONE!"
    i = 1
    while (i<=originaln):
        print i
        i = i + 1

countdown3(5)

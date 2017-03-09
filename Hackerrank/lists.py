if __name__ == '__main__':
    N = int(raw_input())
    l = []
    for _ in range(N):
        s = raw_input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print l

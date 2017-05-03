if __name__ == '__main__':
    N = int(raw_input())
    arr = list()
    for i in range (0,N):
        input = raw_input()
        split = input.split(' ')
        if split[0] == 'insert':
            arr.insert(int(split[1]),int(split[2]))
        elif split[0] == 'remove':
            arr.remove(int(split[1]))
        elif split[0] == 'append':
            arr.append(int(split[1]))
        elif split[0] == 'sort':
            arr.sort()
        elif split[0] == 'pop':
            arr.pop()
        elif split[0] == 'reverse':
            arr.reverse()
        elif split[0] == 'print':
            print arr
        #else:
         #   print 'Enter proper input'
        i = i+1

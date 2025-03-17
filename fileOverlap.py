def fileOverlap(file1, file2):
    list1 = []
    list2 = []
    
    with open(file1, 'r') as f1:
        for line in f1:
            number = line.strip()
            if not number:
                continue
            list1.append(int(number))
    
        

    with open(file2, 'r') as f2:
        for line in f2:
            number = line.strip()
            if not number:
                continue
            list2.append(int(number))
        
    overlaplist = [i for i in list1 if i in list2]
    print(overlaplist)


fileOverlap("file1.txt", "file2.txt")
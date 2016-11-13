for i in range(3):
    for j in range(3):
        for n in range(3):
            if i==j==n==3:
                break
            else: print(i,j,n)
        else: continue
        break
    else: continue
    break
print("3 3 3")


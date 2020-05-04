
def mordell(n,m):
    for i in range (1,m):
        for j in range (1,m):
            if i*i==j*j*j + n:
                print("y =" ,i, "x =",j)
            

def lista(x):
    y=0
    print ("La lista original es:",x)
    while y<len(x):
        if x[y]<0:
            x[y]=0
        else:
            x[y]=x[y]
        y=y+1
    print ("La lista sin negativos es:",x)
    
lista([2,-3,-10,-5,19,-6])


            




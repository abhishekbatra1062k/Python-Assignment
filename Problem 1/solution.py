import numpy as np

if __name__ == '__main__':

    A = np.array([
        [0, 1, 2, 0],
        [0, 4, 11, 0],
        [14, 14, 41, 0],
        [155, 145, 0, 0]
    ])

    rows,cols=np.shape(A)
    h1=w1=0
    h2=rows-1
    w2=cols-1


    flag=True
    for i in range(rows):
        for j in range(cols):
            if A[i][j]!=0 and flag:
                h1=i
                flag=False
        if not flag:
            break

    flag=True
    for i in range(rows)[::-1]:
        for j in range(cols):
            if A[i][j]!=0 and flag:
                h2=i
                flag=False
        if not flag:
            break

    flag=True
    for i in range(cols):
        for j in range(rows):
            if A[j][i]!=0 and flag:
                w1=i
                flag=False
        if not flag:
            break

    flag=True
    for i in range(cols)[::-1]:
        for j in range(rows):
            if A[j][i]!=0 and flag:
                w2=i
                flag=False
        if not flag:
            break

    print("Coordinates of Smallest rectangle containing all non-zero elements: (",h1,",",w1,")")
    print("Height of Smallest rectangle containing all non-zero elements:", h2-h1+1)
    print("Width of Smallest rectangle containing all non-zero elements:", w2-w1+1)
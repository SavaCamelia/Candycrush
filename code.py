from random import *


def showMatrix(a):
    for i in a:
        print(i)
    print('\n')


def generate():  # functia genereaza o matrice cu elemente cuprinse intre 1 si 4 alese aleator
    a = []
    for i in range(0, 11):
        b = []
        for j in range(0, 11):
            b.append(randint(1, 4))
        a.append(b)
    for i in a:
        shuffle(i)
    return a


def zero_matrix():  # functia returneaza matricea nula
    a = []
    for i in range(0, 11):
        b = []
        for j in range(0, 11):
            b.append(0)
        a.append(b)
    return a


def line_of_3(a, b):  # functia verifica daca exista linie de 3
    for i in range(0, 11):
        for j in range(0, 9):
            if a[i][j] == a[i][j + 1] and a[i][j + 1] == a[i][j + 2]:
                if b[i][j] == 0 and b[i][j + 1] == 0 and b[i][j + 2] == 0:
                    b[i][j] = 1
                    b[i][j + 1] = 1
                    b[i][j + 2] = 1
                    return 1
    return 0


def column_of_3(a, b):  # functia verifica daca exista coloana de 3
    for i in range(0, 9):
        for j in range(0, 11):
            if a[i][j] == a[i + 1][j] and a[i + 1][j] == a[i + 2][j]:
                if b[i][j] == 0 and b[i + 1][j] == 0 and b[i + 2][j] == 0:
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    return 1
        return 0


def line_of_4(a, b):  # functia verifica daca exista linie de 4
    for i in range(0, 11):
        for j in range(0, 8):
            if a[i][j] == a[i][j + 1] and a[i][j + 1] == a[i][j + 2] and a[i][j + 2] == a[i][j + 3]:
                if b[i][j] == 0 and b[i][j + 1] == 0 and b[i][j + 2] == 0 and b[i][j + 3] == 0:
                    b[i][j] = 1
                    b[i][j + 1] = 1
                    b[i][j + 2] = 1
                    b[i][j + 3] = 1
                    return 1
    return 0


def column_of_4(a, b):  # functia verifica daca exista coloana de 4
    for i in range(0, 8):
        for j in range(0, 11):
            if a[i][j] == a[i + 1][j] and a[i + 1][j] == a[i + 2][j] and a[i + 2][j] == a[i + 3][j]:
                if b[i][j] == 0 and b[i + 1][j] == 0 and b[i + 2][j] == 0 and b[i + 3][j] == 0:
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    b[i + 3][j] = 1
                    return 1
    return 0


def line_of_5(a, b):  # functia verifica daca exista linie de 5
    for i in range(0, 11):
        for j in range(0, 7):
            if a[i][j] == a[i][j + 1] and a[i][j + 1] == a[i][j + 2] and a[i][j + 2] == a[i][j + 3] and a[i][j + 3] == \
                    a[i][j + 4]:
                if b[i][j] == 0 and b[i][j + 1] == 0 and b[i][j + 2] == 0 and b[i][j + 3] == 0 and b[i][j + 4] == 0:
                    b[i][j] = 1
                    b[i][j + 1] = 1
                    b[i][j + 2] = 1
                    b[i][j + 3] = 1
                    b[i][j + 4] = 1
                    return 1
    return 0


def column_of_5(a, b):  # functia verifica daca exista coloana de 5
    for i in range(0, 7):
        for j in range(0, 11):
            if a[i][j] == a[i + 1][j] and a[i + 1][j] == a[i + 2][j] and a[i + 2][j] == a[i + 3][j] and a[i + 3][j] == \
                    a[i + 4][j]:
                if b[i][j] == 0 and b[i + 1][j] == 0 and b[i + 2][j] == 0 and b[i + 3][j] == 0 and b[i + 4][j] == 0:
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    b[i + 3][j] = 1
                    b[i + 4][j] = 1
                    return 1
    return 0


def l_shape(a, b):  # functia verifica daca exista formatiune de L
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == a[i + 1][j] and a[i + 1][j] == a[i + 2][j] and a[i + 2][j] == a[i + 2][j + 1] and a[i + 2][
                j + 1] == a[i + 2][j + 2]:
                if b[i][j] == 0 and b[i + 1][j] == 0 and b[i + 2][j] == 0 and b[i + 2][j + 1] == 0 and b[i + 2][
                    j + 2] == 0:
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    b[i + 2][j + 1] = 1
                    b[i + 2][j + 2] = 1
                    return 1
    return 0


def l_shape_at_90_degrees(a, b):  # functia verifica daca exista formatiune de L la 90 de grade
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == a[i + 1][j] and a[i + 1][j] == a[i + 2][j] and a[i + 2][j] == a[i][j + 1] and a[i][j + 1] == \
                    a[i][j + 2]:
                if b[i][j] == 0 and b[i + 1][j] == 0 and b[i + 2][j] == 0 and b[i][j + 1] == 0 and b[i][j + 2] == 0:
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    b[i][j + 1] = 1
                    b[i][j + 2] = 1
                    return 1
    return 0


def l_shape_at_180_degrees(a, b):  # functia verifica daca exista formatiune de L la 180 de grade
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == a[i][j + 1] and a[i][j + 1] == a[i][j + 2] and a[i][j + 2] == a[i + 1][j + 2] and a[i + 1][
                j + 2] == a[i + 2][j + 2]:
                if b[i][j] == 0 and b[i][j + 1] == 0 and b[i][j + 2] == 0 and b[i + 1][j + 2] == 0 and b[i + 2][
                    j + 2] == 0:
                    b[i][j] = 1
                    b[i][j + 1] = 1
                    b[i][j + 2] = 1
                    b[i + 1][j + 2] = 1
                    b[i + 2][j + 2] = 1
                    return 1
    return 0


def l_shape_at_270_degrees(a, b):  # functia verifica daca exista formatiune de L la 270 de grade
    for i in range(0, 9):
        for j in range(2, 11):
            if a[i][j] == a[i + 1][j] and a[i + 1][j] == a[i + 2][j] and a[i + 2][j] == a[i + 2][j - 1] and a[i + 2][
                j - 1] == a[i + 2][j - 2]:
                if b[i][j] == 0 and b[i + 1][j] == 0 and b[i + 2][j] == 0 and b[i + 2][j - 1] == 0 and b[i + 2][
                    j - 2] == 0:
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    b[i + 2][j - 1] = 1
                    b[i + 2][j - 2] = 1
                    return 1
    return 0


def t_shape(a, b):  # functia verifica daca exista formatiune de T
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == a[i][j + 1] and a[i][j + 1] == a[i][j + 2] and a[i][j + 2] == a[i + 1][j + 1] and a[i + 1][
                j + 1] == a[i + 2][j + 1]:
                if b[i][j] == 0 and b[i][j + 1] == 0 and b[i][j + 2] == 0 and b[i + 1][j + 1] == 0 and b[i + 2][
                    j + 1] == 0:
                    b[i][j] = 1
                    b[i][j + 1] = 1
                    b[i][j + 2] = 1
                    b[i + 1][j + 1] = 1
                    b[i + 2][j + 1] = 1
                    return 1
    return 0


def t_shape_at_90_degrees(a, b):  # functia verifica daca exista formatiune de T la 90 de grade
    for i in range(1, 10):
        for j in range(0, 9):
            if a[i][j] == a[i][j + 1] and a[i][j + 1] == a[i][j + 2] and a[i][j + 2] == a[i - 1][j + 2] and a[i - 1][
                j + 2] == a[i + 1][j + 2]:
                if b[i][j] == 0 and b[i][j + 1] == 0 and b[i][j + 2] == 0 and b[i - 1][j + 2] == 0 and b[i + 1][
                    j + 2] == 0:
                    b[i][j] = 1
                    b[i][j + 1] = 1
                    b[i][j + 2] = 1
                    b[i - 1][j + 2] = 1
                    b[i + 1][j + 2] = 1
                    return 1
    return 0


def t_shape_at_180_degrees(a, b):  # functia verifica daca exista formatiune de T la 180 de grade
    for i in range(0, 9):
        for j in range(1, 10):
            if a[i][j] == a[i + 1][j] and a[i + 1][j] == a[i + 2][j] and a[i + 2][j] == a[i + 2][j - 1] and a[i + 2][
                j - 1] == a[i + 2][j + 1]:
                if b[i][j] == 0 and b[i + 1][j] == 0 and b[i + 2][j] == 0 and b[i + 2][j - 1] == 0 and b[i + 2][
                    j + 1] == 0:
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    b[i + 2][j - 1] = 1
                    b[i + 2][j + 1] = 1
                    return 1
    return 0


def t_shape_at_270_degrees(a, b):  # functia verifica daca exista formatiune de T la 270 de grade
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == a[i + 1][j] and a[i + 1][j] == a[i + 2][j] and a[i + 2][j] == a[i + 1][j + 1] and a[i + 1][
                j + 1] == a[i + 1][j + 2]:
                if b[i][j] == 0 and b[i + 1][j] == 0 and b[i + 2][j] == 0 and b[i + 1][j + 1] == 0 and b[i + 1][
                    j + 2] == 0:
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    b[i + 1][j + 1] = 1
                    b[i + 1][j + 2] = 1
                    return 1
    return 0


def find_line_of_3(a, b):
    for i in range(0, 11):
        for j in range(0, 11):
            x = a[i][j]
            if i <= 10:
                if j < 8:
                    if a[i][j + 1] == x and a[i][j + 3] == x:
                        a[i][j + 3], a[i][j + 2] = a[i][j + 2], a[i][j + 3]
                        b[i][j] = 1
                        b[i][j + 1] = 1
                        b[i][j + 2] = 1
                        return 1
                    if a[i][j + 2] == x and a[i][j + 3] == x:
                        a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
                        b[i][j + 1] = 1
                        b[i][j + 2] = 1
                        b[i][j + 3] = 1
                        return 1
                if j < 9 and i < 10:
                    if a[i][j + 1] == x and a[i + 1][j + 2] == x:
                        a[i][j + 2], a[i + 1][j + 2] = a[i + 1][j + 2], a[i][j + 2]
                        b[i][j] = 1
                        b[i][j + 1] = 1
                        b[i][j + 2] = 1
                        return 1
                    if a[i + 1][j + 1] == x and a[i][j + 2] == x:
                        a[i][j + 1], a[i + 1][j + 1] = a[i + 1][j + 1], a[i][j + 1]
                        b[i][j] = 1
                        b[i][j + 1] = 1
                        b[i][j + 2] = 1
                        return 1
                if 0 < j < 10 and i < 10:
                    if a[i + 1][j - 1] == x and a[i][j + 1] == x:
                        a[i + 1][j - 1], a[i][j - 1] = a[i][j - 1], a[i + 1][j - 1]
                        b[i][j] = 1
                        b[i][j - 1] = 1
                        b[i][j + 1] = 1
                        return 1
            if i > 0:
                if j < 9:
                    if a[i - 1][j + 1] == x and a[i][j + 2] == x:
                        a[i - 1][j + 1], a[i][j + 1] = a[i][j + 1], a[i - 1][j + 1]
                        b[i][j] = 1
                        b[i][j + 1] = 1
                        b[i][j + 2] = 1
                        return 1
                if 0 < j < 10:
                    if a[i - 1][j - 1] == x and a[i][j + 1] == x:
                        a[i - 1][j - 1], a[i][j - 1] = a[i][j - 1], a[i - 1][j - 1]
                        b[i][j] = 1
                        b[i][j - 1] = 1
                        b[i][j + 1] = 1
                        return 1
                    if a[i][j - 1] == x and a[i - 1][j + 1] == x:
                        a[i - 1][j + 1], a[i][j + 1] = a[i][j + 1], a[i - 1][j + 1]
                        b[i][j] = 1
                        b[i][j + 1] = 1
                        b[i][j - 1] = 1
                        return 1
    return 0


def find_column_of_3(a, b):
    for i in range(0, 10):
        for j in range(0, 11):
            x = a[i][j]
            if i < 8:
                if x == a[i + 2][j] and x == a[i + 3][j]:
                    a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    b[i + 3][j] = 1
                    return 1
                if x == a[i + 1][j] and x == a[i + 3][j]:
                    a[i + 3][j], a[i + 2][j] = a[i + 2][j], a[i + 3][j]
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    return 1
            if j > 0:
                if x == a[i + 1][j] and x == a[i + 2][j - 1]:
                    a[i + 2][j - 1], a[i + 2][j] = a[i + 2][j], a[i + 2][j - 1]
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    return 1
            if j < 10:
                if x == a[i + 1][j] and x == a[i + 2][j + 1]:
                    a[i + 2][j + 1], a[i + 2][j] = a[i + 2][j], a[i + 2][j + 1]
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    return 1
            if j > 0:
                if x == a[i + 1][j - 1] and x == a[i + 2][j]:
                    a[i + 1][j - 1], a[i + 1][j] = a[i + 1][j], a[i + 1][j - 1]
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    return 1
            if j < 10:
                if x == a[i + 1][j + 1] and x == a[i + 2][j]:
                    a[i + 1][j + 1], a[i + 1][j] = a[i + 1][j], a[i + 1][j + 1]
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    b[i + 2][j] = 1
                    return 1
            if i > 1 and j < 10:
                if x == a[i - 1][j + 1] and x == a[i + 1][j]:
                    a[i - 1][j + 1], a[i - 1][j] = a[i - 1][j], a[i - 1][j + 1]
                    b[i - 1][j] = 1
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    return 1
            if i > 1 and j > 0:
                if x == a[i - 1][j - 1] and x == a[i + 1][j]:
                    a[i - 1][j - 1], a[i - 1][j] = a[i - 1][j], a[i - 1][j - 1]
                    b[i - 1][j] = 1
                    b[i][j] = 1
                    b[i + 1][j] = 1
                    return 1
    return 0


def find_line_of_4(a, b):
    if line_of_3(a, b):#daca exista deja linie de 3
        for i in range(0, 11):
            for j in range(0, 11):
                if b[i][j] == 1:
                    if i > 0:
                        if j > 0:
                            if a[i - 1][j - 1] == a[i][j]:
                                a[i - 1][j - 1], a[i][j - 1] = a[i][j - 1], a[i - 1][j - 1]
                                b[i][j - 1] = 1
                                return 1
                        if j < 8:
                            if a[i - 1][j + 3] == a[i][j]:
                                a[i - 1][j + 3], a[i][j + 3] = a[i][j + 3], a[i - 1][j + 3]
                                b[i][j + 3] = 1
                                return 1
                    if i <= 10:
                        if i < 10 and j > 0:
                            if a[i + 1][j - 1] == a[i][j]:
                                a[i + 1][j - 1], a[i][j - 1] = a[i][j - 1], a[i + 1][j - 1]
                                b[i][j - 1] = 1
                                return 1
                        if i < 10 and j < 8:
                            if a[i + 1][j + 3] == a[i][j]:
                                a[i + 1][j + 3], a[i][j + 3] = a[i][j + 3], a[i + 1][j + 3]
                                b[i][j + 3] = 1
                                return 1
                        if j > 1:
                            if a[i][j - 2] == a[i][j]:
                                a[i][j - 2], a[i][j - 1] = a[i][j - 1], a[i][j - 2]
                                b[i][j - 1] = 1
                                return 1
                        if j < 7:
                            if a[i][j + 4] == a[i][j]:
                                a[i][j + 4], a[i][j + 3] = a[i][j + 3], a[i][j + 4]
                                b[i][j + 3] = 1
                                return 1
                    break
            break
    else:#daca exista doua elemente
        for i in range(0,11):
            for j in range(0,11):
                x=a[i][j]
                if i>0:
                    if j<8:
                        if x==a[i][j+1] and x==a[i][j+3] and x==a[i-1][j+2]:
                            a[i-1][j+2],a[i][j+2]=a[i][j+2],a[i-1][j+2]
                            b[i][j]=1
                            b[i][j+1]=1
                            b[i][j+2]=1
                            b[i][j+3]=1
                            return 1
                        if x==a[i-1][j+1] and x==a[i][j+2] and x==a[i][j+3]:
                            a[i-1][j+1],a[i][j+1]=a[i][j+1],a[i-1][j+1]
                            b[i][j]=1
                            b[i][j + 1] = 1
                            b[i][j + 2] = 1
                            b[i][j + 3] = 1
                            return 1
                if i<10:
                    if j<8:
                        if x==a[i][j+1] and x==a[i][j+3] and x==a[i+1][j+2]:
                            a[i+1][j+2],a[i][j+2]=a[i][j+2],a[i+1][j+2]
                            b[i][j]=1
                            b[i][j+1]=1
                            b[i][j+2]=1
                            b[i][j+3]=1
                            return 1
                        if x==a[i+1][j+1] and x==a[i][j+2] and x==a[i][j+3]:
                            a[i+1][j+1],a[i][j+1]=a[i][j+1],a[i+1][j+1]
                            b[i][j]=1
                            b[i][j + 1] = 1
                            b[i][j + 2] = 1
                            b[i][j + 3] = 1
                            return 1
    return 0

def find_column_of_4(a,b):
    if column_of_3(a,b):
        for i in range(0,11):
            for j in range(0,11):
                if b[i][j]==1:
                    if i>1:
                        if a[i][j]==a[i-2][j]:
                            a[i-2][j],a[i-1][j]=a[i-1][j],a[i-2][j]
                            b[i-1][j]=1
                            return 1
                        if j>0:
                            if a[i][j] == a[i - 1][j-1]:
                                a[i - 1][j-1], a[i - 1][j] = a[i - 1][j], a[i - 1][j-1]
                                b[i - 1][j] = 1
                                return 1
                        if j<10:
                            if a[i][j] == a[i - 1][j+1]:
                                a[i - 1][j+1], a[i - 1][j] = a[i - 1][j], a[i - 1][j+1]
                                b[i - 1][j] = 1
                                return 1
                    if i<8:
                        if i<7:
                            if a[i][j]==a[i+4][j]:
                                a[i+4][j],a[i+3][j]=a[i+3][j],a[i+4][j]
                                b[i+3][j]=1
                                return 1
                        if j>1:
                            if a[i][j]==a[i+3][j-1]:
                                a[i+3][j-1],a[i+3][j]=a[i+3][j],a[i+3][j-1]
                                b[i+3][j]=1
                                return 1
                        if j<10:
                            if a[i][j]==a[i+3][j+1]:
                                a[i+3][j+1],a[i+3][j]=a[i+3][j],a[i+3][j+1]
                                b[i+3][j]=1
                                return 1
                    break
            break
    else:
        for i in range(0,8):
            for j in range(0,11):
                x=a[i][j]
                if j<10:
                    if x==a[i+1][j] and x==a[i+2][j+1] and x==a[i+3][j]:
                        a[i+2][j+1],a[i+2][j]=a[i+2][j],a[i+2][j+1]
                        b[i][j]=1
                        b[i+1][j]=1
                        b[i+2][j] = 1
                        b[i + 3][j] = 1
                        return 1
                    if x==a[i+1][j+1] and x==a[i+2][j] and x==a[i+3][j]:
                        a[i+1][j+1],a[i+1][j]=a[i+1][j],a[i+1][j+1]
                        b[i][j]=1
                        b[i+1][j]=1
                        b[i+2][j] = 1
                        b[i + 3][j] = 1
                        return 1
                if j>1:
                    if x==a[i+1][j] and x==a[i+2][j-1] and x==a[i+3][j]:
                        a[i+2][j-1],a[i+2][j]=a[i+2][j],a[i+2][j-1]
                        b[i][j]=1
                        b[i+1][j]=1
                        b[i+2][j] = 1
                        b[i + 3][j] = 1
                        return 1
                    if x==a[i+1][j-1] and x==a[i+2][j] and x==a[i+3][j]:
                        a[i+1][j-1],a[i+1][j]=a[i+1][j],a[i+1][j-1]
                        b[i][j]=1
                        b[i+1][j]=1
                        b[i+2][j] = 1
                        b[i + 3][j] = 1
                        return 1
    return 0


def find_line_of_5(a,b):#completez cu 3
    if line_of_4(a,b):
        for i in range(0,11):
            for j in range(0,11):
                if a[i][j]==1:
                    if j>1:
                        if a[i][j]==a[i][j-2]:
                            a[i][j-2],a[i][j-1]=a[i][j-1],a[i][j-2]
                            b[i][j-1]=1
                            return 1
                    if j<6:
                        if a[i][j]==a[i][j+5]:
                            a[i][j+5],a[i][j+4]=a[i][j+4],a[i][j+5]
                            b[i][j+4]=1
                            return 1
                    if i < 10:
                        if j>0:
                            if a[i][j]==a[i+1][j-1]:
                                a[i+1][j-1],a[i][j-1]=a[i][j-1],a[i+1][j-1]
                                b[i][j-1]=1
                                return 1
                        if j<7:
                            if a[i][j]==a[i+1][j+4]:
                                a[i+1][j+4],a[i][j+4]=a[i][j+4],a[i+1][j+4]
                                b[i][j+4]=1
                                return 1
                    if i>0:
                        if j > 0:
                            if a[i][j] == a[i - 1][j - 1]:
                                a[i - 1][j - 1], a[i][j - 1] = a[i][j - 1], a[i - 1][j - 1]
                                b[i][j - 1] = 1
                                return 1
                        if j < 7:
                            if a[i][j] == a[i - 1][j + 4]:
                                a[i - 1][j + 4], a[i][j + 4] = a[i][j + 4], a[i - 1][j + 4]
                                b[i][j + 4] = 1
                                return 1
                    break
            break
    else:
        for i in range(0,11):
            for j in range(0,7):
                x=a[i][j]
                if i>1:
                    if x==a[i][j+1] and x==a[i][j+2] and x==a[i-1][j+3] and x==a[i][j+4]:
                        a[i-1][j+3],a[i][j+3]=a[i][j+3],a[i-1][j+3]
                        b[i][j],b[i][j+1],b[i][j+2],b[i][j+3],b[i][j+4]=1,1,1,1,1
                        return 1
                    if x==a[i][j+1] and x==a[i-1][j+2] and x==a[i][j+3] and x==a[i][j+4]:
                        a[i-1][j+2],a[i][j+2]=a[i][j+2],a[i-1][j+2]
                        b[i][j],b[i][j+1],b[i][j+2],b[i][j+3],b[i][j+4]=1,1,1,1,1
                        return 1
                    if x==a[i-1][j+1] and x==a[i][j+2] and x==a[i][j+3] and x==a[i][j+4]:
                        a[i-1][j+1],a[i][j+2]=a[i][j+2],a[i-1][j+1]
                        b[i][j],b[i][j+1],b[i][j+2],b[i][j+3],b[i][j+4]=1,1,1,1,1
                        return 1
                if i<10:
                    if x==a[i][j+1] and x==a[i][j+2] and x==a[i+1][j+3] and x==a[i][j+4]:
                        a[i+1][j+3],a[i][j+3]=a[i][j+3],a[i+1][j+3]
                        b[i][j],b[i][j+1],b[i][j+2],b[i][j+3],b[i][j+4]=1,1,1,1,1
                        return 1
                    if x==a[i][j+1] and x==a[i+1][j+2] and x==a[i][j+3] and x==a[i][j+4]:
                        a[i+1][j+2],a[i][j+2]=a[i][j+2],a[i+1][j+2]
                        b[i][j],b[i][j+1],b[i][j+2],b[i][j+3],b[i][j+4]=1,1,1,1,1
                        return 1
                    if x==a[i+1][j+1] and x==a[i][j+2] and x==a[i][j+3] and x==a[i][j+4]:
                        a[i+1][j+1],a[i][j+2]=a[i][j+2],a[i+1][j+1]
                        b[i][j],b[i][j+1],b[i][j+2],b[i][j+3],b[i][j+4]=1,1,1,1,1
                        return 1
    return 0

def find_column_of_5(a,b):#completez cu 4
    if column_of_4(a,b):
        for i in range(0,11):
            for j in range(0,11):
                if b[i][j]==1:
                    if i>1:
                        if a[i][j]==a[i-2][j]:
                            a[i-2][j],a[i-1][j]=a[i-1][j],a[i-2][j]
                            b[i-1][j]=1
                            return 1
                    if i>0:
                        if j>1:
                            if a[i][j]==a[i-1][j-1]:
                                a[i-1][j-1],a[i-1][j]=a[i-1][j],a[i-1][j-1]
                                b[i-1][j]=1
                                return 1
                        if j <10:
                            if a[i][j] == a[i - 1][j + 1]:
                                a[i - 1][j + 1], a[i - 1][j] = a[i - 1][j], a[i - 1][j + 1]
                                b[i - 1][j] = 1
                                return 1
                    if i<7:
                        if i<6:
                            if a[i][j]==a[i+5][j]:
                                a[i +5][j], a[i + 4][j] = a[i +4][j], a[i +5][j]
                                b[i +4][j] = 1
                                return 1
                        if j > 1:
                            if a[i][j] == a[i +4][j - 1]:
                                a[i + 4][j - 1], a[i + 4][j] = a[i + 4][j], a[i + 4][j - 1]
                                b[i + 4][j] = 1
                                return 1
                        if j < 10:
                            if a[i][j] == a[i + 4][j + 1]:
                                a[i + 4][j + 1], a[i + 4][j] = a[i + 4][j], a[i + 4][j + 1]
                                b[i + 4][j] = 1
                                return 1
                    break
            break
    else:
        for i in range(0,7):
            for j in range(0,11):
                x=a[i][j]
                if j>1:
                    if x==a[i+1][j] and x==a[i+2][j] and x==a[i+3][j-1] and x==a[i+4][j]:
                        a[i+3][j-1],a[i+3][j]=a[i+3][j],a[i+3][j-1]
                        b[i][j],b[i+1][j],b[i+2][j],b[i+3][j],b[i+4][j]=1,1,1,1,1
                        return 1
                    if x==a[i+1][j] and x==a[i+2][j-1] and x==a[i+3][j] and x==a[i+4][j]:
                        a[i+2][j-1],a[i+2][j]=a[i+2][j],a[i+2][j-1]
                        b[i][j],b[i+1][j],b[i+2][j],b[i+3][j],b[i+4][j]=1,1,1,1,1
                        return 1
                    if x==a[i+1][j-1] and x==a[i+2][j] and x==a[i+3][j] and x==a[i+4][j]:
                        a[i+1][j-1],a[i+1][j]=a[i+1][j],a[i+1][j-1]
                        b[i][j],b[i+1][j],b[i+2][j],b[i+3][j],b[i+4][j]=1,1,1,1,1
                        return 1
                if j<10:
                    if x==a[i+1][j] and x==a[i+2][j] and x==a[i+3][j+1] and x==a[i+4][j]:
                        a[i+3][j+1],a[i+3][j]=a[i+3][j],a[i+3][j+1]
                        b[i][j],b[i+1][j],b[i+2][j],b[i+3][j],b[i+4][j]=1,1,1,1,1
                        return 1
                    if x==a[i+1][j] and x==a[i+2][j+1] and x==a[i+3][j] and x==a[i+4][j]:
                        a[i+2][j+1],a[i+2][j]=a[i+2][j],a[i+2][j+1]
                        b[i][j],b[i+1][j],b[i+2][j],b[i+3][j],b[i+4][j]=1,1,1,1,1
                        return 1
                    if x==a[i+1][j+1] and x==a[i+2][j] and x==a[i+3][j] and x==a[i+4][j]:
                        a[i+1][j+1],a[i+1][j]=a[i+1][j],a[i+1][j+1]
                        b[i][j],b[i+1][j],b[i+2][j],b[i+3][j],b[i+4][j]=1,1,1,1,1
                        return 1
    return 0


def find_L_shape(a,b):#completez cu 1
    if line_of_3(a,b):
        for i in range(0,11):
            for j in range(0,11):
                if i>1:
                    if a[i][j] == a[i - 1][j]:
                        if j>1:
                            if a[i-2][j-1]==a[i][j]:
                                a[i-2][j-1],a[i-2][j]=a[i-2][j],a[i-2][j-1]
                                b[i-1][j],b[i-2][j]=1,1
                                return 1
                        if j<10:
                            if a[i-2][j+1]==a[i][j]:
                                a[i-2][j+1],a[i-2][j]=a[i-2][j],a[i-2][j+1]
                                b[i-1][j],b[i-2][j]=1,1
                                return 1
                        if i>2:
                            if a[i-3][j]==a[i][j]:
                                a[i-3][j],a[i-2][j]=a[i-2][j],a[i-3][j]
                                b[i-1][j],b[i-2][j]=1,1
                                return 1
                    elif a[i][j]==a[i-2][j]:
                        if j>0:
                            if a[i][j]==a[i-1][j-1]:
                                a[i-1][j-1],a[i-1][j]=a[i-1][j],a[i-1][j-1]
                                b[i - 1][j], b[i - 2][j] = 1, 1
                                return 1
                        if j<10:
                            if a[i][j]==a[i-1][j+1]:
                                a[i-1][j+1],a[i-1][j]=a[i-1][j],a[i-1][j+1]
                                b[i - 1][j], b[i - 2][j] = 1, 1
                                return 1
                    if j<9:
                        if a[i][j] == a[i - 1][j + 2]:
                            if i>2:
                                if a[i-3][j+2]==a[i][j]:
                                    a[i-3][j+2],a[i-2][j+2]=a[i-2][j+2],a[i-3][j+2]
                                    b[i-1][j+2],b[i-2][j+2]=1,1
                                    return 1
                            if j>1:
                                if a[i-2][j+1]==a[i][j]:
                                    a[i-2][j+1],a[i-2][j+2]=a[i-2][j+2],a[i-2][j+1]
                                    b[i-1][j+2],b[i-2][j+2]=1,1
                                    return 1
                            if j<8:
                                if a[i-2][j+3]==a[i][j]:
                                    a[i-2][j+3],a[i-2][j+2]=a[i-2][j+3],a[i-2][j+2]
                                    b[i-1][j+2],b[i-2][j+2]=1,1
                                    return 1
                        elif a[i][j] == a[i - 2][j+2]:
                            if j<9:
                                if a[i][j] == a[i - 1][j + 1]:
                                    a[i - 1][j + 1], a[i - 1][j+2] = a[i - 1][j+2], a[i - 1][j + 1]
                                    b[i - 1][j], b[i - 2][j] = 1, 1
                                    return 1
                            if j < 8:
                                if a[i][j] == a[i - 1][j + 3]:
                                    a[i - 1][j + 3], a[i - 1][j+2] = a[i - 1][j+2], a[i - 1][j + 3]
                                    b[i - 1][j], b[i - 2][j] = 1, 1
                                    return 1
                if i<9:
                    if j<9:
                        if a[i][j]==a[i+1][j+2]:
                            if a[i+2][j+1]==a[i][j]:
                                a[i+2][j+1],a[i+2][j+2]=a[i+2][j+2],a[i+2][j+1]
                                b[i+1][j+2],b[i+2][j+2]=1,1
                                return 1
                            if j<8:
                                if a[i + 2][j + 3] == a[i][j]:
                                    a[i + 2][j + 3], a[i + 2][j + 2] = a[i + 2][j + 2], a[i + 2][j + 3]
                                    b[i + 1][j + 2], b[i + 2][j + 2] = 1, 1
                                    return 1
                            if i<8:
                                if a[i + 3][j + 2] == a[i][j]:
                                    a[i + 3][j + 2], a[i + 2][j + 2] = a[i + 2][j + 2], a[i + 3][j + 2]
                                    b[i + 1][j + 2], b[i + 2][j + 2] = 1, 1
                                    return 1
                        elif a[i][j]==a[i+2][j+2]:
                            if a[i][j]==a[i+1][j+1]:
                                a[i+1][j+1],a[i+1][j+2]=a[i+1][j+2],a[i+1][j+1]
                                b[i + 1][j + 2], b[i + 2][j + 2] = 1, 1
                                return 1
                            if j<8:
                                if a[i + 1][j + 3] == a[i][j]:
                                    a[i + 1][j + 3], a[i + 1][j + 2] = a[i + 1][j + 2], a[i + 1][j + 3]
                                    b[i + 1][j + 2], b[i + 2][j + 2] = 1, 1
                                    return 1
                    if a[i][j]==a[i+1][j]:
                        if j<10:
                            if a[i+2][j+1]==a[i][j]:
                                a[i+2][j+1],a[i+2][j]=a[i+2][j],a[i+2][j+1]
                                b[i+1][j],b[i+2][j]=1,1
                                return 1
                        if j>0:
                            if a[i + 2][j-1] == a[i][j]:
                                a[i + 2][j-1], a[i + 2][j] = a[i + 2][j], a[i + 2][j-1]
                                b[i + 1][j], b[i + 2][j] = 1, 1
                                return 1
                        if i<8:
                            if a[i + 3][j] == a[i][j]:
                                a[i + 3][j], a[i + 2][j] = a[i + 2][j], a[i + 3][j]
                                b[i + 1][j], b[i + 2][j] = 1, 1
                                return 1
                    elif a[i][j]==a[i+2][j]:
                        if j>0 and j<10:
                            if a[i][j]==a[i+1][j+1]:#bug
                                a[i+1][j-1],a[i+1][j]=a[i+1][j],a[i+1][j-1]
                                b[i + 1][j], b[i + 2][j] = 1, 1
                                return 1
                        if j<10:
                            if a[i + 1][j + 1] == a[i][j]:
                                a[i + 1][j + 1], a[i + 1][j] = a[i + 1][j], a[i + 1][j + 1]
                                b[i + 1][j], b[i + 2][j] = 1, 1
                                return 1
    return 0

def find_T_shape(a,b):
    if line_of_3(a,b):
        for i in range(0,11):
            for j in range(0,11):
                if i<9:
                    if j<10:
                        if a[i][j]==a[i+1][j+1]:
                            if j<9:
                                if a[i][j]==a[i+2][j+2]:
                                    a[i+2][j+1],a[i+2][j+2]=a[i+2][j+2],a[i+2][j+1]
                                    b[i+1][j+1],b[i+2][j+1]=1,1
                                    return 1
                            if a[i][j]==a[i+2][j]:
                                a[i+2][j],a[i+2][j+1]=a[i+2][j+1],a[i+2][j]
                                b[i+1][j+1],b[i+2][j+1]=1,1
                                return 1
                            if i<8:
                                if a[i][j] == a[i + 3][j+1]:
                                    a[i + 3][j+1], a[i + 2][j+1] = a[i + 2][j+1], a[i + 3][j+1]
                                    b[i + 1][j + 1], b[i + 2][j + 1] = 1, 1
                                    return 1
                        elif a[i][j]==a[i+2][j+1]:
                            if j<9:
                                if a[i][j]==a[i+1][j+2]:
                                    a[i+1][j+1],a[i+1][j+2]=a[i+1][j+2],a[i+1][j+1]
                                    b[i+1][j+1],b[i+2][j+1]=1,1
                                    return 1
                            if a[i][j]==a[i+1][j]:
                                a[i+1][j],a[i+1][j+1]=a[i+1][j+1],a[i+1][j]
                                b[i+1][j+1],b[i+2][j+1]=1,1
                                return 1
                if i>1:
                    if j<10:
                        if a[i][j]==a[i-1][j+1]:
                            if j<9:
                                if a[i][j]==a[i-2][j+2]:
                                    a[i-2][j+1],a[i-2][j+2]=a[i-2][j+2],a[i-2][j+1]
                                    b[i-1][j+1],b[i-2][j+1]=1,1
                                    return 1
                            if a[i][j]==a[i-2][j]:
                                a[i-2][j],a[i-2][j+1]=a[i-2][j+1],a[i-2][j]
                                b[i-1][j+1],b[i-2][j+1]=1,1
                                return 1
                            if i>2:
                                if a[i][j] == a[i - 3][j+1]:
                                    a[i - 3][j+1], a[i - 2][j+1] = a[i - 2][j+1], a[i - 3][j+1]
                                    b[i - 1][j + 1], b[i - 2][j + 1] = 1, 1
                                    return 1
                        elif a[i][j]==a[i-2][j+1]:
                            if j<9:
                                if a[i][j]==a[i-1][j+2]:
                                    a[i-1][j+1],a[i-1][j+2]=a[i-1][j+2],a[i-1][j+1]
                                    b[i-1][j+1],b[i-2][j+1]=1,1
                                    return 1
                            if a[i][j]==a[i-1][j]:
                                a[i-1][j],a[i-1][j+1]=a[i-1][j+1],a[i-1][j]
                                b[i-1][j+1],b[i-2][j+1]=1,1
                                return 1
                if i>0 and i<10:
                    if j<9:
                        if a[i][j]==a[i+1][j+2]:
                            if a[i][j]==a[i-1][j+1]:
                                a[i-1][j+1],a[i-1][j+2]=a[i-1][j+2],a[i-1][j+1]
                                a[i-1][j+2],a[i+1][j+2]=1,1
                                return 1
                            if i>1:
                                if a[i][j] == a[i - 2][j + 2]:
                                    a[i - 1][j + 2], a[i - 2][j + 2] = a[i - 2][j + 2], a[i - 1][j + 2]
                                    a[i - 1][j + 2], a[i + 1][j + 2] = 1, 1
                                    return 1
                            if j<8:
                                if a[i][j] == a[i - 1][j + 3]:
                                    a[i - 1][j + 3], a[i - 1][j + 2] = a[i - 1][j + 2], a[i - 1][j + 3]
                                    a[i - 1][j + 2], a[i + 1][j + 2] = 1, 1
                                    return 1
                        elif a[i][j]==a[i-1][j+2]:
                            if a[i][j]==a[i+1][j+1]:
                                a[i+1][j+1],a[i+1][j+2]=a[i+1][j+2],a[i+1][j+1]
                                a[i-1][j+2],a[i+1][j+2]=1,1
                                return 1
                            if i<9:
                                if a[i][j] == a[i + 2][j + 2]:
                                    a[i + 1][j + 2], a[i + 2][j + 2] = a[i + 2][j + 2], a[i + 1][j + 2]
                                    a[i - 1][j + 2], a[i + 1][j + 2] = 1, 1
                                    return 1
                            if j<8:
                                if a[i][j] == a[i + 1][j + 3]:
                                    a[i + 1][j + 3], a[i + 1][j + 2] = a[i + 1][j + 2], a[i + 1][j + 3]
                                    a[i - 1][j + 2], a[i + 1][j + 2] = 1, 1
                                    return 1
                    if j>1:
                        if a[i][j]==a[i+1][j]:
                            if j<10 and a[i][j]==a[i-1][j+1]:
                                a[i-1][j+1],a[i-1][j]=a[i-1][j],a[i-1][j+1]
                                b[i-1][j],b[i+1][j]=1,1
                                return 1
                            if i>1:
                                if a[i][j]==a[i-2][j]:
                                    a[i-2][j],a[i-1][j]=a[i-1][j],a[i-2][j]
                                    b[i - 1][j], b[i + 1][j] = 1, 1
                                    return 1
                            if a[i][j]==a[i-1][j-1]:
                                a[i-1][j-1],a[i-1][j]=a[i-1][j],a[i-1][j-1]
                                b[i - 1][j], b[i + 1][j] = 1, 1
                                return 1
                        elif a[i][j]==a[i-1][j]:
                            if j<10 and a[i][j]==a[i+1][j+1]:
                                a[i+1][j+1],a[i+1][j]=a[i+1][j],a[i+1][j+1]
                                b[i-1][j],b[i+1][j]=1,1
                                return 1
                            if i<9:
                                if a[i][j]==a[i+2][j]:
                                    a[i+2][j],a[i+1][j]=a[i+1][j],a[i+2][j]
                                    b[i - 1][j], b[i + 1][j] = 1, 1
                                    return 1
                            if a[i][j]==a[i+1][j-1]:
                                a[i+1][j-1],a[i+1][j]=a[i+1][j],a[i+1][j-1]
                                b[i - 1][j], b[i + 1][j] = 1, 1
                                return 1
    return 0





def fall(a, b):
    for i in range(0, 11):
        for j in range(10, -1, -1):
            if b[j][i] != 0:
                for k in range(j, 0, -1):
                    a[k][i] = a[k - 1][i]
                a[0][i] = randint(1, 4)
                b[j][i] = 0
                j += 1  # s-ar putea sa am coloana de elemente egale
                # prin urmare mai verificam inca o data aceasta pozitie dupa ce au cazut elementele
    showMatrix(a)


def repeatFunction(a, b):
    score = 0
    while line_of_5(a, b):
        score += 50
        fall(a, b)
        showMatrix(a)
    while column_of_5(a, b):
        score += 50
        fall(a, b)
        showMatrix(a)
    return score


def repeatOthers(a, b):
    score = 0
    while t_shape(a, b):
        score += 30
        fall(a, b)
        showMatrix(a)
    while t_shape_at_90_degrees(a, b):
        score += 30
        fall(a, b)
        showMatrix(a)
    while t_shape_at_180_degrees(a, b):
        score += 30
        fall(a, b)
        showMatrix(a)
    while t_shape_at_270_degrees(a, b):
        score += 30
        fall(a, b)
        showMatrix(a)
    return score


def main():
    games=1
    totalScore=0
    while games>0:
        score = 0
        interschimbari = 10000
        a = generate()
        b = zero_matrix()
        check = True
        while check and interschimbari > 0:
            check = False
            print("Matricea e:")
            showMatrix(a)
            while line_of_5(a, b):
                score += 50
                fall(a, b)
            while column_of_5(a, b):
                score += 50
                fall(a, b)
            while t_shape(a, b):
                score += 30
                fall(a, b)
                score += repeatFunction(a, b)
            while t_shape_at_90_degrees(a, b):
                score += 30
                fall(a, b)
                score += repeatFunction(a, b)
            while t_shape_at_180_degrees(a, b):
                score += 30
                fall(a, b)
                score += repeatFunction(a, b)
            while t_shape_at_270_degrees(a, b):
                score += 30
                fall(a, b)
                score += repeatFunction(a, b)
            while l_shape(a, b)!=0:
                score += 20
                fall(a, b)
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
            while l_shape_at_90_degrees(a, b):
                score += 20
                fall(a, b)
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
            while l_shape_at_180_degrees(a, b):
                score += 20
                fall(a, b)
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
            while l_shape_at_270_degrees(a, b):
                score += 20
                fall(a, b)
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
            while line_of_4(a, b):
                score += 10
                fall(a, b)
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
            while column_of_4(a, b):
                score += 10
                fall(a, b)
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
            while line_of_3(a, b):
                score += 5
                fall(a, b)
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
            while column_of_3(a, b):
                score += 5
                fall(a, b)
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
            if find_line_of_5(a, b):
                check = True
                score += 50
                interschimbari -= 1
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
                fall(a, b)
            elif find_column_of_5(a,b)!=0:
                check = True
                score += 50
                interschimbari -= 1
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
                fall(a, b)
            if find_T_shape(a,b):
                check = True
                score += 30
                interschimbari -= 1
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
                fall(a, b)
            if find_L_shape(a,b):
                check = True
                score += 20
                interschimbari -= 1
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
                fall(a, b)
            if find_line_of_4(a, b):
                check = True
                score += 10
                interschimbari -= 1
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
                fall(a, b)
            elif find_column_of_4(a, b):
                check = True
                score += 10
                interschimbari -= 1
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
                fall(a, b)
            if find_line_of_3(a, b):
                check = True
                score += 5
                interschimbari -= 1
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
                fall(a, b)
            elif column_of_3(a, b):
                check = True
                score += 5
                interschimbari -= 1
                score += repeatFunction(a, b)
                score += repeatOthers(a, b)
            fall(a, b)
            score += repeatFunction(a, b)
            score += repeatOthers(a, b)
            showMatrix(a)
            print(score,"au mai ramas ",interschimbari)
        totalScore+=score
        games-=1
    print("Media celor 1000 de jocuri e: ",totalScore/1000)


if __name__ == "__main__":
    main()

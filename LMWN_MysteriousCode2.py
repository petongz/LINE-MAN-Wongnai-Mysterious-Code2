import numpy as np

txt = "CYtZBsWZaZliYZocWLZlXuZZYWYeYXZsXeZXtXWpXeRYYYd!ZnYeWXoYXasnX,WXWrWPoAdWesnciGenWr"

txt2 = ""
for c in txt:
    txt2 = txt2 + c if c not in 'WXYZ' else txt2
    
def zigzag_easy(txt, numRows):
    i = 0
    j = 0
    status = 'down'

    mat = np.array([[' ' for j in range(numRows)] for i in range(numRows)], dtype = 'object')

    for c in txt:
        mat[i, j] = c
        if status == 'down':
            if i+1 < mat.shape[0]:
                i = i + 1
            else:
                status = 'up'
                if j + 1 == mat.shape[1]:
                    mat = np.concatenate([mat, np.array([[' ' for k in range(numRows)]], dtype = 'object').T], axis = 1)
                i = i - 1
                j = j + 1
        elif status == 'up':
            if i != 0:
                if j + 1 == mat.shape[1]:
                    mat = np.concatenate([mat, np.array([[' ' for k in range(numRows)]], dtype = 'object').T], axis = 1)
                i = i - 1
                j = j + 1
            else:
                status = 'down'
                i = i + 1

    if mat[:, -1].sum().strip() == '':
        mat = mat[:, :-1].copy()

    return mat

def zigzag_txt(s, matrix_loc, map_thai = False, ban = 'WXYZ'):
    a, b = matrix_loc.shape
    m = np.zeros((a, b), dtype="object")
    for i in range(a):
        for j in range(b):
            if matrix_loc[i, j] == ' ':
                m[i, j] = " "
                continue

            if len(s) >= int(matrix_loc[i, j]):

                c = s[int(matrix_loc[i, j]) - 1]

                if c in ban:
                    c = ' '

                if map_thai:
                    m[i, j] = map_keyboard.get(c, ' ')
                else:
                    m[i, j] = c

            else:
                m[i, j] = " "
    
    return m

def zigzag_easy_inverse(s, numRows):
    
    mat = zigzag_easy(s, numRows = numRows)

    i = 1
    l2 = []
    for l in mat:
        l1 = []
        for c in l:
            if c != ' ':
                l1.append(i)
                i = i + 1
            else:
                l1.append(' ')
        l2.append(l1)

    mat2 = np.array(l2)
    
    mat3 = zigzag_txt(s, mat2, map_thai = False, ban = '')

    i = 0
    j = 0
    c = mat3[i, j]
    status = 'down'

    s2 = ""

    while c != ' ':
        s2 += c
        if status == 'down':
            if i+1 < mat3.shape[0]:
                i = i + 1
            else:
                status = 'up'
                i = i - 1
                j = j + 1
        elif status == 'up':
            if i != 0:
                i = i - 1
                j = j + 1
            else:
                status = 'down'
                i = i + 1
            
        if j == mat3.shape[1]: break

        c = mat3[i, j]
    
    return s2

if __name__ == '__main__':
    print("Answer:", zigzag_easy_inverse(txt2, numRows = 4))

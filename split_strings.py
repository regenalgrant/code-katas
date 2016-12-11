def solution(s):

    split_s = [ s[index-1] + s[index] 
    for index in range(len(s)) if index % 2 ] 

    if  len(s) % 2:
        split_s.append(s[-1] + '_')

    return split_s
    pass
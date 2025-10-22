def reverse_letter(a):
    for i in range(len(a)-1,0-1,-1):
        result="".join(a[i])
    print(result)

reverse_letter("python")
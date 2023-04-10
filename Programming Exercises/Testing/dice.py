for r in [0,1,2,3,4,5]:
    C='o '
    s='-----\n|'+C[r<1]+' '+C[r<3]+'|\n|'+C[r<5]
    print(s+C[r&1]+s[::-1])
    print('\n')

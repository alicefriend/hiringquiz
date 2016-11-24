def solve(denominator):
    
    #1 job for getting length of not recurring part
    factor_2, factor_5 = 0, 0
    reduction = denominator
    while (reduction % 2 == 0) or (reduction % 5 == 0):
        if reduction % 2 == 0:
            factor_2 += 1
            reduction = int(reduction / 2)
        if reduction % 5 == 0:
            factor_5 += 1
            reduction = int(reduction / 5)
    
    length_not_recur = factor_2 if factor_2 > factor_5 else factor_5
    

    # if there's no recurring part, end function
    if reduction == 1:
        return
    
    
    #2 job for getting length of recurring part
    length_recur = 1
    while True:
        if (10**length_recur - 1) % reduction == 0: break
        length_recur += 1
        
        
    #3 getting recurring part number
    numerator = 1
    rest = numerator
    digit = []
    
    for i in range(length_not_recur):
        rest *= 10
        rest %= denominator
        
    for i in range(length_recur):
        rest *= 10
        share = str(int(rest / denominator))
        digit.append(share)
        rest %= denominator
    
    answer = ''.join(digit)
    print(denominator, answer)

N = input()
solve(int(N))
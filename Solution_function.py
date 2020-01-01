def solution(num):
    ''' int-> int 
    
    give the sum of numbers smaller than num(inclusive)
    which can only be devided to 3 or 5
    
    >>> solution(6)
    14
    
    >>> solution(11)
    33
    
    >>> solution(56)
    753    
    '''
    return sum([i for i in range(num+1) if i % 3 == 0 or i % 5 == 0])
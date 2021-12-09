''' 
    given a (start) and a (length), return the sum of a matrix of consecutive numbers where for 
    each row you stop counting 1 element sooner, when all of these numbers are xor'ed consecutively.
    example below....

    start = 100
    length = 9

    100  101  102  103  104  105  106  107  108
    109  110  111  112  113  114  115  116  ___
    118  119  120  121  122  123  124  ___  ___
    127  128  129  130  131  132  ___  ___  ___
    136  137  138  139  140  ___  ___  ___  ___
    145  146  147  148  ___  ___  ___  ___  ___
    154  155  156  ___  ___  ___  ___  ___  ___
    163  164  ___  ___  ___  ___  ___  ___  ___
    172  ___  ___  ___  ___  ___  ___  ___  ___

    100^101^102^103^104^105^106^107^108^109^110^111^112^113^114^115^116^118^119^120^121^122^123^124^... 

'''

def solution(start, length):
    
    def xor_n( n ) :
        k = n % 4;
        if(k == 0) :
            return n;
        elif(k == 1) :
            return 1;
        elif(k == 2) :
            return n + 1;
        elif(k == 3) :
            return 0;

    s = start;
    l = length;
    _sum = 0;
    for i in range(l) :
        _k = l - i - 1;
        _sum = _sum ^ xor_n(s + (i * l) + _k) ^ xor_n(s + (i * l) - 1);
        
    return _sum;
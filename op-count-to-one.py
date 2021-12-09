'''
    given a number (n) and the operations  +1 , -1 , /2  return the
    smallest number of operations that will change n to 1 while 
    while maintaining that (n) is always an integer. This means you 
    can only divide by 2 when (n = a-power-of-two).
'''

def solution_(n):
    count = 0;
    while n > 1:
        if( n & 1 == 1 ):
            if( n % 4 == 1 or n == 3) :
                n -= 1;
            else :
                n += 1;
        else :
            n = n >> 1;
        count += 1;

    return count;

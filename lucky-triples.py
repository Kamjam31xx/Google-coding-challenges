'''
    given a list of sorted numbers, return the number of (x,y,z) pairs.
    where x|y and y|z (x divides y & y divides z). 
'''

def solution(l):

    list_length = len(l);
    count = 0;
    count2 = 0;
    total = 0;
    
    for j in range(1, list_length - 1) :
        for k in range(j + 1, list_length) :
            if(l[k]%l[j] == 0) :
                count += 1;
        if(count > 0) :
            for i in range(0, j) :
                if(l[j]%l[i] == 0) :
                    count2 += 1;
        total = total + (count * count2);
        count = 0;
        count2 = 0;

    return total;

print(solution([2, 3, 4, 8, 16, 32, 7]));
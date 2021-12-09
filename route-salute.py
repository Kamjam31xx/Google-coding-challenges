'''
    each employee must salute when they pass
    salutes last 5 seconds
    the encounter lasts 10 seconds because they salute sequentially
    
    you are given the hallway layout with this string
    hallway layout string example : "--->-><-><-->-"
    
    character keys are as follows
    char( '>' )    an employee walking to the right
    char( '<' )    an employee walking to the left
    char( '-' )    an empty space
    each employee walks the same speed in all directions
'''

def solution(s) :
    chars = list(s.replace('-',''));
    w_chars = len(chars);
    salutes = 0;
    r_count = 0;
    for i in range(w_chars) :
        if (chars[i] == '>') :
            r_count += 1;
        else :
            salutes += 2 * r_count;
    return salutes;
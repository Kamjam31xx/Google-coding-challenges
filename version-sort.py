'''
    given a list of versions (ex : "1.0 , 3.2.1 , 0.23.1"),
    sort the list and return it.
'''

def solution(l):

    def version_a_greater_than_b(_a, _b) :
            
        ver_a = _a.split('.');
        ver_a = [int(element) for element in ver_a];
        ver_b = _b.split('.');
        ver_b = [int(element) for element in ver_b];
            
        len_a = len(ver_a);
        len_b = len(ver_b);

        if(len_a > len_b) :
            for i in range(len_b, len_a):
                ver_b.append(0);
        elif(len_b > len_a) :
            for i in range(len_a, len_b):
                ver_a.append(0);
            
        for i in range(len(ver_a)) :
            if(ver_a[i] > ver_b[i]) :
                return True;
            elif(ver_a[i] < ver_b[i]) :
                return False;
                    
        if(len_a > len_b) :
            return True;
        else :
            return False;

    def quick_sort_versions(_arr) :
        
        length = len(_arr);
        pivot = None;
        
        if( length <= 1 ) :
            return _arr;
        else :
            pivot = _arr.pop();
            
        high = [];
        low = [];
        
        for element in _arr :
            if(version_a_greater_than_b(element, pivot)) :
                high.append(element);
            else:
                low.append(element);
                
        return quick_sort_versions(low) + [pivot] + quick_sort_versions(high);
                
    return quick_sort_versions(l);

test_arr = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"];
sort_arr = solution(test_arr);
print(sort_arr);
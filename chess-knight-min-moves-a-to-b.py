'''
    given a src(source) square and a dest(destination) square on a chess board,
    place a knight on that spot. give the least number of moves the knight can make
    to travel from the source square to the destination square.
'''

def solution(src, dest):

    if(src == dest):
        return 0;
    
    import math;
    # used like macros for references x and y from arrays
    x = 0;
    y = 1;
    
    def index_to_xy(_i) :
        # conver index into xy position on a grid of size 8x8
        x_coord = _i % 8;
        y_coord = math.floor(_i/8);
        
        return [x_coord, y_coord];

    def xy_to_index(_xy) :
        # converts an [x,y] coordinate into an index on a grid of size 8x8
        return _xy[x] + (_xy[y] * 8);
        
    def is_legal_position(_coords) :
        # test if a coordinate is on the chess board
        if(_coords[x] > 7 or _coords[x] < 0 or _coords[y] > 7 or _coords[y] < 0):
            # position is not on the chess board
            return False;
        else :
            # position is on the chess board
            return True;
            
    def add_vectors(_vec1, _vec2) :
        # adds two vectors together and returns the resulting vector
        return [_vec1[x] + _vec2[x], _vec1[y] + _vec2[y]];
        
    def is_equal_vector(_vec1, _vec2) :
        # checks if two vectors are equal
        if(_vec1[x] != _vec2[x] or _vec1[y] != _vec2[y]) :
            return False;
        else :
            return True;

    def remove_duplicates_in_list(_list) :
        # removes duplicated elements from a list
        new_list = [];
        for element in _list :
            if element not in new_list :
                new_list.append(element);
        
        return new_list;

    def remove_a_if_in_b(_list_a, _list_b) :
        new_list = [];
        for a in _list_a :
            if a not in _list_b :
                new_list.append(a);
        return new_list;

    def move_knight(_start_positions, _end, _visited, _last_step) :

        possible_moves = [[2,1], [2,-1], [-2, 1], [-2, -1], [1,2], [1,-2], [-1, 2], [-1, -2]]; 
        knight_move_count = 8;

        new_positions = [];
        for position in _start_positions :
            for i in range(knight_move_count) :
                new_position = add_vectors(position, possible_moves[i]);
                if(is_legal_position(new_position)) :
                    new_positions.append(new_position);

        new_positions = remove_duplicates_in_list(new_positions);
        visited = [];
        for p in _start_positions :
            if p not in _visited :
                visited.append(p);
        for p in _visited :
            visited.append(p);
        

        new_positions = remove_a_if_in_b(new_positions, visited);

        for p in new_positions :
            if( p == _end ) :
                return _last_step + 1;

        if(_last_step < 8) :
            return move_knight(new_positions, _end, visited, _last_step + 1);

  
    start = index_to_xy(src);
    end = index_to_xy(dest);
     
    return move_knight([start], end, [start], 0);
    

solution(0, 63);

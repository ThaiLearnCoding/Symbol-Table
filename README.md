# Advanced Programming : Assignment 3
    My design is like this:
    Initially [[]]
    When we want to add new variable, add it to the list.   
        ex: insert x        -> [[x]]
            insert y        -> [[x, y]]
            begin           -> [[x, y], []]
                int x       -> [[x, y], [x]]
                begin       -> [[x, y], [x], []]
                    int m   -> [[x, y], [x], [m]]
                end         -> [[x, y], [x]]
                int z       -> [[x, y], [x, z]]
            end             -> [[x, y]]
    If the program is valid, it should only contain one list in that list.
    The index of the block will be the scope level for it.
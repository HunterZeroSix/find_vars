def find_vars(msg, sep, sep_end=None):
    '''
    Get all vars in a text and returns it as list  
    Usecase: 
    - find_vars("__test__", sep="__")
    - find_vars("{test}", sep="{", sep_end="}")

    str(msg), str(sep), sep_end default as None else as str(sep_end)  
    '''
    # setup message counter
    if (sep_end == None) or (sep_end == sep): 
        sep_count, sep_end = int(msg.count(sep)/2), sep
    elif (sep_end == "") or (sep_end == ''):
        raise ValueError('sep_end can not be a empty string')
    else: sep_count = int(msg.count(sep))
    
    t = 0 # Init startpoint
    found_list = [] # Init list
    for i in range(0,sep_count):
        found_start = msg.find(sep, t) + len(sep) # found beginning of the var
        found_end = msg.find(sep_end, found_start) # found end of the var
        found_var = msg[found_start:found_end] # return var between the sep
        if found_var not in found_list: # if found_var is not in list
            found_list.append(found_var) # add to list
        t = found_end + len(sep_end)
        # print("Variable", i+1, "|", found_var)
    from contextlib import redirect_stdout 
    with redirect_stdout(None): print(i)
    return found_list # return list

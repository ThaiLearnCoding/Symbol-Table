from StaticError import *
from Symbol import *
from functools import *

def is_valid_identifier(name):
    return name.isidentifier() and name[0].islower()

def is_valid_type(type):
    return type in ['number', 'string']

def is_number(val):
    if val.isdigit():
        if int(val) >= 0:
            return True
    return False

def is_string(val):
    return (
        len(val) >= 2 and
        val[0] == val[-1] == "'" and
        (len(val) == 2 or val[1:-1].isalnum())
    )

def lookup_identifier(table, name):
    return [ (symbol, level) for (scope, level) in zip(reversed(table), reversed(range(len(table)))) for symbol in reversed(scope) if symbol.name == name ]

def get_var_type(table, var):
    if is_number(var): return 'number'
    if is_string(var): return 'string'
    found = lookup_identifier(table, var)
    if found: return found[0][0].typ              # Because found here is a list containing 1 symbol
    return None

def __insert(table, name, type):
    if not is_valid_identifier(name) or not is_valid_type(type):
        raise InvalidInstruction(f"INSERT {name} {type}")
    
    if any(name == symbol.name for symbol in table[-1]):
        raise Redeclared(f"INSERT {name} {type}")
    
    newSymbol = Symbol(name, type)
    return table[:-1] + [table[-1] + [newSymbol]]

def __assign(table, name, val):
    if not is_valid_identifier(name) or not (is_valid_identifier(val) or is_string(val) or is_number(val)):
        raise InvalidInstruction(f"ASSIGN {name} {val}")
    
    symbol_type = get_var_type(table, name)
    val_type = get_var_type(table, val)

    if not symbol_type or not val_type:
        raise Undeclared(f"ASSIGN {name} {val}")

    if symbol_type == val_type:
        return "success"
    else:
        raise TypeMismatch(f"ASSIGN {name} {val}")
        
def __begin(table):
    return table[0:] + [[]]

def __end(table):
    if(len(table) == 1):
        raise UnknownBlock()
    return table[:-1]

def __lookup(table, name):
    if not is_valid_identifier(name):
        raise InvalidInstruction(f"LOOKUP {name}")

    found = lookup_identifier(table, name)
    if not found:
        raise Undeclared(f"LOOKUP {name}")
    return f"{found[0][1]}"

############################ ĐÃ SỬA TỪ TRÊN XUỐNG TỚI ĐÂY #############################
def __print(table):
    result = __rprint(table, [])
    if result == "":
        return result
    parts = result.split()
    return " ".join(reversed(parts))

def __rprint(table, seen_name):
    if(len(table) == 0):
        return ""
    if(len(table[-1]) == 0):
        return __rprint(table[:-1], seen_name)
    if table[-1][-1].name in seen_name: 
        return __rprint(table[:-1] + [table[-1][:-1]], seen_name)

    new_seen_name = seen_name + [table[-1][-1].name]
    result = f"{table[-1][-1].name}//{len(table) - 1}"
    call_result = __rprint(table[:-1] + [table[-1][:-1]], new_seen_name)

    if call_result != "":
        return result + " " + call_result
    else:
        return result 

############################ ĐÃ SỬA TỪ DƯỚI LÊN TỚI ĐÂY #############################
def process_command(table, command):

    #### From here
    if command != command.strip() or "  " in command:
        raise InvalidInstruction(command)

    tokens = command.split(" ")
    op = tokens[0]
    args = tokens[1:]
    # To here, check the correctness of the code


    if op == "INSERT" and len(args) == 2:
        return __insert(table, args[0], args[1]), "success"
    elif op == "ASSIGN" and len(args) == 2:
        return table, __assign(table, args[0], args[1])
    elif op == "BEGIN" and not args:
        return __begin(table), None
    elif op == "END" and not args:
        return __end(table), None
    elif op == "LOOKUP" and len(args) == 1:
        return table, __lookup(table, args[0])
    elif op == "PRINT" and not args:
        return table, __print(table)
    elif op == "RPRINT" and not args:
        return table, __rprint(table, [])
    else:
        raise InvalidInstruction(command)

def process_all(list_of_commands):
    def helper(table, list_out, cmds):
        if not cmds:
            if len(table) != 1:
                raise UnclosedBlock(len(table) - 1)
            return list_out
        else:# try:
            new_table, output = process_command(table, cmds[0])
            new_list_out = list_out + ([output] if output else ([""] if output == "" else []))
            return helper(new_table, new_list_out, cmds[1:])
        # except StaticError as e:
        #     raise type(e)(cmds[0])
    return helper([[]], [], list_of_commands)



def simulate(list_of_commands):
    """
    Executes a list of commands and processes them sequentially.

    Args:
        list_of_commands (list[str]): A list of commands to be executed.

    Returns:
        list[str]: A list of return messages corresponding to each command.
    """


    return process_all(list_of_commands)

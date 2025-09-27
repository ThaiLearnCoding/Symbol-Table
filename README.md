# Symbol-Table
Advanced Programming Assigment - Semester 242

# Symbol Table Implementation

## Project Overview 📄

This project implements a **Symbol Table** system for a programming language compiler/interpreter. A symbol table is a crucial data structure used in programming language implementations to track variable declarations, their types, and scope information during static analysis and compilation.

## Purpose 🎯

The primary purpose of this project is to:

1. **Variable Management**: Track variable declarations and their associated data types (`number` and `string`)
2. **Scope Management**: Handle nested scopes using `BEGIN` and `END` blocks
3. **Static Error Detection**: Identify common programming errors at compile-time:
   - Redeclared variables
   - Undeclared variables 
   - Type mismatches
   - Invalid instructions
   - Unclosed blocks Missing

4. **Variable Assignment**: Support assignment operations with type checking
5. **Symbol Lookup**: Efficiently find variables across different scope levels
6. **Symbol Table Printing**: Display the current state of the symbol table with scope information

## Architecture Design 👨‍💻

The symbol table uses a **nested list structure** to represent scopes:

```
Initially: [[]]
When adding variables:
    INSERT x        -> [[x]]
    INSERT y        -> [[x, y]]
    BEGIN           -> [[x, y], []]
        INSERT x    -> [[x, y], [x]]      # Variable shadowing allowed
        BEGIN       -> [[x, y], [x], []]
            INSERT m -> [[x, y], [x], [m]]
        END         -> [[x, y], [x]]
        INSERT z    -> [[x, y], [x, z]]
    END             -> [[x, y]]
```

- Each inner list represents a scope level
- The outermost list is the global scope
- Inner lists represent nested block scopes
- Index position indicates the scope level for variable lookup

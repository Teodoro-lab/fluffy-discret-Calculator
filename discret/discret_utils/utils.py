def binary(num, binString=""):
    """Bin() == bin() => can be use as an alternative to python bin function"""
    mod = num%2
    binString += str(mod)
    if num == 0:
        return("0")  
    elif num == 1:
        return("0b"+binString[::-1]) 
    num = num//2 
    return(binary(num, binString)) 


"""************************************************************
         ---------------- Karnaugh functions------------------
************************************************************"""

def pattern(num):
    """Generates the pattern of index changes in the [0]-matrix to optain
    the karnaugh order_values in a KarnaughMap

    Parameter: Recibes 2**num number(depends on the number of variables)"""
  
    if num == 1:
        return [1]
    return pattern(num-1)+[num]+pattern(num-1)


def karnaugh_Matrix(num):
    """Creates a matrix containing the 0's & 1's combinations following the
        one-number-change rule in KarnaughMaps

        Parameter: Recibes a 2**var number(depends on the number of variables)"""
    
    indexChg = pattern(num)
    karnaughOrder = []
    matrix = [0]*num
    karnaughOrder.append(matrix.copy())
    for i in indexChg:
        if matrix[-i] == 0:
            matrix[-i] = 1
            karnaughOrder.append(matrix.copy())
        else:
            matrix[-i] = 0
            karnaughOrder.append(matrix.copy())
    return karnaughOrder
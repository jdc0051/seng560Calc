import math

def add(var1, var2):
    try:
        if type(var1) == str or type(var2) == str:
            print("Invalid Parameters.  Parameters must be integer or float values")
            return None
        else:
            return var1 + var2
    except:
        print("Invalid Parameters.  Parameters must be integer or float values")
    
def subtract(var1, var2):
    try:
        if type(var1) == str or type(var2) == str:
            print("Invalid Parameters.  Parameters must be integer or float values")
            return None
        else:
            return var1 - var2
    except:
        print("Invalid Parameters.  Parameters must be integer or float values")
    
def multiply(var1, var2):
    try:
        if type(var1) == str or type(var2) == str:
            print("Invalid Parameters.  Parameters must be integer or float values")
            return None
        else:
            return var1 * var2
    except:
        print("Invalid Parameters.  Parameters must be integer or float values")
    
def divide(var1, var2):
    try:
        if type(var1) == str or type(var2) == str:
            print("Invalid Parameters.  Parameters must be integer or float values")
            return None
        else:
            return var1 / var2
    except:
        print("Invalid Parameters.  Parameters must be integer or float values")
    
def squareroot(var1):
    try:
        if type(var1) == str:
            print("Invalid Parameters.  Parameters must be integer or float values")
            return None
        else:
            return math.sqrt(var1)
    except:
        print("Invalid Parameters.  Parameters must be integer or float values")
    
def exponent(var1, var2):
    try:
        if type(var1) == str or type(var2) == str:
            print("Invalid Parameters.  Parameters must be integer or float values")
            return None
        else:
            return var1 ** var2
    except:
        print("Invalid Parameters.  Parameters must be integer or float values")
    
def convertToInt(var1):
    try:
        dataType = type(var1)
        if dataType == float:
            return int(var1)
        elif dataType == str:
            if var1[0:2] == '0x' or var1[0:2] == '0X':
                return int(var1, 16)
            elif var1[0:2] == '0o' or var1[0:2] == '0O':
                return int(var1, 8)
            elif var1[0:2] == '0b' or var1[0:2] == '0B':
                return int(var1, 2)
            else:
                print("Invalid parameters.  Parameters must be Integer, Hex, Octal, or Binary values in either integer or string format")
                return None
        else:
            return var1
    except:
        print("Invalid parameters.  Parameters must be Integer, Hex, Octal, or Binary values in either integer or string format")
    
def convertToHex(var1):
    try:
        dataType = type(var1)
        if dataType == float:
            print('Float to Hex not supported')
            return None
        elif dataType == str:
            if var1[0:2] == '0o' or var1[0:2] == '0O':
                temp = int(var1, 8)
                return hex(temp)
            elif var1[0:2] == '0b' or var1[0:2] == '0B':
                temp = int(var1, 2)
                return hex(temp)
            else:
                print("Invalid parameters.  Parameters must be Integer, Hex, Octal, or Binary values in either integer or string format")
                return None
        else:
            return hex(var1)
    except:
        print("Invalid parameters.  Parameters must be Integer, Hex, Octal, or Binary values in either integer or string format")
    
    
def convertToOct(var1):
    try:
        dataType = type(var1)
        if dataType == float:
            print('Float to Oct not supported')
            return None
        elif dataType == str:
            if var1[0:2] == '0x' or var1[0:2] == '0X':
                temp = int(var1, 16)
                return oct(temp)
            elif var1[0:2] == '0b' or var1[0:2] == '0B':
                temp = int(var1, 2)
                return oct(temp)
            else:
                print("Invalid parameters.  Parameters must be Integer, Hex, Octal, or Binary values in either integer or string format")
                return None
        else:
            return oct(var1)
    except:
        print("Invalid parameters.  Parameters must be Integer, Hex, Octal, or Binary values in either integer or string format")
    
    
def convertToBin(var1):
    try:
        dataType = type(var1)
        if dataType == float:
            print('Float to Bin not supported')
            return None
        elif dataType == str:
            if var1[0:2] == '0x' or var1[0:2] == '0X':
                temp = int(var1, 16)
                return bin(temp)
            elif var1[0:2] == '0o' or var1[0:2] == '0O':
                temp = int(var1, 8)
                return bin(temp)
            else:
                print("Invalid parameters.  Parameters must be Integer, Hex, Octal, or Binary values in either integer or string format")
                return None
        else:
            return bin(var1)
    except:
        print("Invalid parameters.  Parameters must be Integer, Hex, Octal, or Binary values in either integer or string format")
    

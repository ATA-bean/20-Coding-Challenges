def denary_to_binary(denary_input : int) -> int:

    binary_place_values = []
    binary_output = ""

    count = 0
    while count < 8:
        place_value = (2 ** (8 - (count + 1)))
        binary_place_values.insert(count,place_value)

        if (denary_input - place_value) >= 0:
            binary_output += "1"
            denary_input -= place_value
        else:
            binary_output += "0"

        count += 1
    
    
    return int(binary_output)
def binary_to_hex(binary_input : int) -> str:
    binary_input = str(binary_input)

    hex_table = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"] 
    
    hex_output = [] 
    length = len(hex_output)
    hex_number = ""
    
    count = 0
    index = 0 
    for letter in binary_input:
        bin_count = 2 ** (4 - (count + 1))
        hex_output.insert(index,int(letter) * bin_count)
        if count > 2:
            count = 0
        else:
            count += 1
        index += 1
    
    count = 0
    hex_numberp1 = 0
    hex_numberp2 = 0
    for length in hex_output:
        if count > 3:
            hex_numberp2 += hex_output[count-1]
        else:
            hex_numberp1 += hex_output[count-1]
        count += 1
    
    hex_numberp1 = str(hex_table[hex_numberp1])
    hex_numberp2 = str(hex_table[hex_numberp2])
    hex_number = hex_numberp1 + hex_numberp2

    return hex_number
def hex_to_denary(hex_input : str) -> int:
    
    denary_output = 0

    input_length = len(hex_input)
    hex_table = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

    while input_length > 0:
        place_value = 16 ** ((len(hex_input)) - input_length)
        
        hex_code = hex_input[input_length - 1]
        denary_output += hex_table.index(hex_code) * place_value
        
        input_length -= 1

    return denary_output

def denary_to_hex(denary_input : int) -> str:
    hex_output = binary_to_hex(denary_to_binary(denary_input))
    return hex_output
def hex_to_binary(denary_input : int) -> int:
    binary_output = denary_to_binary(hex_to_denary(denary_input))
    return binary_output
def binary_to_denary(binary_input : int) -> int:
    denary_output = hex_to_denary(binary_to_hex(binary_input))
    return denary_output


print(denary_to_binary(255))
print(binary_to_hex(11111111))
print(hex_to_denary("FF"))

print(denary_to_hex(255))
print(hex_to_binary("FF"))
print(binary_to_denary(11111111))

def check_measurement_prefix(measurement : str):
    
    def check_prefix_specified_length(measurement : str , prefix_length : int):
        prefix_4 = {
            "giga" : 10**9,
            "mega" : 10**6,
            "kilo" : 10**3,
            "nano" : 10**-9,
        }
        prefix_5 = {
            "centi" : 10**-2,
            "milli" : 10**-3,
            "micro" : 10**-6
        }

        measurement = measurement.lower().strip()
        measurement_prefix = measurement[0:prefix_length]
        measurement = measurement.replace(measurement_prefix,"")
        
        prefix_dict = {}
        if prefix_length == 4:
            prefix_dict = prefix_4
        elif prefix_length == 5:
            prefix_dict = prefix_5

        try:
            multiplier = prefix_dict[measurement_prefix]
            return multiplier
        except KeyError:
            return None
    
    prefix_found_value = (
        check_prefix_specified_length(measurement, 4) or 
        check_prefix_specified_length(measurement, 5)
    )

    if prefix_found_value == None:
        prefix_found_value = 1

    return prefix_found_value

def take_user_inputs():
    print("Welcome to the Unit Converter")

    print("What unit are you converting FROM:")
    measurement_from = input("")

    print("What unit are you converting TO:")
    measurement_to = input("")

    print(f"What is the amount of {measurement_from} are you converting")
    value_to_convert = float(input(""))

    return [measurement_from,measurement_to,value_to_convert]

def convert_value(conversion_data : list):
    value_to_convert = conversion_data[2]

    measurement_from = check_measurement_prefix(conversion_data[0])
    measurement_to = check_measurement_prefix(conversion_data[1])
    conversion_multiplier = measurement_from / measurement_to

    converted_value = value_to_convert * conversion_multiplier
    converted_value = str(converted_value)

    output = converted_value + " " + conversion_data[1] + "s"

    return output

def measurement_convertor():
    user_input = take_user_inputs()
    print(convert_value(user_input))

measurement_convertor()
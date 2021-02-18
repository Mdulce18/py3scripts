#  Go trought a list containing dicctionaries from a json
list_of_dic = response['json']['2']['something']  # list with dictionaries
            for dictionaries in list_of_dic:
                for key, value in dicionaries.items():
                    value_in_string = str(value)  # use the value searched
                    if 'ABC' in value_in_string:
                        abc_string_to_list = value_in_string.split()
                        for a in abc_string_to_list:
                            do something

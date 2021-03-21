# Original code
def most_repeated_letter(string):
    string_list = []
    for element in string:
        string_list.append(element.lower())
    most_repeated = max(set(string_list), key = string_list.count) 
    return most_repeated

# Update of code
def most_repeated_letter_new(string):
    string_list = list(string.lower())
    most_repeated = max(set(string_list), key = string_list.count) 
    return most_repeated

print(most_repeated_letter("anueeeel"))

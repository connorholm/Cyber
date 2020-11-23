#WordIndex.py
#Name:
#Date:
#Assignment:

def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value

def main():
    textFile = open("/Users/90305163/Developer/Cyber/Lab6-master/fish.txt", 'r')
    words = {}
    document = []
    lineIndex = 1
    for line in textFile:
        document.append(line.split())
    for line in document:
        for word in line:
            append_value(words, word, lineIndex)
        lineIndex = lineIndex + 1
     #create an empty dictionary

    print ("fish" in words) #is a word already in the dictionary?
    words["fish"] = [2]     #add a list to the dictionary
    print ("fish" in words) #is the word there now?
    words["fish"].append(5) #add to an existing list
    print(words)


main()

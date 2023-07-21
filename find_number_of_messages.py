from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    main = 0
    f = data["messages"]
    for i in f:
        if i["type"]== "message":
            main += 1 


    return main

data=read_data("data/result.json")

print(find_number_of_messages(data))
import json
def read_data(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    #open file
    data=open(file_path,encoding="UTF-8").read()
    return json.loads(data)

#print(read_data('data/result.json'))
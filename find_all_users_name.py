from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    a = []
    for row in data('message'):
        if msg['type'] == 'message':
            if msg['from'] not in name_list:
                if msg ['fron_id'].startswith('user'):
                    name_list.append(msg['from'])
        if msg ['type'] == 'service':
            if msg['actor'] not in name_list:
                if msg['actor_id'].startswith('user'):
                    name_list.append(msg['actor'])


    return name_list 

data = read_data('data/result.json')
print(find_all_users_name(data))

"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    
    species = set()
    data = open(filename)
    for line in data:
        sp = line.split("|")[1]
        species.add(sp)

    

    # TODO: replace this with your code

    return species
# print(all_species("villagers.csv"))

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    villagers = []
    data = open(filename)
    for line in data:
        name, species = line.split("|")[:2]
        if search_string in ("All", species):
            villagers.append(name)
    

    

    # TODO: replace this with your code

    return sorted(villagers)

#print(get_villagers_by_species("villagers.csv", "All"))
#print("----------------------------------------------")
#print(get_villagers_by_species("villagers.csv", "Bear"))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    
    all_names = [[],[],[],[],[],[]]
    hob_list = ['Fitness', 'Nature', 'Education', 'Music', 'Fashion', 'Play']
    
    data = open(filename)
    for line in data:
        name, _, _, hobby = line.split("|")[0 : 4]
        for index, item in enumerate(hob_list):
            if hobby == item:
                all_names[index].append(name)
        
    for i in range(len(all_names)):
        all_names[i].sort()
    
    
    return all_names

 



def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    data = open(filename)
    for line in data:
        all_data.append(tuple(line.rstrip().split("|")))
    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    data = open(filename)
    for line in data:
        name, _, _, _, motto = line.rstrip().split("|")
        if name == villager_name:
            return motto
    
    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    villagers_like = set()
    target_personality = None
    data = open(filename)
    for line in data:
        name, _, personality = line.rstrip().split("|")[:3]
        if name == villager_name:
            target_personality = personality
            break
    

    if target_personality:
        
        for villager_data in all_data(filename):
            if villager_data[2] == target_personality:
                villagers_like.add(villager_data[0])

    
    return villagers_like



    # TODO: replace this with your code

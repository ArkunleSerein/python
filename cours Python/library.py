def oui_non(value):
    if value:
        return 'oui'
    else:
        return 'non'
    
def reverse_lookup(my_list, value):
    """ cette fonction prend en paramètre une liste est une valeur à rechercher. Elle renvoie l'index de la valeur si elle est trouvée ou None si la valeur n'est pas trouvée.
     
      my_list list la list dans laquelle il faut chercher
      value any la valeur à rechercher
      return int si la valeur est trouvée ou None si la valeur n'est pas trouvée 
    """
    for i in range(len(my_list)):
        if my_list[i] == value:
            #@dev
            #print(f'{i = }')
            return i
        
    return None
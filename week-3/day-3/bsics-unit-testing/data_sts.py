'''
    - create a list which can contain numbers, strings and booleans
    - square each element of tuple 
    - add new element to tuple of strings
    - sort the values of dictionary by descending order
'''


class DataManipulation:

    def list_of_elements(self, *args):
        valid_types = [str, bool, int, float]

        lst = [*args]
        for itm in lst:
            if type(itm) not in valid_types:
                return None

        return lst

    def square_each_tuple(self,*args):
        lst=[*args]
        return tuple(i**2 for i in lst)

    def add_new_element_tuple(self,*args,**kwargs):
        lst=[*args]
        lt=kwargs.get('lt')
        lst.append(lt)
        return(tuple(lst))
    def sort_dec_dict(self,dt):
        if type(dt)!=dict:
            return None
        lst=[*dt.values()]
        res=sorted(lst,reverse=True)
        return res
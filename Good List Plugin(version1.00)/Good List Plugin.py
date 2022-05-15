'''This is version 1.00 of the Good List Plugin, made by BilibiliFeipi, which makes it easier for you to
use lists and increases productivity. If you like you can go to GitHub to subscribe to this plugin, thanks
for using it'''

class two_dim():
    def tra(list,target,list_indx=''):
        if type(list_indx) == 'str':
            for x in list:
                if x == target:
                    return x
        elif type(list_indx) == 'int':
            for x in list[list_indx]:
                if x == target:
                    return x
    def retn_list(list,index):
        List = list[index]

class one_dim():
    def tra(list,target):
        for x in list:
            if x == target:
                return x
    
    def indx_str(list,index):
        Str = list[index]
        return Str
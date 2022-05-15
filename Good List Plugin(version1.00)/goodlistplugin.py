'''This is version 1.00 of the Good List Plugin, made by BilibiliFeipi, which makes it easier for you to
use lists and increases productivity. If you like you can go to GitHub to subscribe to this plugin, thanks
for using it'''

class two_dim():
    def tra(list,target,self,list_indx=''):
        a=0
        if type(list_indx) == 'str':
            for x in list:
                if x == target:
                    return x
        elif type(list_indx) == 'int':
            for x in list[list_indx]:
                if x == target:
                    return x,a
                a+=1
    def retn_list(self,list,index):
        List = list[index]

class one_dim():
    def tra(self,list,target):
        a=0
        for x in list:
            if x == target:
                return x,a
        a+=1
    
    def indx_str(self,list,index):
        Str = list[index]
        return Str
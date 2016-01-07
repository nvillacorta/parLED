class Mapping(dict):
    def __setitem__(self, key, item): 
        self.__dict__[key] = item
    
    def __getitem__(self, key): 
        return self.__dict__[key]
    
    def __repr__(self): 
        return repr(self.__dict__)
    
    def __len__(self): 
        return len(self.__dict__)
    
    def __delitem__(self, key): 
        del self.__dict__[key]
    
    def clear(self):
        return self.__dict__.clear()
    
    def copy(self):
        return self.__dict__.copy()
    
    def has_key(self, k):
        return self.__dict__.has_key(k)
    
    def pop(self, k, d=None):
        return self.__dict__.pop(k, d)
    
    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)
    
    def keys(self):
        return self.__dict__.keys()
    
    def values(self):
        return self.__dict__.values()
    
    def items(self):
        return self.__dict__.items()
    
    def pop(self, *args):
        return self.__dict__.pop(*args)
    
    def __cmp__(self, dict):
        return cmp(self.__dict__, dict)
    
    def __contains__(self, item):
        return item in self.__dict__
    
    def __iter__(self):
        return iter(self.__dict__)
    
    def __unicode__(self):
        return unicode(repr(self.__dict__))

class colors(Mapping):
    def __init__(self):
        self.red = (255,0,0)
        self.blue = (0,0,255)
        self.green = (0,255,0)
        self.cyan = (0,255,255)
        self.magenta = (255,0,255)
        self.yellow = (255,255,0)
        self.white = (255,255,255)
        self.black = (0,0,0)

Colors = colors()

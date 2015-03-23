from google.appengine.api import users
from google.appengine.ext import ndb

class Cooker(ndb.Model):
    cooker_id = ndb.StringProperty(indexed=True)
    
    constant = ndb.FloatProperty()
    p_value = ndb.FloatProperty()
    
    current_temp = ndb.FloatProperty()
    target_temp = ndb.FloatProperty()
    
    current_output = ndb.ComputedProperty(lambda self:self._CalcOutput())

    def _CalcOutput(self):
        temp_diff = self.target_temp - self.current_temp
        if temp_diff < 0:
            return 0
        return min(1,self.constant+self.p_value*temp_diff)

class HistoryEntry(ndb.Model):
    cooker_id = ndb.StringProperty(indexed=True)
    
    target_temp = ndb.FloatProperty()
    current_temp = ndb.FloatProperty()
    error = ndb.ComputedProperty(lambda self: self.target_temp-self.current_temp)
    
    constant = ndb.FloatProperty()
    p_value = ndb.FloatProperty()
    output = ndb.FloatProperty()

    time = ndb.DateTimeProperty(auto_now_add=True)

class BaseValues(ndb.Model):
    constant = ndb.FloatProperty()
    p_value = ndb.FloatProperty()

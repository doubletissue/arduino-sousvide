import models

_DEFAULT_CONSTANT = .4
_DEFAULT_P_VALUE = (1-_DEFAULT_CONSTANT)/5.0 # Off by 5 degrees gets full power
_DEFAULT_TARGET = 130

def GetBaseValues():
    base_vals = models.BaseValues.query().fetch(1)
    if base_vals:
        base_vals_instance = base_vals[0]
        return base_vals_instance.constant, base_vals_instance.p_value
    base_vals_instance = models.BaseValues(constant=_DEFAULT_CONSTANT, p_value=_DEFAULT_P_VALUE)
    base_vals_instance.put()
    return base_vals_instance.constant, base_vals_instance.p_value

def GetCooker(cooker_id):
    cooker = models.Cooker.query().filter(models.Cooker.cooker_id==cooker_id).fetch(1)
    if cooker:
        return cooker[0]
    constant, p_value = GetBaseValues()
    cooker = models.Cooker(cooker_id=cooker_id,
                           constant=constant,
                           p_value=p_value,
                           current_temp=0,
                           target_temp=_DEFAULT_TARGET)
    return cooker
    
def AddHistoryPoint(cooker):
    data_point = models.HistoryEntry(
        cooker_id=cooker.cooker_id,
        target_temp=cooker.target_temp,
        current_temp=cooker.current_temp,
        constant=cooker.constant,
        p_value=cooker.p_value,
        output=cooker.current_output)
    data_point.put()

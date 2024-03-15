
def water_column_height(tower_height, tank_height):
    
    height= tower_height+(3*tank_height)/4
    return height

def pressure_gain_from_water_height(height):

    pressure=(998.2*9.80665*height)/1000
    return pressure
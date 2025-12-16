km_to_m = lambda km : km* 1000
m_to_cm = lambda m : m * 100            
cm_to_mm = lambda cm : cm * 10
feet_to_inches = lambda feet : feet * 12
inches_to_cm = lambda inches : inches * 2.54

distance = float(input("Enter the distance: "))

def distance_converter(dist, conversiontype, conversionfun):
    result = conversionfun(dist)
    from_unit , to = conversiontype.split(' to ')
    print(distance, from_unit, "=",result,to)
distance_converter(distance, "km to m", km_to_m)
distance_converter(distance, "m to cm", m_to_cm)
distance_converter(distance, "cm to mm", cm_to_mm)      
distance_converter(distance, "feet to inches", feet_to_inches)
distance_converter(distance, "inches to cm", inches_to_cm)

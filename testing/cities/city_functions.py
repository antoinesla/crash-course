def get_formatted_city_name(city, country, population=0):
    '''returns nicely formatted city and country string'''
    formatted_string = f'{city}, {country}'.title()
    if population != 0:
         formatted_string += f' - population {population}'
    return formatted_string
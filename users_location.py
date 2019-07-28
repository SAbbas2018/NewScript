import geocoder 

#Global 
location = geocoder.ip('me')

#get the users lcoation through ip address
def get_users_location():
    """
    get the users location through their ip address
    and then return the city, province/state, and latlng coordinates
    in a list 
    """
    city = location.city
    province = location.province
    latlng = location.latlng
    country = location.country
    #return a list containing the city's name, province/state, and the lat and long as
    #separate entries and as strings 
    list_to_return = [city, province, str(latlng[0]), str(latlng[1]), country]
    return list_to_return

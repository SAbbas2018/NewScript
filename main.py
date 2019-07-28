import displaydateandtime
import users_location
import ShowWeather
import os
import news 

class User:
    def __init__(self, name, city, lat, lon, country):
        """
        #intialize a user object
        """
        self._name = name 
        self._city = city
        self._lat = lat
        self._lon = lon
        self._count = country


def NewUser(): 
    """
    Intialize a new user and set them up
    """
    #take in the users name and display an introduction and the current date and time 
    username = input("Please enter your name: ")

    while not username.isalpha():
        print("Error, name entered is not alphabetic!")
        username = input("Please enter your name: ")
    print()
    
    intro = ("Hello {}, Welcome to Starlight: Newscript").format(username.capitalize())
    print(intro)
    displaydateandtime.show_date()
    displaydateandtime.show_time()

    #get the users location use geolocation 
    #its a list containing the following [city, pro, lat, lng, count]
    location_list = users_location.get_users_location()
    
    #open a new file in write mode to write the usersname and home location 
    new_file = open("user_data_file.txt", "w")
    new_file.write(username.capitalize() + "\n")
    for i in range(len(location_list)):
        new_file.write(location_list[i] + "\n")
    new_file.close()

    #fill in user object
    current_user = User(username.capitalize(), location_list[0], location_list[2], location_list[3], location_list[4])

    return current_user 

def ReturningUser():
    """
    Say hello to a returning user and load up their info from the text file
    """
    user_data = []

    #open and read in the file
    userdatafile = open("user_data_file.txt", "r")
    for line in userdatafile:
        user_data.append(line.rstrip())
    #user_data will be list of format username, city, province, lat, long
    username = user_data[0]
    user_city = user_data[1]
    lat = user_data[3]
    lon = user_data[4]
    count = user_data[5]
    
    #display intro
    print(("Welcome back, {}").format(username))
    displaydateandtime.show_date()
    displaydateandtime.show_time()

    #fill in user object 
    current_user = User(username, user_city, lat, lon, count)
    return current_user



if __name__ == "__main__":
    #check if data file exists 
    exists = os.path.isfile('user_data_file.txt')
    if exists:
        current_user = ReturningUser()
    else:
        current_user = NewUser()

    print()
    #show weather 
    ShowWeather.show_weather(current_user)
    news.News(current_user)


    print('Thank you for using Starlight - By Raza Abbas')
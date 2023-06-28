#!/bin/python3
import requests
import os


print ("""/        |                                                              /  |                                         /      \ /  |                          /  |      
$$$$$$$$/______   _____  ____    ______    ______    ______   ______   _$$ |_    __    __   ______    ______        /$$$$$$  |$$ |____    ______    _______ $$ |   __ 
   $$ | /      \ /     \/    \  /      \  /      \  /      \ /      \ / $$   |  /  |  /  | /      \  /      \       $$ |  $$/ $$      \  /      \  /       |$$ |  /  |
   $$ |/$$$$$$  |$$$$$$ $$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$/   $$ |  $$ |/$$$$$$  |/$$$$$$  |      $$ |      $$$$$$$  |/$$$$$$  |/$$$$$$$/ $$ |_/$$/ 
   $$ |$$    $$ |$$ | $$ | $$ |$$ |  $$ |$$    $$ |$$ |  $$/ /    $$ |  $$ | __ $$ |  $$ |$$ |  $$/ $$    $$ |      $$ |   __ $$ |  $$ |$$    $$ |$$ |      $$   $$<  
   $$ |$$$$$$$$/ $$ | $$ | $$ |$$ |__$$ |$$$$$$$$/ $$ |     /$$$$$$$ |  $$ |/  |$$ \__$$ |$$ |      $$$$$$$$/       $$ \__/  |$$ |  $$ |$$$$$$$$/ $$ \_____ $$$$$$  \ 
   $$ |$$       |$$ | $$ | $$ |$$    $$/ $$       |$$ |     $$    $$ |  $$  $$/ $$    $$/ $$ |      $$       |      $$    $$/ $$ |  $$ |$$       |$$       |$$ | $$  |
   $$/  $$$$$$$/ $$/  $$/  $$/ $$$$$$$/   $$$$$$$/ $$/       $$$$$$$/    $$$$/   $$$$$$/  $$/        $$$$$$$/        $$$$$$/  $$/   $$/  $$$$$$$/  $$$$$$$/ $$/   $$/ 
                               $$ |                                                                                                                                   
                               $$ |                                                                                                                                   
                               $$/                                                                                                                                    """)




api_key = "" ##Add your API Key here from https://openweathermap.org/ 
api_url = "https://api.openweathermap.org/data/2.5/weather"


while True:
    location = input("\n\nWhere would you like to know the current temperature of?  \n")
    
    response = requests.get(
        url = api_url,
        params = {
            "q": location,
            "appid": api_key,
            "units": "metric",
        }
    )

    weather_data = response.json()['main']['temp']
    print (f"\n\nThe Temperature in {location} is currently {weather_data} Degrees Celcius")
    
    while True:
        choice = ""
        choice = input("\n\nDo you want to know about somewhere else? Y or N\n")
        if choice == "N":
            exit()
        elif choice == "Y":
            break
        elif choice != "Y" or "N":
            print("Please type either Y or N")
            pass
            
        

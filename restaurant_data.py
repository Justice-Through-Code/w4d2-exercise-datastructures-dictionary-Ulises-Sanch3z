
'''
    Below is a dictionary consisting of details of 1 restaurant fetched from Yelp.
'''

restaurant_1 = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "state": "CA",
    "address": "375 Valencia St",
    "zip_code": "94113",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}


def explore_data():
    # 1.1 TODO: Print the URL of the website of Four Barrel Coffee.

    # 1.2 TODO: Print the latitude and longitude of Four Barrel Coffee, using one print statement.

    # 1.3 TODO: Print the complete address of the Four Barrel Coffee, formatted as a string - 
    # it should include the address, city, state and the zip code, with commas between them e.g.:
    # "375 Valencia St, San Francisco, CA, 94113"


def favorite_restaurant():
    # Let's ask the user for some information about their favorite restaurant

    # 2.1 TODO: Create an empty dictionary in a variable called `favorite_restaurant`

    # 2.2 TODO: Ask the user for the restaurant `name`, `address`, and their `favorite_dish`
    # Add all three of these as key value pairs in your new dictionary, ala:
    #    favorite_restaurant  = {
    #        "name": "Subway",
    #        "address" : "116th & Broadway, NY 10016",
    #        "favorite_dish" : "Chicken BLT Sandwich"
    #    }

    # 2.3 TODO: Print out your dictionary to make sure it populated correctly

    # Oh no, the restaurant stopped serving the user's favorite dish!
    # 2.4 TODO: Remove the `favorite_dish` key/value pair from the dictionary

    # 2.5 TODO: Print out the dictionary again. This time, the dictionary 
    # should only contain a 'name' and 'address' for that restaurant

    # Looks like the restaurant is going through a lot of changes-- they moved!
    # 2.6 TODO: Update the address of the user's favorite restaurant to "116th & Broadway, NY 10016"

    # 2.7 TODO: Print out the restaurant's new address by printing the dictionary's value 
    # for the key `address`


def clean_print():
    # It's hard to read the contents of a dictionary when we print the whole thing out.

    # 3.1 TODO: Instead, loop through each item-pair in the `restaurant_1` dictionary
    # and print out each key and value on their own line, ala:
    #      `name: Four Barrel Coffee
    #       url: https://www.yelp.com/biz/four-barrel-coffee-san-francisco`
    # etc etc

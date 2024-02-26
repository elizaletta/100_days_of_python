#nesting dictionaries
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#nesting a list in a dictionary
travel_log1 = {
    "France": ["Paris", "Lilion"],
    "Belarus": ["Minsk", "Baranovichi", "Grodno"],
}

#nesting a dictionary in a dictionary
travel_log = {
    "France": ["Paris", "Lilion"],
    "Belarus": {"Minsk": "Lived there",
                "Baranovichi": "Also lived there, but in childhood",
                "Grodno": "Visited more than 10 times, my favourite city",
    }
}


travel_log = {
    "France": ["Paris", "Lilion"],
    "Belarus": {"Cities visited": ["Minsk", "Baranovichi", "Grodno"],
                "Total number of visits": 20,
                },
}

#nesting dictionary in a list
travel_log2 = [
    {"Country": "Belarus",
     "Cities visited": ["Minsk", "Baranovichi", "Hrodno"],
     "Total visits": 20,
     },
    {"Country": "Poland",
     "Cities visited": ["Warsaw", "Krakow", "Gdansk"],
     "Total visits": 5,
     }
]
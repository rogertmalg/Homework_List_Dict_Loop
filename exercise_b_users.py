users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users.get("Jonathan").get("twitter"))
# 2. Get Erik's hometown
print(users.get("Erik").get("home_town"))
# 3. Get the array of Erik's lottery numbers
print(users.get("Erik").get("lottery_numbers"))
# 4. Get the species of Avril's pet Monty
print(users.get("Avril").get("pets")[0].get("species"))
# 5. Get the smallest of Erik's lottery numbers
users.get("Erik").get("lottery_numbers").sort()
print(users.get("Erik").get("lottery_numbers")[0])
# 6. Return an array of Avril's lottery numbers that are even
even_numbers = []
for number in users.get("Avril").get("lottery_numbers"):
      if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users.get("Erik").get("lottery_numbers").append(7)
# 8. Change Erik's hometown to Edinburgh
users.get("Erik")["home_town"] = "Edinburgh"
# 9. Add a pet dog to Erik called "Fluffy"
users.get("Erik").get("pets").append({"name" : "Fluffy", "species" : "dog"})
# 10. Add another person to the users dictionary
users["Roger"] = {
  "twitter" : "rogertmalg",
  "lottery_numbers" : [3, 14, 19, 28, 35, 44],
  "home_town" : "Rio de Janeiro",
  "pets" : [
    {
      "name" : "Aslam",
      "species" : "dog" 
    }
  ]
}
print(users)
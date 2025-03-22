import json

info_about_me = {
    "name": "Michele",
    "has_a_dog": False
}

with open("info.json", "w") as f:
    json.dump(info_about_me, f)
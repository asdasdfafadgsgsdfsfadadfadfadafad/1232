from pynput.mouse import Button , Controller
import requests
def getcoords():
    points = (requests.get("https://shrouded-springs-42410.herokuapp.com").text)
    return [int(x) for x in points.split(",")]

def update(value):
  requests.post("https://shrouded-springs-42410.herokuapp.com/update",json={"coords": value})



update("24,3513")
print(getcoords())





import pyrebase
from users import User, Users
from trash_bin import TrashBin, TrashBins

config = {
  "databaseURL":"https://minka-3763e-default-rtdb.europe-west1.firebasedatabase.app/",
  "apiKey": "AIzaSyDMCiTQo-F0nilEce15yNy3jhnFFDryQVo",
  "authDomain": "minka-3763e.firebaseapp.com",
  "projectId": "minka-3763e",
  "storageBucket": "minka-3763e.appspot.com",
  "messagingSenderId": "1044868675427",
  "appId": "1:1044868675427:web:589b69381ed04b398e4556",
  "measurementId": "G-E3HYRB08DT"
}


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()


def set_user_data(user):
  # sets user data; if user not exist, create user
  id = user.id()
  name = user.name()
  surname = user.surname()
  password = user.password()
  score = user.score()
  db.child("users").child(id).set({"name": name, "surname": surname, "password": password, "score": score})


def update_user_particular_data(id, key, newValue):
  # if key not exist, create new key
  db.child("users").child(id).update({key: newValue})


def remove_user_data(id):
  # removes data
  db.child("users").child(id).remove()


def list_of_users():
  list_of_users = []
  all_users = db.child("users").get()
  try:
    for users in all_users.each()[1:]:
      id = users.key()
      name = users.val()["name"]
      surname = users.val()["surname"]
      password = users.val()["password"]
      score = users.val()["score"]
      user = User(name, surname, id, password, score)
      list_of_users.append(user)
  except TypeError:
    pass
  return Users(list_of_users)

def check_user_data(id):
  # check user data by user id
  all_users = db.child("users").get()
  for users in all_users.each()[1:]:
    if users.key() == id:
      return(users.val())


def check_user_particular_data(id, key):
  #check one attribute of user
  return check_user_data(id)[key]


def find_users_by_key(key, keyValue):
  # finds all users who have particular keyValue
  all_users = db.child("users").get()
  list = []
  for users in all_users.each()[1:]:
    if all_users.val()[users.key()][key] == keyValue:
      list.append(users.key())
  return list


def user_instance_by_id(id):
  # creates user instance from id
  all_users = db.child("users").get()
  for user in all_users.each()[1:]:
    if user.key() == id:
      name = all_users.val()[user.key()]["name"]
      surname = all_users.val()[user.key()]["surname"]
      password = all_users.val()[user.key()]["password"]
      score = all_users.val()[user.key()]["score"]
      user_instance = User(name, surname, id, password, score)
      return user_instance

######################################################################

def set_trash_bin_data(trash_bin):
  # sets trash_bin data; if trash_bin not exist, create trash_bin
  id = trash_bin.id()
  apartment = trash_bin.apartment()
  full = trash_bin.full()
  user_throwing = trash_bin.user_throwing()
  db.child("bins").child(id).set({"apartment": apartment, "full": full, "user_throwing": user_throwing})


def update_trash_bin_particular_data(id, key, newValue):
  # if key not exist, create new key
  db.child("bins").child(id).update({key: newValue})


def remove_trash_bin_data(id):
  # removes data
  db.child("bins").child(id).remove()


def print_all_trash_bins():
  # print out all bins keys and values
  all_bins = db.child("bins").get()
  for bins in all_bins.each()[1:]:
    print(bins.key())
    print(bins.val())


def list_of_trash_bins():
  list_of_bins = []
  all_bins = db.child("bins").get()
  try:
    for bins in all_bins.each()[1:]:
      id = bins.key()
      apartment = bins.val()["apartment"]
      full = bins.val()["full"]
      user_throwing = bins.val()['user_throwing']
      bin = TrashBin(id, apartment, full, user_throwing)
      list_of_bins.append(bin)
  except TypeError:
    pass
  return TrashBins(list_of_bins)


def check_trash_bin_data(id):
  # check bin data by bin id
  all_bins = db.child("bins").get()
  for bins in all_bins.each()[1:]:
    if bins.key() == id:
      return(bins.val())


def check_trash_bin_particular_data(id, key):
  #check one attribute of a_bin
  return check_trash_bin_data(id)[key]


def find_trash_bin_by_key(key, keyValue):
  # finds all bins which have particular keyValue
  all_bins = db.child("bins").get()
  list = []
  if all_bins.val() is not None:
    for bins in all_bins.each()[1:]:
      if all_bins.val()[bins.key()][key] == keyValue:
        list.append(bins.key())
  return list
  

import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

isMale = False
user_name = ""

@anvil.server.callable
def set_data(name, incomingBool):
  user_name = name
  isMale = incomingBool
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

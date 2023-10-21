import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

user_name = ""

@anvil.server.callable
def set_data(name):
  user_name = name
  return

@anvil.server.callable
def add_prompt(response):
  app_tables.convos.add_row(
    pastConvos=response, 
  )
  return

@anvil.server.callable
def add_response(response):
  app_tables.convos.add_row(
    pastResponses=response, 
  )
  return
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

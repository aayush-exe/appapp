from ._anvil_designer import Form2Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.panel1.items = app_tables.convos.search()
    self.panel1_copy.items = app_tables.convos.search()

    # Any code you write here will run before the form opens.

  def outlined_button_1_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass

  def outlined_button_1_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass



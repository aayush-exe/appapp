from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def button_1_click(self, **event_args):
  ##  set_data(self.name_input.text, incomingBool)
    name = self.name_input.text
    genderBool = True if self.gender.selected_value == "Male" else False
    anvil.server.call('set_data', name, genderBool)
    Notification(name + "::" + str(genderBool)).show()
    # Call your 'clear_inputs' method to clear the boxes
    self.clear_inputs()
    self.column_panel_1_hide()
    pass

  def column_panel_1_hide(self, **event_args):
    """This method is called when the column panel is removed from the screen"""
    pass

  def submit_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass






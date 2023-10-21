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
    self.IntroPane.visible = True
    self.MainPane.visible = False

    # Any code you write here will run before the form opens.

  def outlined_button_1_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass

  def outlined_button_1_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass

  def submit_prompt_click(self, **event_args):
    alert("I'm sending this through OpenAI, so it might take a while!! Bear with me, please... \n ~Misaki")
    
    new_call = self.text_area_1.text
    new_data_point = app_tables.convos.add_row(pastConvos=new_call)
    l = list(self.panel1.items) + [new_data_point]
    self.panel1.items = l
    
    add_to_text = anvil.server.call('get_text', new_call)
    new_data_point_copy = app_tables.convos.add_row(pastResponses=add_to_text)
    m = list(self.panel1_copy.items) + [new_data_point_copy]
    self.panel1_copy.items = m
    pass

  def button_1_click(self, **event_args):
    self.IntroPane.visible = False
    self.MainPane.visible = True
    pass





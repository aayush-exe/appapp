from ._anvil_designer import Form2Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import time

displayIngredients = True

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.panel1.items = app_tables.convos.search()
    self.panel1_copy.items = app_tables.convos.search()
    self.IntroPane.visible = True
    self.MainPane.visible = False
    self.IngredPane.visible = False
    self.recipes_button.visible = False    
    self.chatter_label_copy_3.text = "Here's the ingredients!"
    self.ingredients_list_display.visible = True
    self.instructions_list_display.visible = False
    self.chat_image.source = anvil.server.call('get_image')
    self.recipe_image.source = anvil.server.call('get_image')
    

    # Any code you write here will run before the form opens.

  def outlined_button_1_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass

  def outlined_button_1_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass

  def submit_prompt_click(self, **event_args):
    
    new_call = self.text_area_1.text
    self.text_area_1.text = ""
    
    new_data_point = app_tables.convos.add_row(pastConvos=new_call)
    l = list(self.panel1.items) + [new_data_point]
    self.panel1.items = l
    
    ReadyToGo, add_to_text = anvil.server.call('get_text', new_call)
    if (ReadyToGo):
      self.recipes_button.visible = True
      
    new_data_point_copy = app_tables.convos.add_row(pastResponses=add_to_text)
    m = list(self.panel1_copy.items) + [new_data_point_copy]
    self.panel1_copy.items = m
    pass

  def button_1_click(self, **event_args):
    name = self.name_input.text
    anvil.server.call('send_name', name)
    
    app_tables.convos.delete_all_rows()
    self.panel1.items = []
    self.panel1_copy.items = []

    alert("Hi, "+name+"! Excited to cook with you today!")
    self.IntroPane.visible = False
    self.MainPane.visible = True
    
    pass

  def back_button_click(self, **event_args):
    self.chatter_label_copy_3.text = "Here's the ingredients!"
    self.ingredients_list_display.visible = True
    self.instructions_list_display.visible = False
    pass

  def clear_history_click(self, **event_args):
    app_tables.convos.delete_all_rows()
    self.panel1.items = []
    self.panel1_copy.items = []
    pass

  def recipes_button_click(self, **event_args): 
    
    alert("Hey, this might take a bit. Hang tight, please! \n~Misaki")
    ingredientsList, instructionsList, maxLength = anvil.server.call("get_recipe")
    
    for i in range(maxLength):
      if (len(ingredientsList)-1 < i):
        newDataIn = ""
      else:
        newDataIn = ingredientsList[i]
        
      if (len(instructionsList)-1 < i):
        newDataIns = ""
      else:
        newDataIns = instructionsList[i]
      app_tables.recipe_data.add_row(ingredients=newDataIn, instructions=newDataIns)

    time.sleep(1)
    self.ingredients_list_display.items = app_tables.recipe_data.search()
    self.instructions_list_display.items = app_tables.recipe_data.search()
    self.MainPane.visible = False
    self.IngredPane.visible = True
    app_tables.recipe_data.delete_all_rows()
    self.panel1.items = []
    self.panel1_copy.items = []
    
    pass

  def next_button_click(self, **event_args):
    self.chatter_label_copy_3.text = "Here's the steps to make it!"
    self.ingredients_list_display.visible = False
    self.instructions_list_display.visible = True
    pass

  def restart_button_click(self, **event_args):
    anvil.server.call('send_name',"")
    app_tables.recipe_data.delete_all_rows()
    app_tables.convos.delete_all_rows()
    self.panel1.items = app_tables.convos.search()
    self.panel1_copy.items = app_tables.convos.search()
    self.IntroPane.visible = True
    self.MainPane.visible = False
    self.IngredPane.visible = False
    self.recipes_button.visible = False    
    self.chatter_label_copy_3.text = "Here's the ingredients!"
    self.ingredients_list_display.visible = True
    self.instructions_list_display.visible = False
    self.chat_image.source = anvil.server.call('get_image')
    self.recipe_image.source = anvil.server.call('get_image')
    pass










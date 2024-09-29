import Config as c
import dearpygui.dearpygui as dpg
import os
import sys
import Mem as m
import numpy
def SetValue():
    c.ReadConf()
    m.WriteAstral_Mem(addr=int(m.GetModuleBase_Proc() + numpy.int16(c.conf['Offsets']['astral_player1'])), val=int(dpg.get_value("astralpl1")))
def SetGUI():
    dpg.create_context()
    
    with dpg.window(tag="windw"):
        dpg.add_input_int(label="Int Value for Player 1", min_value=0, max_value=10000, tag="astralpl1")
        dpg.add_button(label="Unlimited Astral(Player 1)", callback=SetValue)
    dpg.create_viewport(title='Dominions 5 External Trainer By RiritoXXL', width=855, height=855)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("windw", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

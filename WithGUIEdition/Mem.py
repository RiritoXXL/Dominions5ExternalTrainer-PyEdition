import pymem
import Config as c
import dearpygui.dearpygui as dpg

def DPG_GetV(value_name):
    return int(dpg.get_value(value_name))
def OpenProcDominions5():
    c.ReadConf()
    return pymem.Pymem(c.conf['Dominions5']['filename'])
def GetModuleBase_Proc():
    c.ReadConf()
    proc = OpenProcDominions5()
    return proc.base_address
def get_AstralPlayer3Addr():
    return int(0x269FCFA)
def get_AstralPlayer1Addr():
    c.ReadConf()
    return int(c.conf['Offsets']['astral_player1'])
def WriteAstral_Mem(addr, val):
    c.ReadConf()
    processmem = OpenProcDominions5()
    processmem.write_int(addr, lambda: DPG_GetV(val))

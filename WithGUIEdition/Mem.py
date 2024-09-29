import pymem
import Config as c

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
def WritePlayer1Astral():
    c.ReadConf()
    print("Hello world!!!")
    processmem = OpenProcDominions5()
    processmem.write_int(GetModuleBase_Proc() + get_AstralPlayer3Addr(), int(10000))
import pymem

def TrHack():
    proc = pymem.Pymem("Dominions5.exe")
    module = proc.base_address
    proc.write_uint(int(module + 0x269EC86), int(15000))
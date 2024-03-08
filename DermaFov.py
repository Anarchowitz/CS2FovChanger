import pymem
import pymem.process
print('Введите значение FOV')
a=int(input())
pm = pymem.Pymem("cs2.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll")
dwLocalPlayerController = pm.read_longlong(client.lpBaseOfDll + 0x19038F8)
def fovactive():
    pm.write_int(dwLocalPlayerController +0x6CC, a) # (A) <- value fov u can change 30-179(180 - not working)
fovactive()
print('Activated!')


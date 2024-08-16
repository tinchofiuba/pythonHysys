import os
import win32com.client as win32

hysys = win32.Dispatch("HYSYS.Application")
os.chdir("C:/Users/tin10/")
path = "pythonHysys2.hsc"
hysys_path = os.path.abspath(path)

hy_case = hysys.Application.ActiveDocument
if hy_case == None:
    hy_case = hysys.SimulationCases.Open(hysys_path)

hysys_f = hy_case.Flowsheet
hysys_ms = hysys_f.MaterialStreams
hysys_es = hysys_f.EnergyStreams
nStreams=hysys_ms.Count
nameStreams=[hysys_ms.Item(i).Name for i in range(0,nStreams)]
print(hysys_ms.Item(nameStreams[0]).MolarFlow.GetValue("kgmole/h"))
hysys_ms.Item(nameStreams[0]).MolarFlow.setValue(1000,"kgmole/h")
print(hysys_ms.Item(nameStreams[0]).MolarFlow.GetValue("kgmole/h"))
'''
stream_mf = hysys_ms.Item("101").MolarFlow.getValue("kgmole/h")
stream_p = hysys_ms.Item("101").Pressure.getValue("bar")
print(hysys_ms.Item(0).Name)
energy_streams = [hysys_es.Item(i).Name for i in range(1, hysys_es.Count + 1)]
print("Energy Streams:", energy_streams)'''

hy_case.Visible = 1


from ClassDef import Boson, Higgs

boson = Boson("Photon", 1, 50)

print("BOSON:")
boson.PrintInfo()

print()

higgs = Higgs("Higgs", 0, 100, 125)

print("HIGGS:")
higgs.PrintInfo()

print("Energy:", higgs.Energy(), "GeV")

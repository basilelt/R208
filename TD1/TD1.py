import pandas
import re
import os

def get_sf(file): ## Facteur d'étalement
    lst_file = file.split("-")
    return lst_file[2]

def get_bw(file): ## Bande passante
    lst_file = file.split("-")
    return lst_file[1]

def get_cr(file): ## Bits redondants
    lst_file = file.split("-")
    return lst_file[3]

def load_data(path_bw_sf, path_raw, file):
    df = pandas.read_csv(os.path.join(path_raw, file), sep = ",", delimiter = None)
    df.columns = ["Time(S)", "Current(A)", "Voltage(V)", "Energy(J)", "UART"]

    df["UART"] = df["UART"].astype("string")

    df["CR"] = get_cr(file)

    df.to_csv(os.path.join(path_bw_sf, f"dataset-{get_bw(file)}-{get_sf(file)}.csv"))



path = os.path.normpath(__file__.replace("TD1.py", ""))
path_raw = os.path.join(path, "raw")
path_bw_sf = os.path.join(path, "bw-sf")

for i in os.listdir(path_raw):
    load_data(path_bw_sf, path_raw, i)

for i in os.listdir(path_bw_sf):
    

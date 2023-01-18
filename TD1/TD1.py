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
    lst_file[3] = lst_file[3].replace(".csv", "")
    return lst_file[3]

def load_data(path, file):
    df = pandas.read_csv(os.path.join(path, file), sep = ",", delimiter = None, dtype = {"File UART (TXT)" : str})
    return df


path = os.path.normpath(__file__.replace("TD1.py", ""))
path_raw = os.path.join(path, "raw")
path_bw_sf = os.path.join(path, "bw-sf")
path_bw = os.path.join(path, "bw")

for i in os.listdir(path_raw):
    df = load_data(path_raw, i)
    df.columns = ["Time(S)", "Current(A)", "Voltage(V)", "Energy(J)", "UART"]

    df["CR"] = get_cr(i)

    df.to_csv(os.path.join(path_bw_sf, f"dataset-{get_bw(i)}-{get_sf(i)}-{get_cr(i)}.csv"), index = False)

df_7 = pandas.DataFrame(columns = ["Time(S)", "Current(A)", "Voltage(V)", "Energy(J)", "UART", "CR"])
df_12 = pandas.DataFrame(columns = ["Time(S)", "Current(A)", "Voltage(V)", "Energy(J)", "UART", "CR"])

for i in os.listdir(path_bw_sf):
    sf = get_sf(i)
    if get_sf(i) == "7":
        df_7 = pandas.concat([df_7, load_data(path_bw_sf, i)])

    elif get_sf(i) == "12":
        df_12 = pandas.concat([df_12, load_data(path_bw_sf, i)])

df_7.to_csv(os.path.join(path_bw, f"dataset-7.csv"), index = False)
df_12.to_csv(os.path.join(path_bw, f"dataset-12.csv"), index = False)

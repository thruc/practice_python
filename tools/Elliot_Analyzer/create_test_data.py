import shutil
import os
PAIRS_FILE = "Pair_Analysis.txt"
FOREX_DATA_PATH = "./ForexData"

with open(PAIRS_FILE, 'r') as infile:
    pairs_to_analyze = infile.read().splitlines()

for pair in pairs_to_analyze:
    pairname, pairtime = pair.split("_")
    forex_name_template = FOREX_DATA_PATH + "\\" + pairname + "\\"
    try:
        os.mkdir(forex_name_template)
    except FileExistsError:
        pass
    forex_data_file = forex_name_template + pair + ".csv"
    shutil.copyfile("./sample_data.csv", forex_data_file)
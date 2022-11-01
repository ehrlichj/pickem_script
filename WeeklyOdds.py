import pandas as pd
import glob
import os


class WeeklyOdds:

    def __init__(self):
        self.odds = self.getOdds()

    def getOdds(self):

        base_path = '/Users/jacobehrlich/Desktop/Pickem_Script/odds/*'
        list_of_files = glob.glob(base_path)
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)

        return pd.read_csv(latest_file)
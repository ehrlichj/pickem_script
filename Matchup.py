import pandas as pd
from datetime import date
class Matchup:

    def __init__(self, teamA, teamB, spreadA, spreadB):
        self.teamA = teamA
        self.teamB = teamB
        self.spreadA = spreadA
        self.spreadB = spreadB


    @staticmethod
    def writeCSV(matchups, week):
        #initialize dataframe
        odds_df = pd.DataFrame(columns=['teamA', 'teamB', 'spreadA', 'spreadB'])

        #iterate through all matchups
        for matchup in matchups:
            teamA = matchup.teamA
            teamB = matchup.teamB
            spreadA = matchup.spreadA
            spreadB = matchup.spreadB

            #initialize data for the next row
            next_row = [teamA,teamB, spreadA,spreadB]
            #add next row tot eh dataframe
            odds_df.loc[len(odds_df)] = next_row
        
        #save dataframe
        base_path = '/Users/jacobehrlich/Desktop/Pickem_Script/odds/'
        path = base_path + week + '_odds_' + date.today().strftime("%m_%d_%Y") + '.csv'
        odds_df.to_csv(path)


        
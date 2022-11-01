
#dictionary to connect abbrv to full team names
full_team_names = {
    'NO' : 'New Orleans Saints',
    'ATL' : 'Atlanta Falcons',
    'SF' : 'San Francisco 49ers',
    'CHI' : 'Chicago Bears',
    'PIT' : 'Pittsburgh Steelers',
    'CIN' : 'Cincinnati Bengals', 
    'PHI' : 'Philadelphia Eagles',
    'DET' : 'Detroit Lions',
    'NE' : 'New England Patriots',
    'MIA' : 'Miami Dolphins',
    'BAL' : 'Baltimore Ravens',
    'NYJ' : 'New York Jets',
    'JAX' : 'Jacksonville Jaguars',
    'WAS' : 'Washington Commanders',
    'CLE' : 'Cleveland Browns',
    'CAR' : 'Carolina Panthers',
    'IND' : 'Indianapolis Colts',
    'HOU' : 'Houston Texans',
    'NYG' : 'New York Giants',
    'TEN' : 'Tennessee Titans',
    'GB'  : 'Green Bay Packers',
    'MIN' : 'Minnesota Vikings',
    'KC'  : 'Kansas City Chiefs',
    'ARI' : 'Arizona Cardinals',
    'LV'  : 'Las Vegas Raiders',
    'LAC' : 'Los Angeles Chargers',
    'TB'  : 'Tampa Bay Buccaneers',
    'DAL' : 'Dallas Cowboys',
    'DEN' : 'Denver Broncos',
    'SEA' : 'Seattle Seahawks',
    'BUF' : 'Buffalo Bills',
    'LAR' : 'Los Angeles Rams'
}
class Team:
    #Initialize Team
    def __init__(self, abrv):
        self.name = full_team_names[abrv]
        self.abrv = abrv

    #Update how teams will be printed
    def __repr__(self):
        return self.name
        
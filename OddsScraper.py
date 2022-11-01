from bs4 import BeautifulSoup
import requests
from Team import Team
from Matchup import Matchup

#Object to scrape a web page looking for odds/spreads
class OddsScraper:
    
    def scrape(self):
        #URL to find odds/spreads
        URL = 'https://www.vegasinsider.com/nfl/odds/las-vegas/'
        #get raw data from the contents of webpage
        page = requests.get(URL)

        #parse raw webpage contents using BeautifulSoup
        soup = BeautifulSoup(page.content, "html.parser")

        #Look for matchups data involving teams
        results = soup.find_all("div", class_="d-flex flex-column h5 justify-content-around py-2 team-name teams-container")
        all_matchups = []
        for matchup in results:
            teams = matchup.find_all('a', class_='pl-1 text-decoration-none')
            matchup_teams = []
            for team in teams:
                abrv = team.text.strip()
                next_team = Team(abrv)
                matchup_teams.append(next_team)
            all_matchups.append(matchup_teams)

        #look for spreads data for each of the matchups
        results = soup.find_all('a', class_='text-decoration-none', href='/goto/fanduel/oddsnfl/', rel='nofollow', target='_blank')
        print(len(results))
        all_spreads = []
        count = 0
        for result in results:
            spreads = result.find_all('div', class_=['m-1 odds-box', "best-odds-box m-1 odds-box"])

            for spread in spreads:
                next_spread = spread.text.replace('\n','').strip().split('+')[0].split('-')
                if len(next_spread) == 2:
                    next_spread = next_spread[:-1]
                elif len(next_spread) == 3:
                    next_spread = ['-'] + next_spread[:-1]
                next_spread = ''.join(next_spread).strip()
                all_spreads.append(next_spread)

        matchup_spreads = []
        matchup_spread = []
        for spread in all_spreads:
            matchup_spread.append(spread)
            if len(matchup_spread) == 2:
                matchup_spreads.append(matchup_spread)
                matchup_spread = []

        matchups = []

        for i in range(len(all_matchups)):
            matchup = all_matchups[i]
            teamA = matchup[0]
            teamB = matchup[1]
            spreadA = matchup_spreads[i][0]
            spreadB = matchup_spreads[i][1]
            
            #create a matchup object 
            next_matchup = Matchup(teamA, teamB, spreadA, spreadB)
            #store matchup object in the matchups list
            matchups.append(next_matchup)

        week = ''.join(soup.find('div', class_='d-flex justify-content-end m-0 pb-1').text.replace('\n','').split()[:2]).lower()
        print(week)

        #write all matchups and their odds to a csv file.
        Matchup.writeCSV(matchups, week)


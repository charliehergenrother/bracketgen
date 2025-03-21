#!/usr/bin/env python3

import random
import argparse
import numpy
import os

PLAY_IN_WINNERS = []
MATCHUP_WINNERS = {}
W_HOME_TEAMS = []

def fill_winners(mens):
    if len(PLAY_IN_WINNERS):
        return
    if mens:
        pass
        PLAY_IN_WINNERS.append("Alabama St.")
        PLAY_IN_WINNERS.append("North Carolina")
        PLAY_IN_WINNERS.append("Mount St. Mary's")
        PLAY_IN_WINNERS.append("Xavier")
        #### start of first round ####
        MATCHUP_WINNERS[0] = "Auburn"
        MATCHUP_WINNERS[1] = "Creighton"
        MATCHUP_WINNERS[2] = "Michigan"
        MATCHUP_WINNERS[3] = "Texas A&M"
        #MATCHUP_WINNERS[4] = "Creighton"
        #MATCHUP_WINNERS[5] = "Baylor"
        #MATCHUP_WINNERS[6] = "Missouri"
        #MATCHUP_WINNERS[7] = "Arizona"
        #MATCHUP_WINNERS[8] = "Purdue"
        #MATCHUP_WINNERS[9] = "Memphis"
        #MATCHUP_WINNERS[10] = "Duke"
        #MATCHUP_WINNERS[11] = "Tennessee"
        MATCHUP_WINNERS[12] = "Drake"
        MATCHUP_WINNERS[13] = "Texas Tech"
        MATCHUP_WINNERS[14] = "Arkansas"
        MATCHUP_WINNERS[15] = "St. John's"
        #MATCHUP_WINNERS[16] = "Houston"
        #MATCHUP_WINNERS[17] = "Iowa"
        #MATCHUP_WINNERS[18] = "Miami (FL)"
        #MATCHUP_WINNERS[19] = "Indiana"
        MATCHUP_WINNERS[20] = "BYU"
        MATCHUP_WINNERS[21] = "Wisconsin"
        #MATCHUP_WINNERS[22] = "Texas A&M"
        #MATCHUP_WINNERS[23] = "Texas"
        MATCHUP_WINNERS[24] = "Houston"
        MATCHUP_WINNERS[25] = "Gonzaga"
        MATCHUP_WINNERS[26] = "McNeese"
        MATCHUP_WINNERS[27] = "Purdue"
        #MATCHUP_WINNERS[28] = "TCU"
        #MATCHUP_WINNERS[29] = "Gonzaga"
        MATCHUP_WINNERS[30] = "UCLA"
        MATCHUP_WINNERS[31] = "Tennessee"
        #### start of second round ####
        #MATCHUP_WINNERS[32] = "Alabama"
        #MATCHUP_WINNERS[33] = "Virginia"
        #MATCHUP_WINNERS[34] = "Baylor"
        #MATCHUP_WINNERS[35] = "Arizona"
        #MATCHUP_WINNERS[36] = "Purdue"
        #MATCHUP_WINNERS[37] = "Tennessee"
        #MATCHUP_WINNERS[38] = "Kansas State"
        #MATCHUP_WINNERS[39] = "Marquette"
        #MATCHUP_WINNERS[40] = "Houston"
        #MATCHUP_WINNERS[41] = "Indiana"
        #MATCHUP_WINNERS[42] = "Xavier"
        #MATCHUP_WINNERS[43] = "Texas"
        #MATCHUP_WINNERS[44] = "Kansas"
        #MATCHUP_WINNERS[45] = "Connecticut"
        #MATCHUP_WINNERS[46] = "Gonzaga"
        #MATCHUP_WINNERS[47] = "UCLA"
        #### start of Sweet 16 ####
        #MATCHUP_WINNERS[48] = "Alabama"
        #MATCHUP_WINNERS[49] = "Arizona"
        #MATCHUP_WINNERS[50] = "Purdue"
        #MATCHUP_WINNERS[51] = "Marquette"
        #MATCHUP_WINNERS[52] = "Houston"
        #MATCHUP_WINNERS[53] = "Texas"
        #MATCHUP_WINNERS[54] = "Kansas"
        #MATCHUP_WINNERS[55] = "UCLA"
        #### start of Elite 8 ####
        #MATCHUP_WINNERS[56] = "Alabama"
        #MATCHUP_WINNERS[57] = "Purdue"
        #MATCHUP_WINNERS[58] = "Houston"
        #MATCHUP_WINNERS[59] = "Kansas"
        #MATCHUP_WINNERS[60] = "Alabama"
        #MATCHUP_WINNERS[61] = "Houston"
        #MATCHUP_WINNERS[62] = "Alabama"
    else:
        PLAY_IN_WINNERS.append("Southern")
        PLAY_IN_WINNERS.append("Iowa St.")
        PLAY_IN_WINNERS.append("William & Mary")
        PLAY_IN_WINNERS.append("Columbia")
        #### start of first round ####
        #MATCHUP_WINNERS[0] = "South Carolina"
        #MATCHUP_WINNERS[1] = "South Florida"
        #MATCHUP_WINNERS[2] = "Oklahoma"
        #MATCHUP_WINNERS[3] = "UCLA"
        #MATCHUP_WINNERS[4] = "Creighton"
        #MATCHUP_WINNERS[5] = "Notre Dame"
        #MATCHUP_WINNERS[6] = "Arizona"
        #MATCHUP_WINNERS[7] = "Maryland"
        #MATCHUP_WINNERS[8] = "Stanford"
        #MATCHUP_WINNERS[9] = "Mississippi"
        #MATCHUP_WINNERS[10] = "Louisville"
        #MATCHUP_WINNERS[11] = "Texas"
        #MATCHUP_WINNERS[12] = "Colorado"
        #MATCHUP_WINNERS[13] = "Duke"
        #MATCHUP_WINNERS[14] = "Florida State"
        #MATCHUP_WINNERS[15] = "Iowa"
        #MATCHUP_WINNERS[16] = "Indiana"
        #MATCHUP_WINNERS[17] = "Oklahoma State"
        #MATCHUP_WINNERS[18] = "Washington State"
        #MATCHUP_WINNERS[19] = "Villanova"
        #MATCHUP_WINNERS[20] = "Michigan"
        #MATCHUP_WINNERS[21] = "LSU"
        #MATCHUP_WINNERS[22] = "NC State"
        #MATCHUP_WINNERS[23] = "Utah"
        #MATCHUP_WINNERS[24] = "Virginia Tech"
        #MATCHUP_WINNERS[25] = "USC"
        #MATCHUP_WINNERS[26] = "Iowa State"
        #MATCHUP_WINNERS[27] = "Tennessee"
        MATCHUP_WINNERS[28] = "Michigan"
        #MATCHUP_WINNERS[29] = "Ohio State"
        #MATCHUP_WINNERS[30] = "Baylor"
        #MATCHUP_WINNERS[31] = "Connecticut"
        #### start of second round ####
        #MATCHUP_WINNERS[32] = "South Carolina"
        #MATCHUP_WINNERS[33] = "UCLA"
        #MATCHUP_WINNERS[34] = "Notre Dame"
        #MATCHUP_WINNERS[35] = "Maryland"
        #MATCHUP_WINNERS[36] = "Stanford"
        #MATCHUP_WINNERS[37] = "Texas"
        #MATCHUP_WINNERS[38] = "Duke"
        #MATCHUP_WINNERS[39] = "Iowa"
        #MATCHUP_WINNERS[40] = "Indiana"
        #MATCHUP_WINNERS[41] = "Villanova"
        #MATCHUP_WINNERS[42] = "LSU"
        #MATCHUP_WINNERS[43] = "Utah"
        #MATCHUP_WINNERS[44] = "Virginia Tech"
        #MATCHUP_WINNERS[45] = "Tennessee"
        #MATCHUP_WINNERS[46] = "Ohio State"
        #MATCHUP_WINNERS[47] = "Connecticut"
        #### start of Sweet 16 ####
        #MATCHUP_WINNERS[48] = "South Carolina"
        #MATCHUP_WINNERS[49] = "Maryland"
        #MATCHUP_WINNERS[50] = "Stanford"
        #MATCHUP_WINNERS[51] = "Iowa"
        #MATCHUP_WINNERS[52] = "Indiana"
        #MATCHUP_WINNERS[53] = "Utah"
        #MATCHUP_WINNERS[54] = "Virginia Tech"
        #MATCHUP_WINNERS[55] = "Connecticut"
        #### start of Elite 8 ####
        #MATCHUP_WINNERS[56] = "South Carolina"
        #MATCHUP_WINNERS[57] = "Stanford"
        #MATCHUP_WINNERS[58] = "Indiana"
        #MATCHUP_WINNERS[59] = "Virginia Tech"
        #MATCHUP_WINNERS[60] = "South Carolina"
        #MATCHUP_WINNERS[61] = "Indiana"
        #MATCHUP_WINNERS[62] = "South Carolina"
        pass

def create_regions(mens):
    regions = [dict(), dict(), dict(), dict()]
    if not mens:
        regions[0] = {  #upper left
            1: "UCLA",
            2: "NC State",
            3: "LSU",
            4: "Baylor",
            5: "Mississippi",
            6: "Florida St.",
            7: "Michigan St.",
            8: "Richmond",
            9: "Georgia Tech",
            10: "Harvard",
            11: "George Mason",
            12: "Ball St.",
            13: "Grand Canyon",
            14: "San Diego St.",
            15: "Vermont",
            16: ["UC San Diego", "Southern"]
        }
        regions[1] = {  #lower left
            1: "USC",
            2: "Connecticut",
            3: "Oklahoma",
            4: "Kentucky",
            5: "Kansas St.",
            6: "Iowa",
            7: "Oklahoma St.",
            8: "California",
            9: "Mississippi St.",
            10: "South Dakota St.",
            11: "Murray St.",
            12: "Fairfield",
            13: "Liberty",
            14: "FGCU",
            15: "Arkansas St.",
            16: "UNC Greensboro"
        }
        regions[2] = {  #upper right
            1: "South Carolina",
            2: "Duke",
            3: "North Carolina",
            4: "Maryland",
            5: "Alabama",
            6: "West Virginia",
            7: "Vanderbilt",
            8: "Utah",
            9: "Indiana",
            10: "Oregon",
            11: ["Columbia", "Washington"],
            12: "Green Bay",
            13: "Norfolk St.",
            14: "Oregon St.",
            15: "Lehigh",
            16: "Tennessee Tech"
        }
        regions[3] = {  #lower right
            1: "Texas",
            2: "TCU",
            3: "Notre Dame",
            4: "Ohio St.",
            5: "Tennessee",
            6: "Michigan",
            7: "Louisville",
            8: "Illinois",
            9: "Creighton",
            10: "Nebraska",
            11: ["Iowa St.", "Princeton"],
            12: "South Florida",
            13: "Montana St.",
            14: "Stephen F. Austin",
            15: "FDU",
            16: ["High Point", "William & Mary"]
        }
    else:
        regions[0] = {  #upper left
            1: "Auburn",
            2: "Michigan St.",
            3: "Iowa St.",
            4: "Texas A&M",
            5: "Michigan",
            6: "Mississippi",
            7: "Marquette",
            8: "Louisville",
            9: "Creighton",
            10: "New Mexico",
            11: ["San Diego St.", "North Carolina"],
            12: "UC San Diego",
            13: "Yale",
            14: "Lipscomb",
            15: "Bryant",
            16: ["Alabama St.", "Saint Francis"]
            }
        regions[1] = {  #lower left
            1: "Florida",
            2: "St. John's",
            3: "Texas Tech",
            4: "Maryland",
            5: "Memphis",
            6: "Missouri",
            7: "Kansas",
            8: "Connecticut",
            9: "Oklahoma",
            10: "Arkansas",
            11: "Drake",
            12: "Colorado St.",
            13: "Grand Canyon",
            14: "UNC Wilmington",
            15: "Omaha",
            16: "Norfolk St."
            }
        regions[2] = {  #upper right
            1: "Duke",
            2: "Alabama",
            3: "Wisconsin",
            4: "Arizona",
            5: "Oregon",
            6: "BYU",
            7: "St. Mary's",
            8: "Mississippi St.",
            9: "Baylor",
            10: "Vanderbilt",
            11: "VCU",
            12: "Liberty",
            13: "Akron",
            14: "Montana",
            15: "Robert Morris",
            16: ["American", "Mount St. Mary's"],
            }
        regions[3] = {  #lower right
            1: "Houston",
            2: "Tennessee",
            3: "Kentucky",
            4: "Purdue",
            5: "Clemson",
            6: "Illinois",
            7: "UCLA",
            8: "Gonzaga",
            9: "Georgia",
            10: "Utah St.",
            11: ["Texas", "Xavier"],
            12: "McNeese",
            13: "High Point",
            14: "Troy",
            15: "Wofford",
            16: "SIU Edwardsville",
            }
        for region in regions:
            for seed in [1, 2, 3, 4]:
                W_HOME_TEAMS.append(region[seed])
    return regions

def do_play_in(matchup, winners, teams, regions, mens):
    if matchup[0] in PLAY_IN_WINNERS:
        for region in regions:
            for seed in region:
                if type(region[seed]) == list and matchup[0] in region[seed]:
                    region[seed] = matchup[0]
                    return matchup[0]
    if matchup[1] in PLAY_IN_WINNERS:
        for region in regions:
            for seed in region:
                if type(region[seed]) == list and matchup[1] in region[seed]:
                    region[seed] = matchup[1]
                    return matchup[1]
    findwinner(matchup[0], matchup[1], winners, teams, regions, mens)
    play_in_winner = winners.pop()
    found = False
    for region in regions:
        for seed in region:
            if region[seed] == matchup:
                region[seed] = play_in_winner
                found = True
                break
        if found:
            break
    return play_in_winner

def findwinner(team1, team2, winners, teams, regions, mens):
    if type(team1) == list:
        play_in_winner = do_play_in(team1, winners, teams, regions, mens)
        team1 = play_in_winner
    if type(team2) == list:
        play_in_winner = do_play_in(team2, winners, teams, regions, mens)
        team2 = play_in_winner
    if len(winners) in MATCHUP_WINNERS:
        winners.append(MATCHUP_WINNERS[len(winners)])
        return
    spread = (teams[team1] - teams[team2])
    if mens:
        spread *= 0.675 # kenpom ratings are over 100 possessions. The average men's bball game has 67.5 possessions
    else:
        #women's first two rounds are at home
        if team1 in W_HOME_TEAMS and len(winners) < 48:
            spread += 2.91
        if team2 in W_HOME_TEAMS and len(winners) < 48:
            spread -= 2.91
    if abs(spread) <= 21:
        chance = -0.00002609*spread*spread*spread + 0.00002466*spread*spread + 0.033206*spread + 0.5
    elif spread > 21:
        chance = 0.98
    elif spread < -21:
        chance = 0.02
    r = random.uniform(0.0, 1.0)
    if r < chance:
        winners.append(team1)
    else:
        winners.append(team2)

def simbracket(mens, winners, teams, regions):
    for region in regions:
        for matchup in [[1, 16], [8, 9], [5, 12], [4, 13], [6, 11], [3, 14], [7, 10], [2, 15]]:
            findwinner(region[matchup[0]], region[matchup[1]], winners, teams, regions, mens)
    winnerindex = 0
    while winnerindex + 1 < len(winners):
        findwinner(winners[winnerindex], winners[winnerindex + 1], winners, teams, regions, mens)
        winnerindex += 2
    
def findmaxlen(teams, indices):
    maxlen = ""
    for x in indices:
        if len(teams[x]) > len(maxlen):
            maxlen = teams[x]
    lens = [len(teams[x]) for x in indices]
    return max(lens)

def create_teams(init_teams):
    rng = numpy.random.default_rng()
    simmed_ratings = dict()
    for team in init_teams:
        simmed_ratings[team] = rng.normal(init_teams[team]["rating"], 0.5)
    return simmed_ratings

def translate_team_kenpom(team):
    translate_dict = {
        "Nebraska Omaha": "Omaha",
        "Saint Mary's": "St. Mary's",
        "SIUE": "SIU Edwardsville"
    }
    if team in translate_dict:
        return translate_dict[team]
    return team

def translate_team_sonny(team):
    translate_dict = {
        "California San Diego": "UC San Diego",
        "Ucla": "UCLA",
        "Lsu": "LSU",
        "North Carolina St.": "NC State",
        "Southern Cal": "USC",
        "North Carolina Greensboro": "UNC Greensboro",
        "Florida Gulf Coast": "FGCU",
        "Wisconsin Green Bay": "Green Bay",
        "S. F. Austin": "Stephen F. Austin",
        "Tcu": "TCU",
        "Fairleigh Dickinson": "FDU"
    }
    if team in translate_dict:
        return translate_dict[team]
    return team

def scrape_initial_kenpom(mens):
    #TODO maybe only do this once a day
    team_kenpoms = dict()
    if mens:
        os.system('wget --user-agent="Mozilla" -O kenpoms.html https://kenpom.com/')
        with open("kenpoms.html", "r") as f:
            for line in f.read().split("\n"):
                if "team.php?" in line:
                    anchor_index = line.find("team.php?")
                    team = line[line.find('">', anchor_index)+2:line.find("</a>")]
                    team = translate_team_kenpom(team)
                    rank = int(line[line.find("hard_left")+11:line.find('</td>')])
                    rating = float(line[line.find("<td>")+4:line.find('</td><td class="td-left divide')])
                    team_kenpoms[team] = {"rating": rating, "rank": rank}
    else:
        os.system('wget -O sonnys.html https://sonnymoorepowerratings.com/w-basket.htm')
        with open("sonnys.html", "r") as f:
            table_start = False
            for line in f.read().split("\n"):
                if line.strip() == "<B>":
                    table_start = True
                    continue
                if table_start:
                    team = line[4:32].strip().title()
                    team = translate_team_sonny(team)
                    rank = int(line[:3].strip())
                    rating = float(line[54:].strip())
                    team_kenpoms[team] = {"rating": rating, "rank": rank}
                    if rank == 362:     #TODO ? How many teams are there?
                        break
    return team_kenpoms

def printbracket(winners, regions):
    space = max([max([len(x[y]) for y in x]) for x in regions])
    left1 = findmaxlen(winners, [x for x in range(0, 16)])
    right1 = findmaxlen(winners, [x for x in range(16, 32)])
    left2 = findmaxlen(winners, [x for x in range(32, 40)])
    right2 = findmaxlen(winners, [x for x in range(40, 48)])
    left3 = findmaxlen(winners, [x for x in range(48, 52)])
    right3 = findmaxlen(winners, [x for x in range(52, 56)])
    left4 = findmaxlen(winners, [x for x in range(56, 58)])
    right4 = findmaxlen(winners, [x for x in range(58, 60)])

    myfirst = ' ' * (left1 + left2 + left3 + left4 + right1 + right2 + right3 + right4 + 16)
    mysecond = ' ' * (left2 + left3 + left4 + right2 + right3 + right4 + 12)
    mythird = ' ' * (left3 + left4 + right3 + right4 + 8)
    myfourth = ' ' * (left4 + right4 + 4)

    print(regions[0][1].ljust(space) + myfirst + regions[2][1].rjust(space))
    print(' '*space + '| ' + winners[0].ljust(left1) + mysecond + winners[16].rjust(right1) + ' |')
    print(regions[0][16].ljust(space) + myfirst + regions[2][16].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + '| ' + winners[32].ljust(left2) + mythird + winners[40].rjust(right2) + ' |')
    print(regions[0][8].ljust(space) + myfirst + regions[2][8].rjust(space))
    print(' '*space + '| ' + winners[1].ljust(left1) + mysecond + winners[17].rjust(right1) + ' |')
    print(regions[0][9].ljust(space) + myfirst + regions[2][9].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + ' '*2 + ' '*left2 + '| ' + winners[48].ljust(left3) + myfourth + winners[52].rjust(right3) + ' |')
    print(regions[0][5].ljust(space) + myfirst + regions[2][5].rjust(space))
    print(' '*space + '| ' + winners[2].ljust(left1) + mysecond + winners[18].rjust(right1) + ' |')
    print(regions[0][12].ljust(space) + myfirst + regions[2][12].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + '| ' + winners[33].ljust(left2) + mythird + winners[41].rjust(right2) + ' |')
    print(regions[0][4].ljust(space) + myfirst + regions[2][4].rjust(space))
    print(' '*space + '| ' + winners[3].ljust(left1) + mysecond + winners[19].rjust(right1) + ' |')
    print(regions[0][13].ljust(space) + myfirst + regions[2][13].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + ' '*2 + ' '*left2 + ' '*2 + ' '*left3 + '| ' + winners[56].ljust(left4) + '  ' + winners[58].rjust(right4) + ' |')
    print(regions[0][6].ljust(space) + myfirst + regions[2][6].rjust(space))
    print(' '*space + '| ' + winners[4].ljust(left1) + mysecond + winners[20].rjust(right1) + ' |')
    print(regions[0][11].ljust(space) + myfirst + regions[2][11].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + '| ' + winners[34].ljust(left2) + mythird + winners[42].rjust(right2) + ' |')
    print(regions[0][3].ljust(space) + myfirst + regions[2][3].rjust(space))
    print(' '*space + '| ' + winners[5].ljust(left1) + mysecond + winners[21].rjust(right1) + ' |')
    print(regions[0][14].ljust(space) + myfirst + regions[2][14].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + ' '*2 + ' '*left2 + '| ' + winners[49].ljust(left3) + myfourth + winners[53].rjust(right3) + ' |')
    print(regions[0][7].ljust(space) + myfirst + regions[2][7].rjust(space))
    print(' '*space + '| ' + winners[6].ljust(left1) + mysecond + winners[22].rjust(right1) + ' |')
    print(regions[0][10].ljust(space) + myfirst + regions[2][10].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + '| ' + winners[35].ljust(left2) + mythird + winners[43].rjust(right2) + ' |')
    print(regions[0][2].ljust(space) + myfirst + regions[2][2].rjust(space))
    print(' '*space + '| ' + winners[7].ljust(left1) + mysecond + winners[23].rjust(right1) + ' |')
    print(regions[0][15].ljust(space) + myfirst + regions[2][15].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + ' '*2 + ' '*left2 + ' '*left3 + '| ' + winners[60].ljust(left4) + '   ' + winners[61].rjust(right4) + ' |')
    print()
    print(' '*space + ' '*2 + ' '*left1 + ' '*2 + ' '*left2 + ' '*left3 + '           ' + winners[62].ljust(right4))
    print(regions[1][1].ljust(space) + myfirst + regions[3][1].rjust(space))
    print(' '*space + '| ' + winners[8].ljust(left1) + mysecond + winners[24].rjust(right1) + ' |')
    print(regions[1][16].ljust(space) + myfirst + regions[3][16].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + '| ' + winners[36].ljust(left2) + mythird + winners[44].rjust(right2) + ' |')
    print(regions[1][8].ljust(space) + myfirst + regions[3][8].rjust(space))
    print(' '*space + '| ' + winners[9].ljust(left1) + mysecond + winners[25].rjust(right1) + ' |')
    print(regions[1][9].ljust(space) + myfirst + regions[3][9].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + ' '*2 + ' '*left2 + '| ' + winners[50].ljust(left3) + myfourth + winners[54].rjust(right3) + ' |')
    print(regions[1][5].ljust(space) + myfirst + regions[3][5].rjust(space))
    print(' '*space + '| ' + winners[10].ljust(left1) + mysecond + winners[26].rjust(right1) + ' |')
    print(regions[1][12].ljust(space) + myfirst + regions[3][12].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + '| ' + winners[37].ljust(left2) + mythird + winners[45].rjust(right2) + ' |')
    print(regions[1][4].ljust(space) + myfirst + regions[3][4].rjust(space))
    print(' '*space + '| ' + winners[11].ljust(left1) + mysecond + winners[27].rjust(right1) + ' |')
    print(regions[1][13].ljust(space) + myfirst + regions[3][13].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + ' '*2 + ' '*left2 + ' '*2 + ' '*left3 + '| ' + winners[57].ljust(left4) + '   ' + winners[59].rjust(right4) + ' |')
    print(regions[1][6].ljust(space) + myfirst + regions[3][6].rjust(space))
    print(' '*space + '| ' + winners[12].ljust(left1) + mysecond + winners[28].rjust(right1) + ' |')
    print(regions[1][11].ljust(space) + myfirst + regions[3][11].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + '| ' + winners[38].ljust(left2) + mythird + winners[46].rjust(right2) + ' |')
    print(regions[1][3].ljust(space) + myfirst + regions[3][3].rjust(space))
    print(' '*space + '| ' + winners[13].ljust(left1) + mysecond + winners[29].rjust(right1) + ' |')
    print(regions[1][14].ljust(space) + myfirst + regions[3][14].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + ' '*2 + ' '*left2 + '| ' + winners[51].ljust(left3) + myfourth + winners[55].rjust(right3) + ' |')
    print(regions[1][7].ljust(space) + myfirst + regions[3][7].rjust(space))
    print(' '*space + '| ' + winners[14].ljust(left1) + mysecond + winners[30].rjust(right1) + ' |')
    print(regions[1][10].ljust(space) + myfirst + regions[3][10].rjust(space))
    print(' '*space + ' '*2 + ' '*left1 + '| ' + winners[39].ljust(left2) + mythird + winners[47].rjust(right2) + ' |')
    print(regions[1][2].ljust(space) + myfirst + regions[3][2].rjust(space))
    print(' '*space + '| ' + winners[15].ljust(left1) + mysecond + winners[31].rjust(right1) + ' |')
    print(regions[1][15].ljust(space) + myfirst + regions[3][15].rjust(space))
    print()

def create_parser():
    parser = argparse.ArgumentParser(description="Randomly generate a bracket using 538's prediction model")
    parser.add_argument("-n", dest="num_sims", type=int, default=1, help="run n simulations and print the results (default=1)")
    parser.add_argument("-s", dest="print_bracket", action='store_false', help="Suppress printing the bracket")
    parser.add_argument("-w", dest="womens", action='store_true', help="Simulate the women's tournament")
    parser.add_argument("-o", dest="outputfile", type=str, default="", help="Store output in this csv file")
    parser.add_argument("-b", dest="htmloutputfile", type=str, default="", help="Build html file with results")
    parser.set_defaults(print_bracket=True, womens=False)
    return parser 

if __name__ == '__main__':

    parser = create_parser()
    args = parser.parse_args()

    num_sims = args.num_sims
    print_bracket = args.print_bracket
    mens = not args.womens
    outputfile = args.outputfile
    htmloutputfile = args.htmloutputfile
    
    trialnum = 0
    finalfours = {}
    champs = {}
    init_teams = scrape_initial_kenpom(mens)
    results = dict()
    for team in init_teams:
        results[team] = [0, 0, 0, 0, 0, 0]

    fill_winners(mens)

    while trialnum < num_sims:
        regions = create_regions(mens)
        winners = []

        teams = create_teams(init_teams)
        simbracket(mens, winners, teams, regions)

        if print_bracket:
            printbracket(winners, regions)
        
        for winner in winners[:32]:
            results[winner][0] += 1

        for winner in winners[32:48]:
            results[winner][1] += 1

        for winner in winners[48:56]:
            results[winner][2] += 1

        for winner in winners[56:60]:
            results[winner][3] += 1

        for winner in winners[60:62]:
            results[winner][4] += 1

        results[winners[62]][5] += 1

        for x in range(56, 60):
            if winners[x] in finalfours:
                finalfours[winners[x]] += 1
            else:
                finalfours[winners[x]] = 1

        if winners[62] in champs:
            champs[winners[62]] += 1
        else:
            champs[winners[62]] = 1

        trialnum += 1


    champlist = list(reversed(sorted(champs.items(), key=lambda kv: kv[1])))
    fflist = list(reversed(sorted(finalfours.items(), key=lambda kv: kv[1])))
    
    champpct = []
    ffpct = []

    for x in champlist:
        champpct.append(tuple([x[0], str(round(x[1]/num_sims*100, 2))+'%']))
    for x in fflist:
        ffpct.append(tuple([x[0], str(round(x[1]/num_sims*100, 2))+'%']))

    print('champs:', champpct, '\n')
    print('final fours:', ffpct)

    print("TEAM                2R     S16    E8     F4     NCG    NC")
    f = open(outputfile, "w")
    f.write("Team,2R,S16,E8,F4,NCG,NC\n")

    h = open(htmloutputfile, "w")
    h.write('<!DOCTYPE html>\n\n')
    h.write('<html>\n')
    h.write('<head>\n')
    h.write('  <link rel="icon" type="image/x-icon" href="assets/chergieball.ico">\n')
    h.write('  <link rel="stylesheet" href="tablestyling.css">\n')
    h.write('</head>\n\n')
    h.write('<div class="link_row"\n')
    h.write('  <nav>\n')
    h.write('    <ul class="link_list">\n')
    h.write('      <li>\n')
    h.write('        <img src=assets/chergieball.ico height="50px" style="padding-top: 5px;"><img/>\n')
    h.write('      </li>\n')
    h.write('      <li class="non_image_element">\n')
    h.write('        <a href="men.html">Men\'s Projections</a>\n')
    h.write('      </li>\n')
    h.write('      <li class="non_image_element">\n')
    h.write('        <a href="women.html">Women\'s Projections</a>\n')
    h.write('      <li>\n')
    h.write('      </li>\n')
    h.write('    </ul>\n')
    h.write('  </nav>\n')
    h.write('</div>\n')
    h.write('<div style="float: left">\n')
    h.write('  <table class="percent_table">\n')
    h.write('    <thead>\n')
    h.write('      <tr><th></th><th>Team</th><th>2R</th><th>S16</th><th>E8</th><th>F4</th><th>NCG</th><th>NC</th></tr>\n')
    h.write('    </thead>\n')
    h.write('    <tbody>\n')
    
    for team in sorted(results, key=lambda x: results[x][5], reverse=True):
        if results[team][0] == 0:
            continue
        print(team.ljust(20), end='')
        print("{:.2f}".format(results[team][0]/num_sims*100).rjust(5), end='  ')
        print("{:.2f}".format(results[team][1]/num_sims*100).rjust(5), end='  ')
        print("{:.2f}".format(results[team][2]/num_sims*100).rjust(5), end='  ')
        print("{:.2f}".format(results[team][3]/num_sims*100).rjust(5), end='  ')
        print("{:.2f}".format(results[team][4]/num_sims*100).rjust(5), end='  ')
        print("{:.2f}".format(results[team][5]/num_sims*100).rjust(5), end='  ')
        print()
        
        f.write(team + ",")
        for i in range(0, 6):
            f.write(str(results[team][i]/num_sims*100))
            f.write(",")
        f.write("\n")
        
        h.write('      <tr>')
        h.write('<td><img class="row_logo" src = assets/' + team.replace(" ", "").replace(".", "").replace("'", "").replace("&", "") + '.png></img></td>')
        h.write('<td>' + team + '</td>')
        for i in range (0, 6):
            color_percentage = str(round((-results[team][i]/num_sims*100)/2 + 100))
            h.write('<td style="background-color: hsl(120, 50%, ' + color_percentage + '%)">' + "{:.2f}".format(results[team][i]/num_sims*100) + '%</td>')
        h.write('</tr>\n')
    h.write('    </tbody>')
    h.write('  </table>\n')
    h.write('</div>\n')


    f.write("\n\n")
    f.write("Team,2R,S16,E8,F4,NCG,NC\n")
    
    h.write('<div style="margin-left: 50%">\n')
    h.write('  <table class="odds_table">\n')
    h.write('    <thead>\n')
    h.write('      <tr><th></th><th>Team</th><th>2R</th><th>S16</th><th>E8</th><th>F4</th><th>NCG</th><th>NC</th></tr>\n')
    h.write('    </thead>\n')
    h.write('    <tbody>\n')

    for team in sorted(results, key=lambda x: results[x][5], reverse=True):
        if results[team][0] == 0:
            continue
        f.write(team + ",")
        h.write('      <tr>')
        h.write('<td><img class="row_logo" src = assets/' + team.replace(" ", "").replace(".", "").replace("'", "").replace("&", "") + '.png></img></td>')
        h.write('<td>' + team + '</td>')
        for i in range(0, 6):
            try:
                if results[team][i]/num_sims > 0.5:
                    odds = 100/(1 - 1/(results[team][i]/num_sims))
                else:
                    odds = 100/(results[team][i]/num_sims) - 100
            except ZeroDivisionError:
                odds = ""
            f.write(str(odds))
            f.write(",")
            
            try:
                odds_out = str(round(odds))
                if odds > 0:
                    odds_out = "+" + odds_out
                color_percentage = str(round((-results[team][i]/num_sims*100)/2 + 100))
                h.write('<td style="background-color: hsl(120, 50%, ' + color_percentage + '%)">' + odds_out + '</td>')
            except TypeError:
                h.write('<td style="background-color: hsl(120, 50%, 100%)"></td>')
        h.write('</tr>\n')
        f.write("\n")





#!/usr/bin/env python3

import os
import sys
import random
import argparse

PLAY_IN_WINNERS = []
MATCHUP_WINNERS = {}

def fill_winners(mens):
    if len(PLAY_IN_WINNERS):
        return
    if mens:
        PLAY_IN_WINNERS.append("Texas A&M-CC")
        PLAY_IN_WINNERS.append("Pittsburgh")
        #PLAY_IN_WINNERS.append("Fairleigh Dickinson")
        #PLAY_IN_WINNERS.append("Arizona State")
        #### start of first round ####
        #MATCHUP_WINNERS[0] = "Alabama"
        #MATCHUP_WINNERS[1] = "Maryland"
        #MATCHUP_WINNERS[2] = "San Diego State"
        #MATCHUP_WINNERS[3] = "Virginia"
        #MATCHUP_WINNERS[4] = "Creighton"
        #MATCHUP_WINNERS[5] = "Baylor"
        #MATCHUP_WINNERS[6] = "Missouri"
        #MATCHUP_WINNERS[7] = "Arizona"
        #MATCHUP_WINNERS[8] = "Purdue"
        #MATCHUP_WINNERS[9] = "Memphis"
        #MATCHUP_WINNERS[10] = "Duke"
        #MATCHUP_WINNERS[11] = "Tennessee"
        #MATCHUP_WINNERS[12] = "Kentucky"
        #MATCHUP_WINNERS[13] = "Kansas State"
        #MATCHUP_WINNERS[14] = "Michigan State"
        #MATCHUP_WINNERS[15] = "Marquette"
        #MATCHUP_WINNERS[16] = "Houston"
        #MATCHUP_WINNERS[17] = "Iowa"
        #MATCHUP_WINNERS[18] = "Miami (FL)"
        #MATCHUP_WINNERS[19] = "Indiana"
        #MATCHUP_WINNERS[20] = "Iowa State"
        #MATCHUP_WINNERS[21] = "Xavier"
        #MATCHUP_WINNERS[22] = "Texas A&M"
        #MATCHUP_WINNERS[23] = "Texas"
        #MATCHUP_WINNERS[24] = "Kansas"
        #MATCHUP_WINNERS[25] = "Arkansas"
        #MATCHUP_WINNERS[26] = "Saint Mary's"
        #MATCHUP_WINNERS[27] = "Connecticut"
        #MATCHUP_WINNERS[28] = "TCU"
        #MATCHUP_WINNERS[29] = "Gonzaga"
        #MATCHUP_WINNERS[30] = "Northwestern"
        #MATCHUP_WINNERS[31] = "UCLA"
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
        #PLAY_IN_WINNERS.append("Mississippi State")
        #PLAY_IN_WINNERS.append("Southern")
        #PLAY_IN_WINNERS.append("Purdue")
        #PLAY_IN_WINNERS.append("Monmouth")
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
        #MATCHUP_WINNERS[28] = "North Carolina"
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
            1: "South Carolina",
            2: "Maryland",
            3: "Notre Dame",
            4: "UCLA",
            5: "Oklahoma",
            6: "Creighton",
            7: "Arizona",
            8: "South Florida",
            9: "Marquette",
            10: "West Virginia",
            11: ["Illinois", "Mississippi State"],
            12: "Portland",
            13: "Sacramento State",
            14: "Southern Utah",
            15: "Holy Cross",
            16: "Norfolk State"
        }
        regions[1] = {  #lower left
            1: "Stanford",
            2: "Iowa",
            3: "Duke",
            4: "Texas",
            5: "Louisville",
            6: "Colorado",
            7: "Florida State",
            8: "Mississippi",
            9: "Gonzaga",
            10: "Georgia",
            11: "Middle Tennessee",
            12: "Drake",
            13: "East Carolina",
            14: "Iona",
            15: "SE Louisiana",
            16: ["Southern", "Sacred Heart"]
        }
        regions[2] = {  #upper right
            1: "Indiana",
            2: "Utah",
            3: "LSU",
            4: "Villanova",
            5: "Washington State",
            6: "Michigan",
            7: "NC State",
            8: "Oklahoma State",
            9: "Miami (FL)",
            10: "Princeton",
            11: "UNLV",
            12: "FGCU",
            13: "Cleveland State",
            14: "Hawaii",
            15: "Gardner-Webb",
            16: ["Tennessee Tech", "Monmouth"]
        }
        regions[3] = {  #lower right
            1: "Virginia Tech",
            2: "Connecticut",
            3: "Ohio State",
            4: "Tennessee",
            5: "Iowa State",
            6: "North Carolina",
            7: "Baylor",
            8: "USC",
            9: "South Dakota State",
            10: "Alabama",
            11: ["Purdue", "Saint John's"],
            12: "Toledo",
            13: "Saint Louis",
            14: "James Madison",
            15: "Vermont",
            16: "Chattanooga"
        }
    else:
        regions[0] = {  #upper left
            1: "Alabama",
            2: "Arizona",
            3: "Baylor",
            4: "Virginia",
            5: "San Diego State",
            6: "Creighton",
            7: "Missouri",
            8: "Maryland",
            9: "West Virginia",
            10: "Utah State",
            11: "NC State",
            12: "Charleston",
            13: "Furman",
            14: "UC-Santa Barbara",
            15: "Princeton",
            16: ["Texas A&M-CC", "SE Missouri State"]
            }
        regions[1] = {  #lower left
            1: "Purdue",
            2: "Marquette",
            3: "Kansas State",
            4: "Tennessee",
            5: "Duke",
            6: "Kentucky",
            7: "Michigan State",
            8: "Memphis",
            9: "Florida Atlantic",
            10: "USC",
            11: "Providence",
            12: "Oral Roberts",
            13: "Louisiana",
            14: "Montana State",
            15: "Vermont",
            16: ["Texas Southern", "Fairleigh Dickinson"]
            }
        regions[2] = {  #upper right
            1: "Houston",
            2: "Texas",
            3: "Xavier",
            4: "Indiana",
            5: "Miami (FL)",
            6: "Iowa State",
            7: "Texas A&M",
            8: "Iowa",
            9: "Auburn",
            10: "Penn State",
            11: ["Mississippi State", "Pittsburgh"],
            12: "Drake",
            13: "Kent State",
            14: "Kennesaw State",
            15: "Colgate",
            16: "Northern Kentucky",
            }
        regions[3] = {  #lower right
            1: "Kansas",
            2: "UCLA",
            3: "Gonzaga",
            4: "Connecticut",
            5: "Saint Mary's",
            6: "TCU",
            7: "Northwestern",
            8: "Arkansas",
            9: "Illinois",
            10: "Boise State",
            11: ["Arizona State", "Nevada"],
            12: "VCU",
            13: "Iona",
            14: "Grand Canyon",
            15: "UNC-Asheville",
            16: "Howard",
            }
    return regions

def do_play_in(matchup, winners, teams, regions):
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
    findwinner(matchup[0], matchup[1], winners, teams, regions)
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

def findwinner(team1, team2, winners, teams, regions):
    if type(team1) == list:
        play_in_winner = do_play_in(team1, winners, teams, regions)
        team1 = play_in_winner
    if type(team2) == list:
        play_in_winner = do_play_in(team2, winners, teams, regions)
        team2 = play_in_winner
    if len(winners) in MATCHUP_WINNERS:
        winners.append(MATCHUP_WINNERS[len(winners)])

    diff = teams[team1] - teams[team2]
    chance =  1/(1+(10**(-1*diff*30.464/400)))
    r = random.uniform(0.0, 1.0)
    if r < chance:
        winners.append(team1)
    else:
        winners.append(team2)

def simbracket(winners, teams, regions):
    for region in regions:
        for matchup in [[1, 16], [8, 9], [5, 12], [4, 13], [6, 11], [3, 14], [7, 10], [2, 15]]:
            findwinner(region[matchup[0]], region[matchup[1]], winners, teams, regions)
    winnerindex = 0
    while winnerindex + 1 < len(winners):
        findwinner(winners[winnerindex], winners[winnerindex + 1], winners, teams, regions)
        winnerindex += 2
    
def findmaxlen(teams, indices):
    maxlen = ""
    for x in indices:
        if len(teams[x]) > len(maxlen):
            maxlen = teams[x]
    lens = [len(teams[x]) for x in indices]
    return max(lens)

def create_teams(mens):
    if mens:
        f = open('fivethirtyeight_ncaa_forecasts_2023_men.csv')
    else:
        f = open('fivethirtyeight_ncaa_forecasts_2023_women.csv')
    teams = {}
    for line in f:
        line = line.strip()
        items = line.split(',')
        if items[0] == 'gender':
            continue
        teams[str(items[13])] = float(items[14])
    return teams

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
    parser.set_defaults(print_bracket=True, womens=False)
    return parser 

if __name__ == '__main__':

    parser = create_parser()
    args = parser.parse_args()

    num_sims = args.num_sims
    print_bracket = args.print_bracket
    mens = not args.womens
    
    trialnum = 0
    finalfours = {}
    champs = {}

    while trialnum < num_sims:
        regions = create_regions(mens)
        winners = []

        teams = create_teams(mens)
        simbracket(winners, teams, regions)

        if print_bracket:
            printbracket(winners, regions)
        
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


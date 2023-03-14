#!/usr/bin/env python3

import os
import sys
import random

PLAY_IN_WINNERS = []
MATCHUP_WINNERS = {
        #0: "Alabama",
        #1: "Maryland",
        #2: "San Diego State",
        #3: "Virginia",
        #4: "Creighton",
        #5: "Baylor",
        #6: "Missouri",
        #7: "Arizona",
        #8: "Purdue",
        #9: "Memphis",
        #10: "Duke",
        #11: "Tennessee",
        #12: "Kentucky",
        #13: "Kansas State",
        #14: "Michigan State",
        #15: "Marquette
        }

def create_regions():
    regions = [dict(), dict(), dict(), dict()]
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
        region[seed] = matchup[0]
        return matchup[0]
    if matchup[1] in PLAY_IN_WINNERS:
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

def createteams():
    f = open('fivethirtyeight_ncaa_forecasts_2023.csv')
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

if __name__ == '__main__':

    print_bracket = True
    num_sims = 1 
    argindex = 1
    
    while argindex < len(sys.argv):
        if sys.argv[argindex] == '-h':
            print("Welcome to bracketgen, the bracket generator!")
            print("Use: ./bracketgen [-h] [-n num_sims] [-s]")
            print("     -h: print this help message")
            print("     -n: run num_sims simulations and print the results afterward")
            print("     -s: suppress printing the bracket")
            sys.exit()
        elif sys.argv[argindex] == '-n':
            num_sims = int(sys.argv[argindex+1])
            argindex += 2
        elif sys.argv[argindex] == '-s':
            print_bracket = False
            argindex += 1 
        else:
            print('incorrect argument', sys.argv[argindex])
            sys.exit()
    
    trialnum = 0
    finalfours = {}
    champs = {}

    while trialnum < num_sims:
        regions = create_regions()
        winners = []

        teams = createteams()
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


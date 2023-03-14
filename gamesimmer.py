#!/usr/bin/env python3

import os
import sys
import bracketgen

if __name__ == '__main__':
    teams = bracketgen.createteams()
    team1 = sys.argv[1]
    team2 = sys.argv[2]
    diff = teams[team1] - teams[team2]
    chance =  1/(1+(10**(-1*diff*30.464/400)))
    print(chance)


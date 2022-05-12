#!/bin/bash

#python3 ./main.py --username ${SPOT_ACCOUNT} --password ${SPOT_PASSWORD} ${SPOT_IP}
python3 /usr/src/app/spot-follow/replay_mission.py ${SPOT_IP} autowalk '/usr/src/app/Example Missions/summerlab.walk'
# For commands that have to be run always at the start of the execution

# Absolute File Paths (from source directory of your OS) /usr/home/app
# Relative File Paths (from the relative directory the account is at) ./app ./folder

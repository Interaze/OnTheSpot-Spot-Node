#!/bin/bash

#python3 ./main.py --username ${SPOT_ACCOUNT} --password ${SPOT_PASSWORD} ${SPOT_IP}
python3 /usr/src/app/spot-follow/replay_mission.py ${SPOT_IP} autowalk '/usr/src/app/Example Missions/summerlab.walk'


#!/bin/bash

service dbus start
bluetoothd &

python3 ${FILE}
# For commands that have to be run always at the start of the execution

# Absolute File Paths (from source directory of your OS) /usr/home/app
# Relative File Paths (from the relative directory the account is at) ./app ./folder
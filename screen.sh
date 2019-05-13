#!/bin/bash

. /lib/lsb/init-functions

NAME=launch.sh

# ----------------------------

log_begin_msg "${COLOR_BLUE} Check terminal... ${COLOR_NC}"
PS=` /bin/ps -Aww -o command | grep -v grep | grep terminalApp -c`
if [ $PS -eq 0 ];
then
  screen -m -d -S terminalApp /home/jackkum/screen/app.sh
fi

log_end_msg 0

# -----------------------------

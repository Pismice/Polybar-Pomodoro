#!/usr/bin/env bash

# Terminate already running bar instances
# If all your bars have ipc enabled, you can use 
polybar-msg cmd quit
# Otherwise you can use the nuclear option:
# killall -q polybar

# Launch example on DP-0 (primary monitor)
MONITOR=DP-0 polybar --reload example &

# Launch secondary on HDMI-0 (secondary monitor)
MONITOR=HDMI-0 polybar --reload secondary &

# echo "Bars launched..."
# echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
# polybar example 2>&1 | tee -a /tmp/polybar2.log & disown

echo "Bars launched..."

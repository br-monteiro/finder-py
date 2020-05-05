#!/bin/bash
set -e

echo "Init"

# current dir
root_dir=$(pwd)
finder=$root_dir"/finder.py"

# setting necessary permissions
sudo chmod +x $finder
# remove old symbolic link
sudo rm -f /usr/local/bin/finder
# setting new symbolic link
sudo ln -s $finder /usr/local/bin/finder

echo "Setup completed successfully! =)"

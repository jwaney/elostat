#!/bin/bash
echo "Starting up EloStat Development Environment"
sudo apt update && sudo apt upgrade -y

if command -v python3 > /dev/null 2>&1; then
	echo "Python3 already installed."
else
	sudo apt install python3 -y
fi

if command -v pip3 > /dev/null 2>&1; then
	echo "Pip3 already installed."
else
	sudo apt install python3-pip -y
	pip3 install virtualenv
fi

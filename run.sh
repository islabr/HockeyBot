#!/bin/bash
apt-get update
pip install discord.py
pip install -U python-dotenv 
pip install matplotlib
pip install tabulate

python hockey_bot.py
#!/bin/bash
mv python3 board.py board
chmod +x board
sudo cp board /usr/bin/board
sudo rm -r ../Tic_tac_toe

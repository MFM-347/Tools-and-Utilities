#!/bin/bash

read -p "Enter the directory path: " directory
read -p "Enter the base name: " base_name

py ren.py "$directory" "$base_name"
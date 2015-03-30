#!/bin/bash
git pull origin master
cd ../scripts
./select.sh
./apply.sh
cd ../
git add .
git commit -m 'update hosts'
git push origin master

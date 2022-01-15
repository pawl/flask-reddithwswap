#!/bin/bash
set -euo pipefail

while true
do
   FLASK_APP=heckingoodboys flask populate-cache
   sleep 14400
done

#!/bin/bash
# compact the three 4th-cycle documents of a country into one readable file
slug=$1; code=$2
out="C:/Users/rolan/AppData/Local/Temp/${slug}_read.txt"
: > "$out"
for d in 1 2 3; do
  f="countries/$slug/evidence/A_HRC_WG.6_53_${code}_${d}-EN.txt"
  [ -f "$f" ] || continue
  echo "=========== DOC $d" >> "$out"
  awk 'BEGIN{p=1} /^Notes$/{p=0} p' "$f" | grep -v "^$" | grep -v "^GE\.\|^A/HRC/WG.6\|^[0-9]$" | sed -n 8,400p >> "$out"
done
wc -c "$out"

#!/usr/bin/env bash
# Usage: accdb-export-all.sh full-path-to-db

command -v mdb-tables >/dev/null 2>&1 || {
    echo >&2 "I require mdb-tables but it's not installed. Aborting.";
    exit 1;
}

command -v mdb-export >/dev/null 2>&1 || {
    echo >&2 "I require mdb-export but it's not installed. Aborting.";
    exit 1;
}

fullfilename=$1
filename=$(basename "$fullfilename")
dbname=${filename%.*}

# Create result/<dbname> directory
output_dir="result/$dbname"
mkdir -p "$output_dir"

IFS=$'\n'
for table in $(mdb-tables -1 "$fullfilename"); do
    echo "Exporting table $table"
    mdb-export "$fullfilename" "$table" > "$output_dir/$table.csv"
done

echo "All tables exported to $output_dir"

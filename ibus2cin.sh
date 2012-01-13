#!/bin/bash

function parse() {
	local dbfile=$1
	local cinfile=$2
	local sqlfile="parse.sql"
	local headerfile="header.txt"
	local tmpdb="output.db.tmp"
	local tmpcsv="output.csv.tmp"
	local sqlite=`which sqlite3`
	
	if [ ! -e "$dbfile" ]; then
		echo "File not found: $dbfile"
		exit
	fi
	
	if [ ! -e "$sqlfile" ]; then
		echo "File missing: $sqlfile"
		exit
	fi

	if [ ! -e "$headerfile" ]; then
		echo "File missing: $headerfile"
		exit
	fi

	if [ -e "$tmpcsv" ]; then
		rm "$tmpcsv"
		exit
	fi

	if [ -e "$tmpdb" ]; then
		rm "$tmpdb"
		exit
	fi
	
	cp "$dbfile" "$tmpdb"
	
	echo "Parse $dbfile."
	$sqlite "$tmpdb" < $sqlfile
	
	echo "Make $cinfile."
	cat "$headerfile" "$tmpcsv" > "$cinfile"
	echo "%chardef end" >> "$cinfile"
	
	# clean up
	rm "$tmpdb"
	rm "$tmpcsv"
	
	echo "Done."
}

function usage() {
	echo
	echo "Description:";
	echo "    ibus2cin -- Convert Boshiamy table for IBus to cin table."
	echo
	echo "Usage:";
	echo "    ibus2cin.sh source_file target_file"
	echo
	echo "Example:"
	echo "    ibus2cin.sh boshiamy_t.db boshiamy_t.cin"
	echo
}

if [ $# != 2 ]; then
	usage
else
	parse $1 $2
fi

/**
 *
 * ibus2cin
 * https://github.com/ethanliu/ibus2cin
 *
 * @author Ethan Liu - https://creativecrap.com
 * @version: 2.0.1
 *
 */

package main

import (
	"database/sql"
	"flag"
	"fmt"
	_ "github.com/mattn/go-sqlite3"
	"io"
	// "io/ioutil"
	"os"
	// "os/exec"
	// "strconv"
	"strings"
	"time"
)

const (
	defaultTableVersion    = "2.1"
	defaultOuptputFileName = "[iBus-file].cin"
	tmpDatabaseFile        = "tmp.db"
)

var tableVersion string
var inputFilePath string
var outputFilePath string

func usage() {
	fmt.Println("ibus2cin - version 2.0.1")
	fmt.Println("Generate CIN table from iBus database provided by boshiamy.com.")
	fmt.Println("This program is distributed to help legal users, but without any warranty.")
	fmt.Println("It's not an official utility from boshiamy.com, please use it well.")
	fmt.Println("Source repo: https://github.com/ethanliu/ibus2cin\n")
	fmt.Printf("Usage:\n  %s [OPTIONS] iBus-file \n\n", os.Args[0])
	fmt.Println("Examples:")
	fmt.Printf("  %s boshiamy-ibus-1-8-x/boshiamy_t.db \n", os.Args[0])
	fmt.Printf("  %s -v 1.1 boshiamy-ibus/boshiamy_t.db \n", os.Args[0])
	fmt.Printf("  %s -v 1.1 -o boshiamy.cin boshiamy-ibus/boshiamy_t.db \n", os.Args[0])
	fmt.Println("\nOptions:")
	flag.PrintDefaults()
	os.Exit(1)
}

func fileExists(path string) bool {
	_, err := os.Stat(path)
	if os.IsNotExist(err) {
		return false
	}
	return err == nil
}

func checkError(err error) {
	if err != nil {
		fmt.Println("Error:")
		panic(err)
	}
}

func copyFile(src string, dst string) {
	from, err := os.Open(src)
	checkError(err)
	defer from.Close()

	to, err := os.OpenFile(dst, os.O_RDWR|os.O_CREATE, 0644)
	checkError(err)
	defer to.Close()

	_, err = io.Copy(to, from)
	checkError(err)
}

func cinHeader(db *sql.DB) string {
	ename := "Boshiamy"
	cname := "嘸蝦米"
	serial := ""
	created_at := (time.Now()).Format("2006-01-02 15:04:05")

	rows, err := db.Query("SELECT attr, val FROM ime WHERE attr IN ('name.zh_tw', 'name', 'serial_number')")
	checkError(err)

	var attr string
	var val string
	for rows.Next() {
		err = rows.Scan(&attr, &val)
		checkError(err)
		if attr == "name" && val != "" {
			ename = val
		} else if attr == "name.zh_tw" && val != "" {
			cname = val
		} else if attr == "serial_number" && val != "" {
			serial = val
		}
	}
	rows.Close()

	return `#
# The table was generated at ` + created_at + ` by ibus2cin utility
# https://github.com/ethanliu/ibus2cin
#
%gen_inp
%encoding UTF-8
%ename ` + ename + `
%cname ` + cname + `
%version ` + tableVersion + `
%serial_number ` + serial + `
%selkey 0123456789
%keyname begin
a a
b b
c c
d d
e e
f f
g g
h h
i i
j j
k k
l l
m m
n n
o o
p p
q q
r r
s s
t t
u u
v v
w w
x x
y y
z z
, ,
. .
' ’
[ [
] ]
%keyname end
%chardef begin
`
}

func cinFooter() string {
	return "%chardef end"
}

func exportV1_1(db *sql.DB) string {
	query := `
		ALTER TABLE "phrases" ADD COLUMN "r0" CHAR; ALTER TABLE "phrases" ADD COLUMN "r1" CHAR; ALTER TABLE "phrases" ADD COLUMN "r2" CHAR; ALTER TABLE "phrases" ADD COLUMN "r3" CHAR; ALTER TABLE "phrases" ADD COLUMN "r4" CHAR;
		UPDATE "phrases" SET r0 = "0" WHERE m0 = 0; UPDATE "phrases" SET r0 = "a" WHERE m0 = 1; UPDATE "phrases" SET r0 = "b" WHERE m0 = 2; UPDATE "phrases" SET r0 = "c" WHERE m0 = 3; UPDATE "phrases" SET r0 = "d" WHERE m0 = 4; UPDATE "phrases" SET r0 = "e" WHERE m0 = 5; UPDATE "phrases" SET r0 = "f" WHERE m0 = 6; UPDATE "phrases" SET r0 = "g" WHERE m0 = 7; UPDATE "phrases" SET r0 = "h" WHERE m0 = 8; UPDATE "phrases" SET r0 = "i" WHERE m0 = 9; UPDATE "phrases" SET r0 = "j" WHERE m0 = 10; UPDATE "phrases" SET r0 = "k" WHERE m0 = 11; UPDATE "phrases" SET r0 = "l" WHERE m0 = 12; UPDATE "phrases" SET r0 = "m" WHERE m0 = 13; UPDATE "phrases" SET r0 = "n" WHERE m0 = 14; UPDATE "phrases" SET r0 = "o" WHERE m0 = 15; UPDATE "phrases" SET r0 = "p" WHERE m0 = 16; UPDATE "phrases" SET r0 = "q" WHERE m0 = 17; UPDATE "phrases" SET r0 = "r" WHERE m0 = 18; UPDATE "phrases" SET r0 = "s" WHERE m0 = 19; UPDATE "phrases" SET r0 = "t" WHERE m0 = 20; UPDATE "phrases" SET r0 = "u" WHERE m0 = 21; UPDATE "phrases" SET r0 = "v" WHERE m0 = 22; UPDATE "phrases" SET r0 = "w" WHERE m0 = 23; UPDATE "phrases" SET r0 = "x" WHERE m0 = 24; UPDATE "phrases" SET r0 = "y" WHERE m0 = 25; UPDATE "phrases" SET r0 = "z" WHERE m0 = 26; UPDATE "phrases" SET r0 = "[" WHERE m0 = 27; UPDATE "phrases" SET r0 = ";" WHERE m0 = 28; UPDATE "phrases" SET r0 = "'" WHERE m0 = 29; UPDATE "phrases" SET r0 = "[" WHERE m0 = 45; UPDATE "phrases" SET r0 = "]" WHERE m0 = 46; UPDATE "phrases" SET r0 = "," WHERE m0 = 55; UPDATE "phrases" SET r0 = "." WHERE m0 = 56;
		UPDATE "phrases" SET r1 = "0" WHERE m1 = 0; UPDATE "phrases" SET r1 = "a" WHERE m1 = 1; UPDATE "phrases" SET r1 = "b" WHERE m1 = 2; UPDATE "phrases" SET r1 = "c" WHERE m1 = 3; UPDATE "phrases" SET r1 = "d" WHERE m1 = 4; UPDATE "phrases" SET r1 = "e" WHERE m1 = 5; UPDATE "phrases" SET r1 = "f" WHERE m1 = 6; UPDATE "phrases" SET r1 = "g" WHERE m1 = 7; UPDATE "phrases" SET r1 = "h" WHERE m1 = 8; UPDATE "phrases" SET r1 = "i" WHERE m1 = 9; UPDATE "phrases" SET r1 = "j" WHERE m1 = 10; UPDATE "phrases" SET r1 = "k" WHERE m1 = 11; UPDATE "phrases" SET r1 = "l" WHERE m1 = 12; UPDATE "phrases" SET r1 = "m" WHERE m1 = 13; UPDATE "phrases" SET r1 = "n" WHERE m1 = 14; UPDATE "phrases" SET r1 = "o" WHERE m1 = 15; UPDATE "phrases" SET r1 = "p" WHERE m1 = 16; UPDATE "phrases" SET r1 = "q" WHERE m1 = 17; UPDATE "phrases" SET r1 = "r" WHERE m1 = 18; UPDATE "phrases" SET r1 = "s" WHERE m1 = 19; UPDATE "phrases" SET r1 = "t" WHERE m1 = 20; UPDATE "phrases" SET r1 = "u" WHERE m1 = 21; UPDATE "phrases" SET r1 = "v" WHERE m1 = 22; UPDATE "phrases" SET r1 = "w" WHERE m1 = 23; UPDATE "phrases" SET r1 = "x" WHERE m1 = 24; UPDATE "phrases" SET r1 = "y" WHERE m1 = 25; UPDATE "phrases" SET r1 = "z" WHERE m1 = 26; UPDATE "phrases" SET r1 = "[" WHERE m1 = 27; UPDATE "phrases" SET r1 = ";" WHERE m1 = 28; UPDATE "phrases" SET r1 = "'" WHERE m1 = 29; UPDATE "phrases" SET r1 = "[" WHERE m1 = 45; UPDATE "phrases" SET r1 = "]" WHERE m1 = 46; UPDATE "phrases" SET r1 = "," WHERE m1 = 55; UPDATE "phrases" SET r1 = "." WHERE m1 = 56;
		UPDATE "phrases" SET r2 = "0" WHERE m2 = 0; UPDATE "phrases" SET r2 = "a" WHERE m2 = 1; UPDATE "phrases" SET r2 = "b" WHERE m2 = 2; UPDATE "phrases" SET r2 = "c" WHERE m2 = 3; UPDATE "phrases" SET r2 = "d" WHERE m2 = 4; UPDATE "phrases" SET r2 = "e" WHERE m2 = 5; UPDATE "phrases" SET r2 = "f" WHERE m2 = 6; UPDATE "phrases" SET r2 = "g" WHERE m2 = 7; UPDATE "phrases" SET r2 = "h" WHERE m2 = 8; UPDATE "phrases" SET r2 = "i" WHERE m2 = 9; UPDATE "phrases" SET r2 = "j" WHERE m2 = 10; UPDATE "phrases" SET r2 = "k" WHERE m2 = 11; UPDATE "phrases" SET r2 = "l" WHERE m2 = 12; UPDATE "phrases" SET r2 = "m" WHERE m2 = 13; UPDATE "phrases" SET r2 = "n" WHERE m2 = 14; UPDATE "phrases" SET r2 = "o" WHERE m2 = 15; UPDATE "phrases" SET r2 = "p" WHERE m2 = 16; UPDATE "phrases" SET r2 = "q" WHERE m2 = 17; UPDATE "phrases" SET r2 = "r" WHERE m2 = 18; UPDATE "phrases" SET r2 = "s" WHERE m2 = 19; UPDATE "phrases" SET r2 = "t" WHERE m2 = 20; UPDATE "phrases" SET r2 = "u" WHERE m2 = 21; UPDATE "phrases" SET r2 = "v" WHERE m2 = 22; UPDATE "phrases" SET r2 = "w" WHERE m2 = 23; UPDATE "phrases" SET r2 = "x" WHERE m2 = 24; UPDATE "phrases" SET r2 = "y" WHERE m2 = 25; UPDATE "phrases" SET r2 = "z" WHERE m2 = 26; UPDATE "phrases" SET r2 = "[" WHERE m2 = 27; UPDATE "phrases" SET r2 = ";" WHERE m2 = 28; UPDATE "phrases" SET r2 = "'" WHERE m2 = 29; UPDATE "phrases" SET r2 = "[" WHERE m2 = 45; UPDATE "phrases" SET r2 = "]" WHERE m2 = 46; UPDATE "phrases" SET r2 = "," WHERE m2 = 55; UPDATE "phrases" SET r2 = "." WHERE m2 = 56;
		UPDATE "phrases" SET r3 = "0" WHERE m3 = 0; UPDATE "phrases" SET r3 = "a" WHERE m3 = 1; UPDATE "phrases" SET r3 = "b" WHERE m3 = 2; UPDATE "phrases" SET r3 = "c" WHERE m3 = 3; UPDATE "phrases" SET r3 = "d" WHERE m3 = 4; UPDATE "phrases" SET r3 = "e" WHERE m3 = 5; UPDATE "phrases" SET r3 = "f" WHERE m3 = 6; UPDATE "phrases" SET r3 = "g" WHERE m3 = 7; UPDATE "phrases" SET r3 = "h" WHERE m3 = 8; UPDATE "phrases" SET r3 = "i" WHERE m3 = 9; UPDATE "phrases" SET r3 = "j" WHERE m3 = 10; UPDATE "phrases" SET r3 = "k" WHERE m3 = 11; UPDATE "phrases" SET r3 = "l" WHERE m3 = 12; UPDATE "phrases" SET r3 = "m" WHERE m3 = 13; UPDATE "phrases" SET r3 = "n" WHERE m3 = 14; UPDATE "phrases" SET r3 = "o" WHERE m3 = 15; UPDATE "phrases" SET r3 = "p" WHERE m3 = 16; UPDATE "phrases" SET r3 = "q" WHERE m3 = 17; UPDATE "phrases" SET r3 = "r" WHERE m3 = 18; UPDATE "phrases" SET r3 = "s" WHERE m3 = 19; UPDATE "phrases" SET r3 = "t" WHERE m3 = 20; UPDATE "phrases" SET r3 = "u" WHERE m3 = 21; UPDATE "phrases" SET r3 = "v" WHERE m3 = 22; UPDATE "phrases" SET r3 = "w" WHERE m3 = 23; UPDATE "phrases" SET r3 = "x" WHERE m3 = 24; UPDATE "phrases" SET r3 = "y" WHERE m3 = 25; UPDATE "phrases" SET r3 = "z" WHERE m3 = 26; UPDATE "phrases" SET r3 = "[" WHERE m3 = 27; UPDATE "phrases" SET r3 = ";" WHERE m3 = 28; UPDATE "phrases" SET r3 = "'" WHERE m3 = 29; UPDATE "phrases" SET r3 = "[" WHERE m3 = 45; UPDATE "phrases" SET r3 = "]" WHERE m3 = 46; UPDATE "phrases" SET r3 = "," WHERE m3 = 55; UPDATE "phrases" SET r3 = "." WHERE m3 = 56;
		UPDATE "phrases" SET r4 = "0" WHERE m4 = 0; UPDATE "phrases" SET r4 = "a" WHERE m4 = 1; UPDATE "phrases" SET r4 = "b" WHERE m4 = 2; UPDATE "phrases" SET r4 = "c" WHERE m4 = 3; UPDATE "phrases" SET r4 = "d" WHERE m4 = 4; UPDATE "phrases" SET r4 = "e" WHERE m4 = 5; UPDATE "phrases" SET r4 = "f" WHERE m4 = 6; UPDATE "phrases" SET r4 = "g" WHERE m4 = 7; UPDATE "phrases" SET r4 = "h" WHERE m4 = 8; UPDATE "phrases" SET r4 = "i" WHERE m4 = 9; UPDATE "phrases" SET r4 = "j" WHERE m4 = 10; UPDATE "phrases" SET r4 = "k" WHERE m4 = 11; UPDATE "phrases" SET r4 = "l" WHERE m4 = 12; UPDATE "phrases" SET r4 = "m" WHERE m4 = 13; UPDATE "phrases" SET r4 = "n" WHERE m4 = 14; UPDATE "phrases" SET r4 = "o" WHERE m4 = 15; UPDATE "phrases" SET r4 = "p" WHERE m4 = 16; UPDATE "phrases" SET r4 = "q" WHERE m4 = 17; UPDATE "phrases" SET r4 = "r" WHERE m4 = 18; UPDATE "phrases" SET r4 = "s" WHERE m4 = 19; UPDATE "phrases" SET r4 = "t" WHERE m4 = 20; UPDATE "phrases" SET r4 = "u" WHERE m4 = 21; UPDATE "phrases" SET r4 = "v" WHERE m4 = 22; UPDATE "phrases" SET r4 = "w" WHERE m4 = 23; UPDATE "phrases" SET r4 = "x" WHERE m4 = 24; UPDATE "phrases" SET r4 = "y" WHERE m4 = 25; UPDATE "phrases" SET r4 = "z" WHERE m4 = 26; UPDATE "phrases" SET r4 = "[" WHERE m4 = 27; UPDATE "phrases" SET r4 = ";" WHERE m4 = 28; UPDATE "phrases" SET r4 = "'" WHERE m4 = 29; UPDATE "phrases" SET r4 = "[" WHERE m4 = 45; UPDATE "phrases" SET r4 = "]" WHERE m4 = 46; UPDATE "phrases" SET r4 = "," WHERE m4 = 55; UPDATE "phrases" SET r4 = "." WHERE m4 = 56;`
	_, err := db.Exec(query)
	// checkError(err)
	if err != nil {
		fmt.Println("Error: Table Version mismatch, please try with another version\n")
		usage()
	}

	rows, err := db.Query("SELECT (coalesce(r0,'')||coalesce(r1,'')||coalesce(r2,'')||coalesce(r3,'')||coalesce(r4,'')) AS root, phrase FROM phrases ORDER BY id ASC")
	checkError(err)

	data := ""
	var root string
	var phrase string

	for rows.Next() {
		err = rows.Scan(&root, &phrase)
		checkError(err)

		root = strings.Trim(strings.ToLower(root), " ")
		phrase = strings.Trim(phrase, " ")

		if root == "" || phrase == "" {
			continue
		}
		data += root + "\t" + phrase + "\n"
		// fmt.Println(root, phrase)
	}
	rows.Close()

	return data
}

func exportV2_1(db *sql.DB) string {
	rows, err := db.Query("SELECT tabkeys AS root, phrase FROM phrases ORDER BY id ASC")
	// checkError(err)
	if err != nil {
		fmt.Println("Error: Version mismatch, please try with another version\n")
		usage()
	}

	data := ""
	var root string
	var phrase string

	for rows.Next() {
		err = rows.Scan(&root, &phrase)
		checkError(err)

		root = strings.Trim(strings.ToLower(root), " ")
		phrase = strings.Trim(phrase, " ")

		if root == "" || phrase == "" {
			continue
		}
		data += root + "\t" + phrase + "\n"
		// fmt.Println(root, phrase)
	}
	rows.Close()

	return data
}

func saveFile(header string, content string, footer string) {
	_, err := os.Stat(outputFilePath)
	if os.IsNotExist(err) {
		// create ifle
		_, err := os.Create(outputFilePath)
		checkError(err)
	}

	file, err := os.OpenFile(outputFilePath, os.O_RDWR, 0644)
	checkError(err)
	defer file.Close()

	_, err = file.WriteString(header + content + footer)
	checkError(err)
}

func export() {
	copyFile(inputFilePath, tmpDatabaseFile)

	db, err := sql.Open("sqlite3", tmpDatabaseFile)
	checkError(err)
	// defer db.Close()

	header := cinHeader(db)
	footer := cinFooter()
	content := ""

	if tableVersion == "1.1" {
		content = exportV1_1(db)
	} else if tableVersion == "2.1" {
		content = exportV2_1(db)
	} else {
		db.Close()
		fmt.Println("Error: Unknown table version")
		usage()
	}

	db.Close()
	saveFile(header, content, footer)

	err = os.Remove(tmpDatabaseFile)
	checkError(err)

}

func init() {
	flag.Usage = usage
	flag.StringVar(&tableVersion, "v", defaultTableVersion, "Boshiamy cin table version")
	flag.StringVar(&outputFilePath, "o", defaultOuptputFileName, "Output file path")
}

func main() {
	flag.Parse()
	inputFilePath = flag.Arg(0)

	if inputFilePath == "" {
		usage()
	}

	if outputFilePath == defaultOuptputFileName {
		outputFilePath = strings.Replace(inputFilePath, ".db", "", -1) + ".cin"
	}

	if fileExists(inputFilePath) == false {
		fmt.Printf("Error:\n%s not exists\n\n", inputFilePath)
		usage()
	}

	export()

	fmt.Println("Table Version:", tableVersion)
	fmt.Println("Input:", inputFilePath)
	fmt.Println("Output:", outputFilePath)
	// fmt.Println("\n")
}

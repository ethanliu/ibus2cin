@echo off
SetLocal

if [%1%]==[] (
	echo Usage: ibus2cin.bat source_file target_file
	echo Example: ibus2cin.bat boshiamy_t.db boshiamy_t.cin
	goto END
)

if [%2%]==[] (
	echo Usage: ibus2cin.bat source_file target_file
	echo Example: ibus2cin.bat boshiamy_t.db boshiamy_t.cin
	goto END
)


set dbfile=%1%
set cinfile=%2%
set sqlfile=parse.sql
set headerfile=header.txt
set tmpdb=output.db.tmp
set tmpcsv=output.csv.tmp


if not exist %dbfile% (
	echo File not found: %dbfile%
	goto END
)

if not exist %sqlfile% (
	echo File missing: %sqlfile%
	goto END
)

if not exist %headerfile% (
	echo File missing: %headerfile%
	goto END
)

if exist %tmpdb% (
	del %tmpdb%
)

if exist %tmpcsv% (
	del %tmpcsv%
)

copy %dbfile% %tmpdb%

echo Parse %dbfile%
sqlite3.exe %tmpdb% < %sqlfile%

echo Make %cinfile%
type %headerfile% %tmpcsv% > %cinfile%
echo %%chardef end >> %cinfile%

del %tmpdb%
del %tmpcsv%

echo Done.

:END
EndLocal
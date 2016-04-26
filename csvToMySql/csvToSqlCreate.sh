#!/bin/sh
# pass in the file name as an argument: ./csvToSqlSchema.sh filename.csv
csvsql --dialect mysql --snifflimit 100000 $1

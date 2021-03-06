
#####################################################################################
### User creation
## mysql --user="root"

CREATE USER 'auditWriter'@'localhost' IDENTIFIED BY 'writer';
GRANT ALL PRIVILEGES ON audit.* TO 'auditWriter'@'localhost'  WITH GRANT OPTION;

CREATE USER 'auditWriter'@'%' IDENTIFIED BY 'writer';
GRANT ALL PRIVILEGES ON audit.* TO 'auditWriter'@'%'  WITH GRANT OPTION;

CREATE USER 'auditReader'@'localhost' IDENTIFIED BY 'reader';
GRANT SELECT, SHOW VIEW ON audit.* TO 'auditReader'@'localhost'  WITH GRANT OPTION;

CREATE USER 'auditReader'@'%' IDENTIFIED BY 'reader';
GRANT SELECT, SHOW VIEW ON audit.* TO 'auditReader'@'%'  WITH GRANT OPTION;

create database audit;
exit

#####################################################################################
### Table creation

## mysql --user="auditWriter"

## Option.1:  generate on local machine
## ./csvToSqlCreate.sh sample.csv
# mysql -h10.9.214.82 -u auditWriter -p --local-infile=1
## Don't forget the --local-infile=1
# LOAD DATA INFILE '/Users/ajeetganga/git/funWithPython/csvToMySql/sample.csv' INTO TABLE audit.sample FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '\\' LINES TERMINATED BY '\n' STARTING BY '';

## Option.2:  generate on-line.
## http://www.convertcsv.com/csv-to-sql.htm

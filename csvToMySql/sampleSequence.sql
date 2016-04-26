## mysql --user="root"
# CREATE USER 'auditWriter'@'localhost' IDENTIFIED BY 'writer';
# GRANT ALL PRIVILEGES ON audit.* TO 'auditWriter'@'localhost'  WITH GRANT OPTION;
# CREATE USER 'auditWriter'@'%' IDENTIFIED BY 'writer';
# GRANT ALL PRIVILEGES ON audit.* TO 'auditWriter'@'%'  WITH GRANT OPTION;
## exit
## mysql --user="auditWriter"
# create database audit;
## ./csvToSqlCreate.sh sample.csv
# LOAD DATA INFILE '/Users/ajeetganga/git/funWithPython/csvToMySql/sample.csv' INTO TABLE audit.sample FIELDS TERMINATED BY ',' ENCLOSED BY '' ESCAPED BY '\\' LINES TERMINATED BY '\n' STARTING BY '';
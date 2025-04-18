CREATE DATABASE mydata;
USE mydata;
CREATE TABLE `hospital` (
  `Nameoftablets` varchar(100) NOT NULL,
  `ref` varchar(50) NOT NULL,
  `dose` varchar(50) DEFAULT NULL,
  `NoOfTablets` varchar(50) DEFAULT NULL,
  `lot` varchar(50) DEFAULT NULL,
  `issuedate` varchar(50) DEFAULT NULL,
  `expdate` varchar(50) DEFAULT NULL,
  `dailydose` varchar(50) DEFAULT NULL,
  `storage` varchar(100) DEFAULT NULL,
  `nhsnumber` varchar(45) DEFAULT NULL,
  `PatientName` varchar(100) DEFAULT NULL,
  `DOB` varchar(45) DEFAULT NULL,
  `PatientAddress` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Nameoftablets`,`ref`)
)

SELECT * FROM mydata.hospital;

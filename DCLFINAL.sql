

#------------------------------------------DCL COMMANDS -------------------------------------------------------------------------------
CREATE USER "manager"@"localhost" identified by "Manager@hms0202";
GRANT all on hostelms.* to "manager"@"localhost";
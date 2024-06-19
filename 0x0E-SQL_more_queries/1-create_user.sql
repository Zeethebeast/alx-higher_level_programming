-- This script cretaes a user on my server and assign a password
CREATE USER 'user_0d_1'@'localhost' IF NOT EXISTS IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'USER_0d_1'@'localhost';
FLUSH PRIVILEGES;

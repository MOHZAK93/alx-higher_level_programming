-- creates the MySQL users on your server
CREATE USER
	IF NOT EXISTS 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
	ON *.*
	TO 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;

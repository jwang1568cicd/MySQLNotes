This projects will focus how to use MySQL with Linux, Windows via CLI, GUI based MySQLWorkbench and Python script with mysql-connector.

1. The following reference will be the starting points if you need fundamental understanding about using MySQL before getting into specific CLI and python scripts for creating, accessing and updatinig the DBs.
a. SQL Tutorial for Beginners [Full Course] : https://www.youtube.com/watch?v=7S_tz1z_5bA
b. Useful installation guide for Ubuntu based MySQL server: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04. The attached Vagrant file is a reference if you are using VirtualBox VM. 
c. For Windows environment, we will try with MySQL-workbench alone with Python scripts.

<samples of snipt of successful installation>
No VM guests are running outdated hypervisor (qemu) binaries on this host.
vagrant@ubuntu-jammy:~$ sudo systemctl status mysql.service
● mysql.service - MySQL Community Server
     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2024-07-04 17:05:05 UTC; 56s ago
    Process: 2667 ExecStartPre=/usr/share/mysql/mysql-systemd-start pre (code=exited, status=0/SUCCES>
   Main PID: 2675 (mysqld)
     Status: "Server is operational"
      Tasks: 38 (limit: 4647)
     Memory: 365.4M
        CPU: 5.157s
     CGroup: /system.slice/mysql.service
             └─2675 /usr/sbin/mysqld

Jul 04 17:05:03 ubuntu-jammy systemd[1]: Starting MySQL Community Server...
Jul 04 17:05:05 ubuntu-jammy systemd[1]: Started MySQL Community Server.
vagrant@ubuntu-jammy:~$ sudo systemctl start mysql.service
vagrant@ubuntu-jammy:~$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.37-0ubuntu0.22.04.3 (Ubuntu)

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show tables;
ERROR 1046 (3D000): No database selected
mysql>
mysql> DROP DATABASE IF EXISTS `jwang1568`;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> CREATE DATABASE `jwang1568`;
Query OK, 1 row affected (0.01 sec)

mysql>

mysql> USE `jwang1568`;
Database changed
mysql>


<samples of Python script and related output>
import mysql.connector
mydb = mysql.connector.connect(
     host="localhost",
     user="jwang1568",
     passwd="Root1568",
     auth_plugin='mysql_native_password',
     database="sql_store"
)

def mysqltest(db):
    mycursor = db.cursor()
    mycursor.execute("show databases;")

    print("=== show databases ===")
    for x in mycursor:
        print(x)

    mycursor.execute("use sql_store")
    for x in mycursor:
        print(x)

    mycursor.execute("show tables")
    print("=== show sql_store tables ===")
    for x in mycursor:
        print(x)

if __name__ == "__main__":
    mysqltest(mydb)


*** python output
=== show databases ===
('information_schema',)
('mysql',)
('performance_schema',)
('sql_hr',)
('sql_inventory',)
('sql_invoicing',)
('sql_store',)
('sys',)
=== show sql_store tables ===
('customers',)
('order_item_notes',)
('order_items',)
('order_statuses',)
('orders',)
('products',)
('shippers',)

import os
import MySQLdb

conn = MySQLdb.connect(
    user=os.getenv('MYSQL_USER'),
    passwd=os.getenv('MYSQL_PASSWORD'),
    host=os.getenv('MYSQL_HOST'),
    port=3306
)

cursor = conn.cursor()

criarDatabase = '''SET NAMES utf8;
    CREATE DATABASE `jogoteca` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
'''

cursor.execute(criarDatabase)

criarTabelaJogo = '''use `jogoteca`;
    CREATE TABLE `app` (
        `id` int(11) NOT NULL AUTO_INCREMENT, 
        `nome` varchar(50) COLLATE utf8_bin NOT NULL,
        `categoria` varchar(40) COLLATE utf8_bin NOT NULL,
        `console` varchar (20) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;;
'''

cursor.execute(criarTabelaJogo)

criarTabelaUsuario = '''use `jogoteca`;
        CREATE TABLE `usuario` (
            `id` varchar(8) COLLATE utf8_bin NOT NULL,
            `nome` varchar(50) COLLATE utf8_bin NOT NULL,
            `senha` varchar(100) COLLATE utf8_bin NOT NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
'''

cursor.execute(criarTabelaUsuario)

cursor.close()
conn.commit()
conn.close()

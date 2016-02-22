#
import os
import pymysql


if not os.path.exists('log'):
    os.mkdir('log')

pymysql.install_as_MySQLdb()

#Django默认使用MySQLdb模块,这里是使用pymysql代替
# 假如是使用Anaconda的工具包,不存在就 conda install pymysql先安装
import pymysql
pymysql.install_as_MySQLdb()

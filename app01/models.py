from django.db import models, OperationalError
import pymysql
print("models running")
# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=20)

class Department(models.Model):
    title = models.CharField(max_length=16)

class Role(models.Model):
    caption = models.CharField(max_length=16)

class collection(models.Model):
    source=models.CharField(max_length=64)

class zhihu(models.Model):
    number=models.CharField(max_length=10,default='')
    title=models.CharField(max_length=500,default='')
    href=models.CharField(max_length=500,default='')
    picture_element=models.URLField(max_length=1000,default='')

class github(models.Model):
    author=models.CharField(max_length=20)
    title=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    href=models.URLField(max_length=500)

class bilibili(models.Model):
    rank=models.IntegerField(default=1)
    pic_href=models.CharField(max_length=500,default='')
    title=models.CharField(max_length=500,default='')
    tname=models.CharField(max_length=100,default='')
    link=models.URLField(max_length=500,default='')

class weibo(models.Model):
    rank_pic_href=models.CharField(max_length=500)
    title=models.CharField(max_length=500)
    link=models.URLField(max_length=10000)

class dektinfo(models.Model):
    category = models.CharField(max_length=100)
    item_id = models.CharField(max_length=100)
    activity_name = models.CharField(max_length=100)
    enroll_start_time = models.DateTimeField()
    enroll_end_time = models.DateTimeField()
    active_start_time = models.DateTimeField()
    active_end_time = models.DateTimeField()
    activity_picurl = models.CharField(max_length=200)

    def __str__(self):
        return self.activity_name
class seieeNotification(models.Model):
    name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    href=models.URLField(max_length=100)

class minhang_24h_weather(models.Model):
    Name_of_weather_picture=models.CharField(max_length=100)
    weather_text=models.CharField(max_length=100)
    temperature=models.CharField(max_length=100)
    wind_direction=models.CharField(max_length=100)
    wind_strength=models.CharField(max_length=100)
    hour=models.CharField(max_length=100)
def create_dynamic_model_collection(table_name):
    table_name='collection_'+table_name
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='root', port=3306, db='nis3368')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 创建表格
    create_table_query = """
        CREATE TABLE `{}` (
            id INT PRIMARY KEY AUTO_INCREMENT,
            source VARCHAR(100),
            title VARCHAR(100),
            image_url VARCHAR(200),
            link_url VARCHAR(200)
        )
        """.format(table_name)
    cursor.execute(create_table_query)
    # 提交事务
    db.commit()
    # 关闭游标和数据库连接
    cursor.close()
    db.close()


def delete_dynamic_model_collection(table_name):
    table_name='collection_'+table_name
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='root', port=3306, db='nis3368')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 执行 SQL 语句
    drop_table_query = "DROP TABLE "+"`{}`".format(table_name)+";"
    cursor.execute(drop_table_query)
    # 提交事务
    db.commit()
    # 关闭游标和数据库连接
    cursor.close()
    db.close()
def insert_dynamic_model_collection(table_name,source, title,image_url,link_url):
    # 打开数据库连接
    table_name='collection_'+table_name
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='root', port=3306, db='nis3368')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    insert_data_query = """
        INSERT INTO `{}` (source, title, image_url, link_url)
        VALUES
            ('{}', '{}', '{}', '{}');
        """.format(table_name, source, title, image_url, link_url)
    cursor.execute(insert_data_query)
    db.commit()
    # 关闭游标和数据库连接
    cursor.close()
    db.close()

def create_dynamic_model_shuiyuan(table_name):
    table_name='shuiyuan_'+table_name
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='root', port=3306, db='nis3368')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 创建表格
    create_table_query = """
        CREATE TABLE IF NOT EXISTS `{}` (
            id INT PRIMARY KEY AUTO_INCREMENT,
            `ref` VARCHAR(100),
            `title` VARCHAR(100),
            `posts_count` VARCHAR(100),
            `reply_count` VARCHAR(100),
            `unseen` VARCHAR(100),
            `shuiyuan_category_dict` VARCHAR(100),
            `tags` VARCHAR(100),
            `views` VARCHAR(100)
        )
        """.format(table_name)
    cursor.execute(create_table_query)
    # 提交事务
    db.commit()
    # 关闭游标和数据库连接
    cursor.close()
    db.close()


def delete_dynamic_model_shuiyuan(table_name):
    table_name='shuiyuan_'+table_name
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='root', port=3306, db='nis3368')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 执行 SQL 语句
    drop_table_query = "DROP TABLE "+"`{}`".format(table_name)+";"
    cursor.execute(drop_table_query)
    # 提交事务
    db.commit()
    # 关闭游标和数据库连接
    cursor.close()
    db.close()
def insert_dynamic_model_shuiyuan(table_name,ref, title,posts_count,reply_count,unseen,shuiyuan_category_dict,tags,views):
    # 打开数据库连接
    table_name='shuiyuan_'+table_name
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='root', port=3306, db='nis3368')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    insert_data_query = """
        INSERT INTO `{}` (`ref`, `title`, `posts_count`, `reply_count`, `unseen`, `shuiyuan_category_dict`, `tags`, `views`)
        VALUES
            ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');
        """.format(table_name, ref, title, posts_count, reply_count,unseen,shuiyuan_category_dict,tags,views)
    cursor.execute(insert_data_query)
    db.commit()
    # 关闭游标和数据库连接
    cursor.close()
    db.close()

def create_dynamic_model_calendar(table_name):
    table_name='calendar_'+table_name
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='root', port=3306, db='nis3368')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 创建表格
    create_table_query = """
        CREATE TABLE IF NOT EXISTS `{}` (
            id INT PRIMARY KEY AUTO_INCREMENT,
            title VARCHAR(100),
            starttime VARCHAR(100),
            endtime VARCHAR(100),
            location VARCHAR(100),
            json_detail_url VARCHAR(100)
        )
        """.format(table_name)
    cursor.execute(create_table_query)
    # 提交事务
    db.commit()
    # 关闭游标和数据库连接
    cursor.close()
    db.close()


def delete_dynamic_model_calendar(table_name):
    table_name='calendar_'+table_name
    # 打开数据库连接
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='root', port=3306, db='nis3368')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 执行 SQL 语句
    drop_table_query = "DROP TABLE "+"`{}`".format(table_name)+";"
    cursor.execute(drop_table_query)
    # 提交事务
    db.commit()
    # 关闭游标和数据库连接
    cursor.close()
    db.close()
def insert_dynamic_model_calendar(table_name,title,starttime,endtime,location,json_detail_url):
    # 打开数据库连接
    table_name='calendar_'+table_name
    db = pymysql.connect(host='127.0.0.1', user='root', passwd='root', port=3306, db='nis3368')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    insert_data_query = """
        INSERT INTO `{}` (title, starttime, endtime, location, json_detail_url)
        VALUES
            ('{}', '{}', '{}', '{}', '{}');
        """.format(table_name, title, starttime, endtime, location, json_detail_url)
    cursor.execute(insert_data_query)
    db.commit()
    # 关闭游标和数据库连接
    cursor.close()
    db.close()
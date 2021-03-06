import sqlite3
import xlrd

#　连接数据库
conn = sqlite3.connect('../db.sqlite3')
cur = conn.cursor()

# 清空表
sql = "delete from repo_questions"
cur.execute(sql)
conn.commit()

# 读取数据并入库
workbook = xlrd.open_workbook('questions.xlsx')
sheet_names = workbook.sheet_names()
for sheet_name in sheet_names:
    sheet = workbook.sheet_by_name(sheet_name)
    print(sheet_name)
    # 获取行数
    print(sheet.nrows)
    try:
        for i in range(1, sheet.nrows):
            print(f"正在插入第{i}行")
            title = sheet.row_values(i)[3]
            answer = sheet.row_values(i)[4]
            content = sheet.row_values(i)[5]
            sql = f"""insert into repo_questions ('title', 'content', 'answer', 'status') values ('{title}','{content}','{answer}','True')"""
            cur.execute(sql)
    except Exception as e:
            print('error', e)
    conn.commit()
conn.close()
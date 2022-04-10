import psycopg2
import secret
conn = psycopg2.connect(host=secret.host, dbname=secret.dbname, user=secret.user, password=secret.password, port=secret.port)
cur = conn.cursor()

# 3번 요구사항을 위한 새로운 테이블 생성 로직
#############################################
cur.execute("CREATE TABLE gender_assignment (concept_id integer PRIMARY KEY, concept_name varchar);")

cur.execute("SELECT concept_id,concept_name from concept where domain_id = %s",(secret.imsi,))
data = cur.fetchall()

sqlString = "INSERT INTO gender_assignment (concept_id, concept_name) VALUES (%s, %s);"
for concept_id, concept_name in data:
    cur.execute(sqlString, (concept_id, concept_name,))

cur.execute("CREATE TABLE race_assignment (concept_id integer PRIMARY KEY, concept_name varchar);")

cur.execute("SELECT concept_id,concept_name from concept where domain_id =  %s",(secret.imsi2,))
data = cur.fetchall()

sqlString = "INSERT INTO race_assignment (concept_id, concept_name) VALUES (%s, %s);"
for concept_id, concept_name in data:
    cur.execute(sqlString, (concept_id, concept_name,))
##########################################################
print("complete")
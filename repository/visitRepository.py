from db_init import cur

def gettypeVisit(value):
    sql = "SELECT count(*) from visit_occurrence where visit_concept_id = %s"
    cur.execute(sql,(value,))
    data = cur.fetchone()
    return data

def getgenderVisit(value):
    sql = "SELECT count(*) from visit_occurrence A,person B  where A.person_id = B.person_id and B.gender_concept_id = %s"
    cur.execute(sql,(value,))
    data = cur.fetchone()
    return data

def getageVisit(value):
    sql = "SELECT count(*) from visit_occurrence A,person B  " \
        "where A.person_id = B.person_id and TO_CHAR(B.birth_datetime,'YYYY') BETWEEN  %s AND %s"
    cur.execute(sql,(str(value[0]), str(value[1])))
    data = cur.fetchone()
    return data

def getraceVisit(value):
    sql = "SELECT count(*) from visit_occurrence A,person B  where A.person_id = B.person_id and B.race_concept_id = %s"
    cur.execute(sql,(value,))
    data = cur.fetchone()
    return data

def getethnicityVisit(value):
    sql = "SELECT count(*) "\
          "from visit_occurrence A,person B  "\
          "where A.person_id = B.person_id and B.ethnicity_concept_id = %s"

    cur.execute(sql,(value,))
    data = cur.fetchone()
    return data
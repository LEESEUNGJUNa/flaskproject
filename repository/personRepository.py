from db_init import cur

def getDeathPerson(value): #8532,8507 gender
    sql = "SELECT count(*) from death"
    cur.execute(sql)
    data = cur.fetchone()
    return data

def getGenderPerson(value):
    sql = "SELECT count(*) from person where gender_concept_id = %s"
    cur.execute(sql,(value,))
    data = cur.fetchone()
    return data

def getTotalPerson(value):
    sql = "SELECT count(*) from person"
    cur.execute(sql)
    data = cur.fetchone()
    return data

def getRacePerson(value):
    sql = "SELECT count(*) from person where race_concept_id = %s"
    cur.execute(sql,(value,))
    data = cur.fetchone()
    return data

def getethnicityPerson(value):
    sql = "SELECT count(*) from person where ethnicity_concept_id = %s"
    cur.execute(sql,(value,))
    data = cur.fetchone()
    return data


def getPersoninfos(type, concept_ids,limit,offset):
    sql = ''
    if type == 0:
        sql = "SELECT person_id," \
            "gender_concept_id," \
            "(SELECT concept_name from concept where concept_id = gender_concept_id )," \
            "birth_datetime," \
            "race_concept_id," \
            "(SELECT concept_name from concept where concept_id = race_concept_id )," \
            "ethnicity_concept_id " \
            "from person where  race_concept_id IN %(concept_ids)s " \
            "LIMIT %(LIMIT)s OFFSET %(OFFSET)s"
    else:
        sql = "SELECT person_id,"\
            "gender_concept_id,"\
            "(SELECT concept_name from concept where concept_id = gender_concept_id ),"\
            "birth_datetime,"\
            "race_concept_id,"\
            "(SELECT concept_name from concept where concept_id = race_concept_id ),"\
            "ethnicity_concept_id "\
            "from person where  gender_concept_id IN %(concept_ids)s " \
            "LIMIT %(LIMIT)s OFFSET %(OFFSET)s"
    cur.execute(sql, {'concept_ids': tuple(concept_ids), 'LIMIT': limit, 'OFFSET': offset,})
    data = cur.fetchall()
    return data


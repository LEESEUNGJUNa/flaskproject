from db_init import cur

def getconcepts(keyword, limit,offset):
    sql = "SELECT concept_id,concept_name,domain_id " \
          "from concept " \
          "where concept_name LIKE %(name)s  " \
          "LIMIT %(LIMIT)s OFFSET %(OFFSET)s"
    cur.execute(sql,{'name': '%{}%'.format(keyword), 'LIMIT': limit, 'OFFSET': offset})
    data = cur.fetchall()
    return data

def getconcept_ids(type,keyword):
    if type == 0:
        sql = "SELECT concept_id from race_assignment where concept_name LIKE %(name)s"
    else:
        sql = "SELECT concept_id from gender_assignment where concept_name LIKE %(name)s"
    cur.execute(sql, {'name': '%{}%'.format(keyword)})
    data = cur.fetchall()
    return data
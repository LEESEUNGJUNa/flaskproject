concept_per_page = 50
from repository import conceptRepository

def getconepts(keyword, page):
    limit = concept_per_page
    offset = concept_per_page*page
    ret = conceptRepository.getconcepts(keyword,limit,offset)
    result = mappingConeptinfo(ret)
    return result

def mappingConeptinfo(ret):
    result = []
    for id, name, domain in ret:
        dic = {}
        dic["concept_id"] = id
        dic["concept_name"] = name
        dic["domain"] = domain
        result.append(dic)
    return result


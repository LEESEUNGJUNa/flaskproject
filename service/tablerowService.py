from repository import conceptRepository,personRepository
concept_per_page = 50

class Smartphone:
    def __init__(self, brand, informations):
        self._brand = brand
        self._informations = informations


def getPersoninfo(type, keyword,page):
    limit = concept_per_page
    offset = concept_per_page * page
    concept_ids = conceptRepository.getconcept_ids(type,keyword)
    ret = personRepository.getPersoninfos(type,concept_ids,limit,offset)
    result = mappingPersoninfo(ret)
    return result

def mappingPersoninfo(ret):
    result = []
    for person_id, gender_concept_id,gendername,birth_datetime,race_concept_id,racename,ethnicity_concept_id in ret:
        dic = {}
        dic["person_id"] = person_id
        dic["gender_concept_id"] = gender_concept_id
        dic["gendername"] = gendername
        dic["birth_datetime"] = str(birth_datetime)
        dic["race_concept_id"] = race_concept_id
        dic["racename"] = racename
        dic["ethnicity_concept_id"] = ethnicity_concept_id
        result.append(dic)
    return result
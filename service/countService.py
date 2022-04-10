from repository import personRepository,visitRepository
from datetime import datetime

year = datetime.today().year
ages = [[year-8,year]]
for i in range(1,13):
    ages.append([ages[0][0]-(i*10),ages[0][1]-(i*10)+1])

personfuncarr = []
personfuncarr.append(personRepository.getDeathPerson)      # 0 사망한 환자수
personfuncarr.append(personRepository.getGenderPerson)     # 1 성별 환자수
personfuncarr.append(personRepository.getTotalPerson)      # 2 전체 환자수
personfuncarr.append(personRepository.getRacePerson)       # 3 인종별 환자수
personfuncarr.append(personRepository.getethnicityPerson)  # 4 민족별 환자수

visitfuncarr = []
visitfuncarr.append(visitRepository.gettypeVisit)       # 0 유형별
visitfuncarr.append(visitRepository.getgenderVisit)     # 1 성별
visitfuncarr.append(visitRepository.getageVisit)        # 2 연령
visitfuncarr.append(visitRepository.getraceVisit)       # 3 인종
visitfuncarr.append(visitRepository.getethnicityVisit)  # 4 민족

def getPersonCount(type, value):
    return personfuncarr[type](value)

def getVisitCount(type, value):
    if type ==2:
        value = ages[value]
    return visitfuncarr[type](value)



from flask import Flask
from flask_restful import Api
from controller import countController,conceptController,tablerowController


app = Flask(__name__)
api = Api(app)
api.add_resource(countController.Person, '/count/person')
api.add_resource(countController.Visit, '/count/visit')
api.add_resource(conceptController.concept, '/concept')
api.add_resource(tablerowController.Personinfo, '/personinfo')

if __name__ == '__main__':
    app.run()



# # cur.execute("SELECT person_id,gender_concept_id,birth_datetime,race_concept_id,ethnicity_concept_id from person")
# # data = cur.fetchall()
# # print(data[0])
# # 8532,8507 gender
#
# # cur.execute("SELECT visit_occurrence_id,person_id,visit_concept_id,visit_start_datetime,visit_end_datetime from visit_occurrence")
# # data = cur.fetchall()
# # print(data[0])
# #
# # cur.execute("SELECT person_id,condition_concept_id,condition_start_datetime,condition_end_datetime,visit_occurrence_id from condition_occurrence")
# # data = cur.fetchall()
# # print(data[0])
# #
# # cur.execute("SELECT person_id,drug_concept_id,drug_exposure_start_datetime,drug_exposure_end_datetime,visit_occurrence_id from drug_exposure")
# # data = cur.fetchall()
# # print(data[0])
# #cur.execute("UPDATE test SET num=num+%s where id = %s", (10, 1))
# #cur.execute("SELECT concept_id,concept_name,domain_id from concept where domain_id != %s",("Drug",))
# cur.execute("SELECT concept_id,concept_name,domain_id from concept where concept_id = %s",(8532,))
# data = cur.fetchall()
# print(data[0])
#
# cur.execute("SELECT person_id,death_date from death")
# data = cur.fetchall()
# print(data[0])


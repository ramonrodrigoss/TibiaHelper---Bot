import schedule
import datetime
from boosted_creature import criatura_dia

def hello():
  criatura_dia()
  data = str(datetime.datetime.now())
  print('criatura carregada!'+data) 



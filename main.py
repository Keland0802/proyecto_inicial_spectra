
from etapa3.MasterModel import MasterModel


result = MasterModel().consult("SELECT * FROM tipo_actividades")
if result is not None:
    print(result)
else:
    print("No data found or an error occurred.")
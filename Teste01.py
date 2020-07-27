import sys  
import clr
import pandas as pd  

sys.path.append(r'C:\Program Files (x86)\PIPC\AF\PublicAssemblies\4.0')    
clr.AddReference('OSIsoft.AFSDK')   
  
from OSIsoft.AF import *  
from OSIsoft.AF.PI import *  
from OSIsoft.AF.Asset import *  
from OSIsoft.AF.Data import *  
from OSIsoft.AF.Time import *  
from OSIsoft.AF.UnitsOfMeasure import *  

###setar servidor padrão como PIAPTESTER
piServers = PIServers() 
piServers.DefaultPIServer = piServers["PIAPTESTER"];  
piServer = piServers.DefaultPIServer;
#########################################

###setar o sistema como TESTER e setar o banco de dados criado
afServers = PISystems()
afServers.DefaultPISystem = afServers["PIAPTESTER"]
afServer = afServers.DefaultPISystem
afServer.DefaultDatabase = "AnalisadorOutliers"
###########################################################
Dados = [[0,1,1],[1,1,1]]
df = pd.DataFrame(Dados)

################PADRÃO
#PIServers = PIDATAPRO
#PISystems = PIAPAFPRO
######################

writept = PIPoint.FindPIPoint(piServer, 'Teste')
writeptname = writept.Name.lower() 
val = AFValue()
for i in range(len(df.columns)):
    for j in range(len(df)):
        val.Value = int(df.iloc[j,i])
        print(val.Value)
        writept.UpdateValue(val, AFUpdateOption.Insert, AFBufferOption.DoNotBuffer)



###verificar dados salvos no banco de dados
#pt = PIPoint.FindPIPoint(piServer, "Teste")  
#timerange = AFTimeRange("05-08-2019","*")
#recorded = pt.RecordedValues(timerange, AFBoundaryType.Inside, "", False)  
#for event in recorded:
#    print(event.Value)
#    print(event.Timestamp.LocalTime)
############################################





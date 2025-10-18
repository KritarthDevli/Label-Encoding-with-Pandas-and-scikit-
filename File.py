import pandas as pd
from sklearn.preprocessing import LabelEncoder
df=pd.read_excel("Simple data.xlsx")
df_label=df.copy()
le=LabelEncoder()
df_label['Gender_Encoded']=le.fit_transform(df_label['gender'])
df_label['Pass_Encoded']=le.fit_transform(df_label['passed'])
print("/n LABELL ENCODED DATA")

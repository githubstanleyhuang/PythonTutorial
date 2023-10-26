import kdbai_client as kdbai
session = kdbai.Session(endpoint='https://cloud.kdb.ai/instance/cc7gkbf8cz', api_key='9fab3ebc22-OlNRWKpfZrx9Iip6gKvzi9QaVbZMlnahwb9+jOUp8yiyto8ceVpqx/qksuJYNtq5qSC4HbJAQIqT7KzI'
                        )
session.list()
table=None
try:
    table=session.table('quickstartkdbai')
except:
    pass
if table==None:
    schema = {'columns': [{'name': 'id', 'pytype': 'str'},
                        {'name': 'vectors',
                            'vectorIndex': {'dims': 8, 'metric': 'L2', 'type': 'flat'}}]}
    table = session.create_table('quickstartkdbai',schema)
session.list()


import numpy as np 
import pandas as pd 

ids = ['h', 'e', 'l', 'l', 'o']  # Example ID values
vectors = np.random.rand(40).astype(np.float32).reshape(5,8)
df = pd.DataFrame({"id": ids, "vectors": list(vectors)})

table.insert(df)
table.search(vectors=[[0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]], n=3)
table.drop()







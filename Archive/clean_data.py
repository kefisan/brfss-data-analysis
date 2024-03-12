import pandas as pd

df = pd.read_csv('data.csv', dtype={4: str})

features_to_drop = ['Data_Value_Footnote_Symbol', 'Data_Value_Footnote', 'PriorityArea1',
                    'PriorityArea2', 'PriorityArea3', 'PriorityArea4', 'GeoLocation',
                    'Datasource', 'Data_Value_Type', 'Data_Value_Unit',
                    'Confidence_Limit_Low', 'Confidence_Limit_High', 'CategoryID',
                    'TopicID', 'IndicatorID', 'BreakoutCategoryID', 'BreakOutID', 'LocationID']
df = df.drop(features_to_drop, axis=1)

df = df[~df['LocationDesc'].isin(['Median of all states', 'Washington, DC', 'Washington'])]

df = df.dropna()

cleaned_data = df
cleaned_data.to_csv('cleaned_data.csv', index=False)

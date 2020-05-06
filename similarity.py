import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import re

df = pd.read_csv("Mapped sku - Sheet1.csv")

def similar_description(string):
    pos_vals = []
    numeric_val = 0
    if len(string.split()) == 1:
        ind = df['Distributor Item code'][df['Distributor Item code'] == string].index.tolist()[0]
        return (df['Company Dscription'].loc[ind],1)
    else:
        string = string.lower()
        tokens = string.split()
        for i in tokens:
            if (re.search("[0-9]+x[0-9]+", i)):
                numeric_val = i
                tokens.remove(i)
                new_num = numeric_val.split('x')[1] + "x" + numeric_val.split('x')[0]
            else:
                continue

        for i in df['Company Dscription']:
            if (numeric_val) and (numeric_val in i.lower() or new_num in i.lower()):
                pos_vals.append(i.lower())
        scores = []
        if len(pos_vals) == 0:
            pos_vals = df['Company Dscription']
        for i in pos_vals:
            score = 0
            for j in tokens:
                if j in i.lower():
                    score += 1
            scores.append(score)
        max_score = max(scores)
        pos_results = []
        for i,j in enumerate(scores):
            if j == max_score:
                pos_results.append(pos_vals[i])
        return pos_results, len(pos_results)

print(similar_description("Cementina GY 300x300"))

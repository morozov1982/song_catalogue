import json

import pandas as pd

file_path = 'songs_2023_12_09.xlsx'
df = pd.read_excel(file_path)
df = df.fillna('')

df = df.rename(columns={'Песня': 'title',
                        'Исполнитель': 'performers',
                        'Закольцованность припева': 'chorus',
                        'Тональность': 'key',
                        'Диапазон': 'range',
                        'Аккорды': 'chords',
                        'Темп': 'bpm',
                        'Музыка': 'composers',
                        'Слова': 'authors',
                        'Ссылка': 'links'})

column_headers = df.columns.tolist()


def split_executors(executors):
    if pd.isna(executors) or executors == 'null':
        return None
    else:
        return executors.split(', ')


df['performers'] = df['performers'].apply(split_executors)
df['composers'] = df['composers'].apply(split_executors)
df['authors'] = df['authors'].apply(split_executors)

# selected_rows = df.iloc[[232, 262, 323, 324, 343]]
# json_output = selected_rows.to_json(orient='records')
# data_dict = selected_rows.to_dict(orient='records')

data_dict = df.to_dict(orient='records')

with open('../fixtures/songs.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, ensure_ascii=False, indent=2)

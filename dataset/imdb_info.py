import numpy as np
from scipy.io import loadmat
import pandas as pd
import datetime as date
from dateutil.relativedelta import relativedelta

cols = ['path', 'gender', 'age', 'face_score1', 'face_score2']

imdb_mat = 'imdb_crop/imdb.mat'

imdb_data = loadmat(imdb_mat)

del imdb_mat

imdb = imdb_data['imdb']

imdb_photo_taken = imdb[0][0][1][0]
imdb_full_path = imdb[0][0][2][0]
imdb_gender = imdb[0][0][3][0]
imdb_face_score1 = imdb[0][0][6][0]
imdb_face_score2 = imdb[0][0][7][0]

imdb_path = []

for path in imdb_full_path:
    imdb_path.append('./dataset/imdb_crop/' + path[0])

imdb_genders = []

for n in range(len(imdb_gender)):
    if imdb_gender[n] == 1:
        imdb_genders.append(0)
    else:
        imdb_genders.append(1)


imdb_dob = []

for file in imdb_path:
    temp = file.split('_')[3] # 생년월일
    temp = temp.split('-') # year, month, day로 나눔
    if len(temp[1]) == 1:
        temp[1] = '0' + temp[1] # 1 -> 01로
    if len(temp[2]) == 1:
        temp[2] = '0' + temp[2] # 1 -> 01로

    if temp[1] == '00':
        temp[1] = '01'
    if temp[2] == '00':
        temp[2] = '01'

    imdb_dob.append('-'.join(temp))


imdb_age = []

for i in range(len(imdb_dob)):
    try:
        d1 = date.datetime.strptime(imdb_dob[i][0:10], '%Y-%m-%d')
        d2 = date.datetime.strptime(str(imdb_photo_taken[i]), '%Y')
        rdelta = relativedelta(d2, d1)
        diff = rdelta.years
    except Exception as ex:
        print(ex) # 태어난 해가 확인이 어려운 case도 있음
        diff = -1
    imdb_age.append(diff)

print()

final_imdb = np.vstack((imdb_path, imdb_genders, imdb_age, imdb_face_score1, imdb_face_score2)).T

final_imdb_df = pd.DataFrame(final_imdb)

final_imdb_df.columns = cols


meta = final_imdb_df

meta = meta[meta['face_score1'] != '-inf']
meta = meta[meta['face_score2'] == 'nan']

meta = meta.drop(['face_score1', 'face_score2'], axis=1)

meta = meta.sample(frac=1)

meta.to_csv('imdb_info.csv', index=False)
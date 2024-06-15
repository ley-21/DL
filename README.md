# DL Project: 익명화된 얼굴 이미지의 나이 및 성별 예측 #
노이즈가 첨부 된 얼굴 이미지를 보고 나이와 성별을 예측하는 모델을 구현하였습니다.

<br>

### Description
![image](https://github.com/ley-21/DL/assets/107639414/d858dbac-c7dc-4322-b8b9-cd96c23ae42a)
- `train_config.yaml`: hyperparameter
- `dataset`: folder with images folder and csv file  
- `eval.py`: code for evaluation
- `infer.py`: code for inference
- `train.py`: code for training
- `runs`: folder with checkpoint 
- `make_csv.py`: code for making csv file before train/eval/infer

<br>

### For download directory ###
<a>https://docs.google.com/spreadsheets/d/1IOMaqyrk64KeSpuynB8OJTY740jMw0IxNIsqouAhEGY/edit?gid=0#gid=0<a>

<br>
   
### Requirement
- pip install efficientnet_pytorch

<br>
  
### For Evaluation & Inference
- make_csv.py에서 test dataset의 path, gender, age 정보를 csv 파일로 만든 후 dataset 폴더에 저장<br>
(csv 파일의 이미지 경로대로 test dataset 경로 지정)
- eval.py, infer.py 내의 data 로드시 csv 파일 경로를 넣고 실행





# 2. 더 깊은 학습: 신경망 적용
## 7. 단어 순서를 고려한 의미 분석: 합성곱 신경망
### 4. 다시 텍스트로
#### 1. 케라스로 합성곱 신경망 구현: 자료 준비
- train/ 폴더에는 neg/ 라는 폴더와 pos/라는 폴더가 있으며, 각각에는 각각 부정적 영화평 텍스트 파일들과 긍정정 영화평 텍스트 파일들이 있음. 다음 예제는 이 파일들로부터 훈련 집합을 준비하는 함수. 이 함수는 두 디렉터리에서 파일들을 읽어 들여서 해당 디렉터리에 맞는 분류명(neg면 0, pos면 1)을 부여. 그러면 긍정적 영화평들 다음에 부정적 영화평들이 있는 목록이 만들어지는데 (목록의 각 요소는 분류명과 영화평 텍스트의 쌍), 효과적인 훈련을 위해 이들의 순서를 무작위로 혼합. 분류명에 따라 정렬된 자료로 훈련을 진행 시 나중에 나오는 훈련 견본들 쪽으로 학습이 치우쳐질 가능성이 있음. 특히 momentum 같은 특정 초매개변수를 사용하는 경우에 더욱더 그럴 수 있음.
- ```python
  import glob
  import os
  from random import shuffle

  def pre_process_Data(filepath):
    """
    자료를 전처리하는 함수. 구체적인 전처리 과정은 훈련 자료에 따라 다르겠지만, 최대한 일반적인 형태로 구현
    """
    postive_path = os.path.join(filepath,'pos')
    negative_path = os.path.join(filepath,'neg')
    pos_label = 1
    neg_label = 0
    dataset= []

    for filename in glob.glob(os.path.join(positive_path,'*.txt')):
        with open(filename,'r') as f:
            dataset.append((pos_label,f.read()))
    for filename in glob.glob(os.path.join(negative_path,'*.txt')):
        with open(filename,'r') as f:
            dataset.append((neg_label,f.read()))

    shuffle(dataset)
    return dataset
  ```
- 다음은 이 함수를 호출, 훈련 집합을 생성, 그 첫 견본을 출력하는 예시. 전처리 함수가 영화평들을 무작위로 뒤섞기때문에, 실제 실행 시마다 출력 예시가 다른 출력이 나올 수 있으나, 문제가 되지 않음. dataset의 각 튜플(두값쌍)은 분류명과 형화평으로 이루어지는데, 분류명은 해당 영화평에 담긴 감정을 의미. 1은 긍정적 감정, 0은 부정적 감정. 훈련과정에서 이 분류명은 해당 견본의 목푯값, 즉 바람직한 예측값으로 사용
- ```python
  dataset = pre_process('<영화평 말뭉치 디렉터리>>/aclimdb/train')
  dataset[0]
  ```
  
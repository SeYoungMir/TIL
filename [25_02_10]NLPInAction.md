# 2. 더 깊은 학습: 신경망 적용
## 5. 신경망 첫걸음: 퍼셉트론과 역전파
### 1. 신경망의 구성 요소
#### 7. 케라스: 신경망 파이썬 구현
- 신경망을 훈련
- ```python
  model.fit(x_train,y_train,epochs = 100)
  ```
- 예시에서는 작은 자료 집합으로 모형을 거듭 적합. 모형이 수렴. 견본들로도 모형이 XOR의 규칙을 학습. 이런 것을 자연어 처리에도 적용.
- ```python
  model.predict(x_train)
  model.predict_classes(x_train0)
  ```
- 훈련된 모형으로 predict를 호출 시 훈련 집합의 견본들에 대해 정확한 답을 예측함. predict_classes는 원본 출력값을 분류명(이 경우 0 또는 1)으로 해석한 결과를 출력. 두 결과 모두, 훈련 집합에 대한 모형의 정확도가 100%임을 보여줌. 정확도가 예측 모형의 품질에 대한 최선의 측도는 아니지만, 예제에서는 이걸로 충분. XOR 모형을 파일로 저장
- ```python
  import h5py
  model_structure = model.to_json()
  with open("basic_model.json","w") as json_file:
        json_file.write(model_structure)
  model.save_weights("basic_weights.h5")
  ```
- 케라스는 이러한 파일들로부터 신경망을 다시 생성하고 가중치들을 불러오는 메서드를 제공. 따라서같은 신경망을 매번 다시 훈련할 필요가 없음. 이러한 기능은 덩치가 큰 신경망에서 더욱 더 유용. 예제의 XOR 모형은 훈련에 단 몇 초밖에 걸리지 않으므로 매번 훈련하는 것이 별로 부담이 되지 않지만, 이후 예제 신경망들은 훈련에 몇 분이 걸릴수도 있고 몇 시간이 걸릴수도 있음. 하드웨어와 모형의 복잡도에 따라 훈련에 며칠이 걸릴수도 있음.
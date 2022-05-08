# Text Image Annotation Competition

> [boostcamp AI Tech](https://boostcamp.connect.or.kr) - Level 2: CV_02 Bucket Interior

### Results

  * **Test dataset for public leaderboard**
    * F1 score: 0.7059 / test precision: 0.7972 / test recall: 0.6333
  * **Test dataset for private leaderboard**
    * F1 score: 0.6120 / test precision: 0.7242 / test recall: 0.5299

### Task

#### Data Annotation Task Specifications

  * **주어진 모델만을 사용하며 주어진 글자 이미지에서 글자 영역을 검출**
    * **Subtask 1: 데이터셋 구축**
      * Community annotation
    * **Subtask 2: 데이터셋 확장**
      * 외부 데이터셋 도입
    * **Subtask 3: 개별 글자 영역 검출**
      * Bounding box suggestion

#### Given Image Dataset Specifications

  * **Train: ICDAR17_Korean + boostcamp_Upstage**
    * ICDAR17_Korean: 536장
    * boostcamp_Upstage: community annotated images
  * **Test: Upstage**
  * **Dataset ratio**
    * Test dataset for public leaderboard: 50% of test dataset
    * Test dataset for private leaderboard: 50% of test dataset

#### Imported Image Dataset List

  * ICDAR19_Korean
  * ICDAR19_English
  * [AI Hub: 야외 실제 촬영 한글 이미지](https://aihub.or.kr/aidata/33985)

#### Main Difficulties

  * **Tight competition schedule**
    * Community annotation 때문에 학습 데이터가 뒤늦게 제공됨
    * 대회 기간이 2주로 짧았음
  * **Fixed model**
    * 주어진 모델과 주어진 pretrained weight의 사용만이 허가됨
  * **Small storage capaticy**
    * GPU 서버의 디스크 용량이 100 GB였음
    * 공개되어 있는 한글 이미지 데이터셋들의 크기가 커서 일부만을 뽑아 사용해야 했음
  * **Bounding box noise**
    * 많은 글자 사진의 글자 영역 annotation이 정확하지 않았음
    * Community annotation이 진행된 데이터셋의 경우 annotation의 일관성이 낮았음
  * **Errorneous baseline code**
    * 반드시 사용되어야 하는 베이스라인 코드에 정사각형 이미지의 경우 annotation을 무시하는 오류가 있었는데, 너무 늦게 보고되었음
  * **Annotation format mismatch**
    * 반드시 사용되어야 하는 베이스라인 코드가 일반적으로 사용되지 않는 annotation format을 요구함

### Approaches

  * **Dealing with tight competition schedule**
    * Ensemble 과정을 생략하고 각자 데이터셋을 다르게 구성함
    * Hyperparameter tuning 과정을 생략하고 각자 learning rate를 다르게 설정함
  * **Dealing with fixed model**
    * Learning rate scheduler로 MultiStepLR과 CosineAnnealingLR을 도입하여 비교 실험을 진행함
    * 일부 실험에서 color jittering augmentation을 도입함
  * **Dealing with small storage capacity**
    * AI Hub 데이터셋을 Tiny, Small, Large 크기로 변형하여 사용함

### Technical Specifications

> 가장 높은 f1 score를 달성한 모델에 대해서만 기록

  * Model: VGG-based pretrained EAST
  * Dataset split: No validation set split(train set 100%)
  * Metric: DetEval(split 20% penalty)

### Thoughts

> 좋은 데이터와 augmentation이 확실히 중요하다는 것을 느꼈다. 특히, 공개된 데이터셋마다 annotation 규칙이 다르기 때문에, 그냥 포맷만 맞춰서 학습시킬 경우 성능이 떨어질 수도 있음을 알게 되었다. 그리고 성능 관점에서는 train과 test에 사용하는 데이터셋의 분포가 비슷한 것이 좋을 것이지만, 여기서 분포가 무엇인지는 결국 inductive bias임을 알게 되었다. <br>
> 이번 대회는 test 데이터셋이 아예 공개되지 않은 대회였다. 특히 private test 데이터셋과 public test 데이터셋의 분포가 많이 달랐는지, 리더보드에 큰 변화가 있었다. 학습 과정에서 train 데이터셋의 분포가 test 데이터셋과 유사하면 지금 학습이 잘 되고 있는지를 확인하기 좋겠지만, 그것보다는 test 데이터셋이 실제 서비스에서 만날 수 있는 데이터들과 유사한지가 generalization 관점에서 더 중요하다는 생각이 들었다. 다양성과 유사성의 균형이 잡힌 데이터셋 설계를 고민해 볼 필요가 있겠다. <br>
> Precision은 올라가고 recall은 떨어지는 경우나, 그 반대의 경우는 어떤 의미인지 고민해 볼 수 있었다. 여러 가지 metric을 사용하는 것이 실무에서 유용할 것이라는 생각이 들었다. <br>
> LR scheduler의 경우, CosineAnnealingLR이 MultiStepLR보다 성능 면에서 유리하다는 것을 확인했다. Data augmentation은 annotation을 해치치 않도록 사용하면 유용함을 확인했다.

### How To Train

```shell
python main.py
```

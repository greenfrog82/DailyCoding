# 파도 센서

 친환경 에너지 기술을 연구개발하고 있는 구름에너지에서는 조수 발전에 대한 실험을 하기 위하여 인프라를 구축하고 있다. 실험 장소에는 다섯 개의 센서를 설치하였는데, 모든 센서의 위치는 각각 다르다. 이 센서들은 자신에게 도달하는 일정 강도 이상의 물결파를 감지하면 알림음을 발생시킨다. 물결파는 발생하는 지점을 중심으로 원의 형태로 커져나가며 일정 반지름 이상 퍼져나가면 센서에서 감지할 수 없는 수준으로 약해진다.

![./ex.jpg](./ex.jgp)


<파도의 한 시점(왼쪽)과 시간이 지나 물결파가 퍼지다 센서에 감지된 시점(오른쪽)>



 구름 에너지에서는 조금 더 정확한 실험을 위하여 물결파를 인위적으로 여러 번 발생시켜가며 센서로 감지하고자 한다. 구름 에너지의 신입 연구원인 당신은 발생한 물결파에 대하여 가장 먼저 물결파를 탐지하는 센서는 어느 센서인지 미리 예측하는 프로그램을 작성해야 한다. 물결파가 발생한 중심과 감지할 수 있는 최대 유효 반지름이 입력으로 주어질 때, 어떤 센서가 가장 먼저 물결파를 감지할 수 있는지 판단하는 프로그램을 작성하시오. 모든 센서와 물결파의 중심은 이차원 평면상의 좌표로 위치가 주어진다.



## 입력 형식
 입력 데이터는 총 6줄에 걸쳐서 주어진다.

 첫 줄에는 물결파가 발생한 위치와 유효 반지름이 X Y R 형식으로 주어진다.

* X와 Y는 물결파가 발생한 중심점의 좌표를 나타내는 절대값이 1,000이하인 정수다.
* R은 물결파가 감지될 수 있는 최대의 유효 반지름을 나타내는 1,000이하의 자연수다.
 이후 총 5줄에 걸쳐서 다섯 개의 센서에 대한 위치가 X Y형식으로 주어진다. 1번 센서, 2번 센서, ... , 5번 센서 순으로 위치가 주어진다.

* X와 Y는 각 센서의 위치를 나타내는 절대값이 1,000이하인 정수다.
* 두 개의 센서가 같은 위치에 있거나 물결파의 중심과의 거리가 같은 경우는 존재하지 않는다.


## 출력 형식
 가장 먼저 물결파를 감지하게 될 센서의 번호를 출력한다. 만약 아무 센서도 물결파를 감지할 수 없다면 -1을 출력한다.


## 테스트

#### 입력 1
-1 0 1  
2 2   
-2 -2  
0 0   
-1 -2   
1 2   

#### 출력 1
3

#### 입력 2
-9 -2 10   
9 -5   
8 10   
-5 -9   
2 4   
-5 9   

#### 출력 2
3

#### 입력 3
-21 6 19    
13 2    
-4 9    
-12 -13  
13 19  
-15 -9  

#### 출력 3
5
class Car:
    color=""
    speed=0
    count=0

    def __init__(self):
        self.speed=0 # speed를 instance variable로 -> 설계도
        Car.count+=1 # count를 Class variable로 -> 자동차 샘플을 만들음, 저장공간 공유

myCar1=Car()
myCar1.speed=30
print("자동차 1의 현재 속도는 %dkm, 생산된 자동차는 총 %d대 입니다."%(myCar1.speed,Car.count))
myCar2=Car()
myCar2.speed=60
print("자동차 2의 현재 속도는 %dkm, 생산된 자동차는 총 %d대 입니다."%(myCar2.speed,Car.count))

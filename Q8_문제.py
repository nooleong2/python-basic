# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [Code]
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        if self.deal_type == "월세":
            print("{0} {1} {2} {3} {4}년".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))
        else:
            print("{0} {1} {2} {3}억 {4}년".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

apt = House("강남", "아파트", "매매", 10, 2010)
op = House("마포", "오피스텔", "전세", 5, 2007)
villa = House("송파", "빌라", "월세", "500/50", 2000)

apt.show_detail()
op.show_detail()
villa.show_detail()



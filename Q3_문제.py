# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# ex) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수 + "!" 로 구성
#                 (nav)         (5)           (1)         (!)
# 정답 : 생성된 비밀번호 : nav51!

url = "http://naver.net"
url = url.replace("http://", "")
url = url[:url.index(".")]
password = url[:3] + str(len(url)) + str(url.count("e")) + "!"
print(password)

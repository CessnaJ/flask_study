from bs4 import BeautifulSoup

html_string = '<div class="w9QyJ vI8SM"><div class="y6tNq"><div class="A_cdD"><em>운영 중</em><span class="U7pYf"><time aria-hidden="true">18:00에 운영 종료</time><span class="place_blind">18시 0분에 운영 종료</span></span></div></div></div>'

soup = BeautifulSoup(html_string, 'html.parser')
status = soup.find('em').text
time1 = soup.find('time').text
time2 = soup.find('span', {'class': 'place_blind'}).text

print(status) # '운영 중'
print(time1) # '18:00에 운영 종료'
print(time2) # '18시 0분에 운영 종료'



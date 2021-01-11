site = "http://naver.com/index.do"

site1 = site.replace("http://","")
print(site1)
site1 = site1[:site1.index(".")]
print(site1)
pwd = site1[:3]+str(len(site1))+str(site.count("e"))+"!"
print(f"{site}의 비밀번호는 {pwd}입니다.")
print(f"{site}의 비밀번호는 {pwd}입니다.".format(site,pwd))
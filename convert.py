import json
from collections import defaultdict

# companies.json 파일 읽기
with open('companies.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

companies = data['companies']

# README.md로 변환할 내용 생성
markdown_content = '''# list-of-companies-using-dotnet

.NET 기술을 사용하는 국내 기업 정보

 
## Description
- 기업 정보를 채용 링크와 함께 기록합니다. 
- 기업 정보 기록 및 공유가 목적이므로 채용이 끝나도 링크를 삭제하지 않습니다. (링크가 유효하지 않을 수 있습니다.)
- 기업 정보 추가 및 수정은 PR 부탁드립니다.
- 이제 [사이트](https://hyolog.github.io/)에서도 확인 가능합니다.

 
## PR Convention
- companies.json 파일에 아래 항목을 포함한 기업정보 추가 후 PR을 요청합니다.
  - "name"(회사명)
  - "location"(회사 주소)
  - "businessGroup"(업종)
  - "recruitUrl"(채용공고 링크)
- 회사 주소는 [카카오맵](https://map.kakao.com/)을 기준으로 입력합니다.
- 업종은 [전자공시시스템](https://dart.fss.or.kr/dsae001/main.do)에서 회사명 검색 후 확인할 수 있습니다.

 
## List of Companies

'''

# 업종별로 기업 그룹화
grouped_companies = defaultdict(list)
for company in companies:
    grouped_companies[company['businessGroup']].append(company)

# 업종별 회사 목록 추가 (가나다순 정렬)
for business_group in sorted(grouped_companies.keys()):
    markdown_content += f"### {business_group}\n"
    # 그룹 내 기업들을 이름 순으로 정렬
    sorted_companies = sorted(grouped_companies[business_group], key=lambda x: x['name'])
    for company in sorted_companies:
        markdown_content += f"- [{company['name']}]({company['recruitUrl']})\n"
    markdown_content += "\n"

# README.md 파일로 저장
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(markdown_content)

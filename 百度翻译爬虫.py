import requests
url = 'https://fanyi.baidu.com/sug'
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
}
choice = 'yes'
while choice=='yes':
    kw = input('请输入要翻译的单词：')
    data = {
        'kw':kw
    }
    response = requests.post(url=url,headers=headers,data=data).json()
    print(response)
    choice = input('若要继续翻译，请输入“yes”：')

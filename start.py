import requests
import time

api_key = "YOUR_API_KEY" # Api key
reklam_tipi = 1
# 5 -> Film/Dizi
# 4 -> Spor/Futbol
# 3 -> Oyun/İndirme
# 2 -> Diğer
# 1 -> Yetişkin içerik +18
def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    print(log_text)
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()

log('Program başladı.')
log('Yapımcı: Can')
log('GitHub: https://github.com/fastuptime')
with open('links.txt', 'r', encoding='utf-8') as f:
    links = f.read()
    links = links.split('\n')
    for link in links:
        
        try:
            r = requests.get('https://ay.live/api/?api=' + api_key + '&url=' + link + '&alias&ct=' + str(reklam_tipi))
            if r.status_code == 200:
                json_data = r.json()
                if json_data['status'] == 'success':
                    log(link + ' başarılı bir şekilde kısaltıldı. Kısa link; ' + json_data['shortenedUrl'])
                    #file = 'Normal URL: ' + link + ' Short URL: ' + json_data['shortenedUrl']
                    file = json_data['shortenedUrl'] + '|' + link
                    with open('shortened_links.txt', 'a', encoding='utf-8') as f:
                        f.write(file + '\n')
                else: 
                    log(link + ' kısaltılırken hata oluştu. ' + json_data)
            else:
                log(link + ' kısaltılamadı')
            time.sleep(3)
        except:
            log(link + ' kısaltılamadı')
            time.sleep(3)
                
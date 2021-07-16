"""
Beautiful Soup from Freecodecamp.org

Scrapping timesjobs.com yang hanya menampilkan job yang sudah beberapa hari di post
"""

from bs4 import BeautifulSoup
import requests
import time
"""

# pada code dibawah ini hasil yang akan di return adalah status code (200, 404, 500, etc)
html_text = requests.get('https://www.jobstreet.co.id/id/job-search/python-jobs/')
print(html_text)

"""
print('Cari Skill yang tidak ada pada!!')
cari_skill = input('> ')
print(f'Filtering {cari_skill}')

def find_jobs():
# pertama akses dulu link nya
# untuk mengambil kode html dari suatu web maka tambahkan atribut 'text' setelah link
    try:
        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    except:
        print('Connection Error')
        quit()
    # masukkan kode html ke dalam instance BeautifulSoup
    soup = BeautifulSoup(html_text, 'lxml')

    #karena semua card yang berisi loker pasti memiliki elemen dan class yang sama maka ambil card yang pertama saja agar load tidak lama
    #output yang akan di dapat adalah isi dari tag dengan class yang dicari
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        #cari tag yang berisi kapan postingan di post
        published_date = job.find('span', class_ = 'sim-posted').span.text

        if 'few' in published_date:

            #cari tag yang berisi nama perusahaan yang membuka loker lalu ambil value dari tag nya menggunakaan atribut 'text'
            #untuk menghapus whitespace bisa menggunakan function 'replace()' dan isi parameternya
            company_name = job.find('h3', class_ = 'joblist-comp-name').text

            #cari tag yang berisi skill yang diperlukan untuk melamar pekerjaannya
            #karena terdapat beberapa tag maka akses dulu tag parent nya
            job_detail = job.find('ul', class_ = 'list-job-dtl clearfix')

            #cari spesific tag yang berisi skill yang dibutuhkan lalu ambil value nya
            skills = job_detail.find('span', class_ = 'srp-skills').text.replace(' ', '')

            #ambil tag yang memiliki link
            #untuk akses 'href' atau yang lain bisa menggunakan ['namanya']
            more_info = job.header.h2.a['href']

            if cari_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name : {company_name.strip()}\n')
                    f.write(f'Required Skills : {skills.strip()}\n')
                    f.write(f'More Info : {more_info}\n')
                print(f'File Saved : {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Time wait {time_wait} seconds')
        time.sleep(time_wait) 







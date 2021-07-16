"""
Beautiful Soup from Freecodecamp.org

Local HTML
"""

from bs4 import BeautifulSoup

#buka file html dalam mode 'read'
with open('home.html', 'r') as html_file:

    #full html dimasukkan ke dalam variabel
    #read() digunakan untuk mengambil semua data pada file
    content = html_file.read()

    #instance dari BeautifulSoup yang mengambil 
    # parameter markup = content
    # dan features yang digunakan adalah 'lxml'  
    soup = BeautifulSoup(content, 'lxml')
    
    # Mencari spesifik tag pada code html yang diambil
    # function find() berguna untk mencari tag yang dicari namun hanya menampilkan tag yang muncul pertama kali
    tag_awal = soup.find('h5')
    # print(tag_awal)
"""
    # function find_all() berguna untuk menampilkan semua tag yang dicari dan mereturn dalam bentuk list
    all_tag = soup.find_all('h5')
    
    #menampilkan hanya text yang ada pada tag saja
    #gunakan atribut 'text'
    for course in all_tag:
        print(course.text)
"""
#Buat List yang menampung nama course dan harga nya
course_and_prices = []

    #mengambil course title and price
    #ambil dulu isi card course nya
course_tags = soup.find_all('div', class_ = 'card')

#karena tag div ada 3 maka akses masing masing div menggunakan for loop
for course in course_tags:

    # Masukkan tag 'h5' yang merupakan sebuah title ke dalam variable
    # atribut text digunakan untuk mengakses value dari tag tersebut
    title = course.h5.text

    # Masukkan tag 'a' yang merupakan tag untuk harga ke dalam variable
    # atribut text digunakan untuk mengakses value dari tag tersebut
    price = course.a.text

    # Masukkan title dan price ke dalam list agar bisa ditampung ke list lain
    newList = [title, price]

    #tambahkan list yang berisi title dan price ke dalam list yang menampung semua title dan price
    course_and_prices.append(newList)

for data in course_and_prices:
    print(f'Course Name : {data[0]}')
    price = data[1].split(' ')
    harga = price[-1]
    print(f'Price : {harga}')
    print('\n')
    
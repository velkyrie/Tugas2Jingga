# Tugas 2 - Vladi Jingga Mentari (2106635631)

[Akses tugas di aplikasi Heroku (bagian katalog)](tugas2jingga.herokuapp.com/katalog)

## Bagan _Request and Response Cycle_ Django 

![Bagan Request and Response Cycle](https://user-images.githubusercontent.com/52811288/190280167-bbcca061-2a00-4649-b82e-199f73d8d0d9.png)

Ketika ada _HTTP request_ yang masuk dari _client/user_, Django memiliki cara kerja tersendiri untuk merespon _request_ tersebut.
1. _Request_ dikirim oleh _client/user_, masuk ke server Django, dan diproses melalui URL Configuration (URLconf) `urls.py`. urls.py berisikan kode yang digunakan oleh Django untuk mencocokkan _request_ URL untuk mencari _views_ yang cocok. Lebih spesifiknya, URL yang di-_request_ akan dicocokkan dengan _path_ di potongan kode `urlpatterns`
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls'))
]
```

2. Setelah URL dicocokkan, _request_ akan diteruskan ke `views.py`, yang berisi kode untuk mendefinisikan _request_
3. Jika terdapat proses atau aktivitas yang melibatkan Database, maka `views.py` akan memanggil _query_ ke `models.py` dan melanjutkannya ke Database untuk memproses data
4. Setelah data diproses, respon berupa hasil _query_ akan dikembalikan ke `views`
5. Setelah _request_ selesai diproses, `View` akan memilih dan memetakan `file html` yang sudah didefinisikan sebelumnya di _return block_ `views.py`
6. Tampilan web dalam bentuk HTML dikembalikan ke _user/client_ sebagai respon dari _request_ 

## Mengapa kita menggunakan _Virtual Environment?_

_Virtual environment_ adalah alat yang membantu memisahkan/mengisolasi tiap proyek Django ke dalam _environment_ masing-masing. _Virtual environment_ digunakan untuk menghindari konflik antar _dependencies_ (_packages_ atau _library_  eksternal) yang digunakan. Konflik dapat terjadi karena secara _default_, setiap _project_ akan menggunakan _directories_ yang sama untuk menyimpan dan mengambil _site packages_, dan tiap proyek dapat menggunakan versi _dependencies_ yang berbeda. Hal ini menjadi masalah karena Python tidak bisa membedakan versi pada direktori _site-packages_. Selain itu, _virtual environment_ akan mengisolasi tiap proyek ke _environment_-nya sendiri sehingga perubahan yang dilakukan pada satu proyek tidak akan memengaruhi proyek lainnya. Oleh karena itu, penggunaan _virtual environment_ pada tiap proyek Django lebih baik dilakukan. 

Pengembangan proyek Django dan Python pada umumnya sebenarnya bisa dilakukan tanpa _virtual environment_, akan tetapi akan sulit jika memiliki banyak proyek karena konflik bisa terjadi dan tentunya akan menghambat proses pengembangan.

## Penjelasan Implementasi

1. Pada `views.py`, buat fungsi untuk melakukan _request_ yaitu untuk mengambil data dari _models_ dan mengembalikannya dalam bentuk HTML
```python
from katalog.models import CatalogItem

def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = { 
        'list_item': data_barang_katalog,
        'nama': 'Vladi Jingga Mentari',
        'student_id': '2106635631'
    }
    return render(request, "katalog.html", context)
```
Untuk menghubungkan View dan data dari Model, penting meng-_import_ data dari model. Data diambil dari:
```python
 data_barang_katalog = CatalogItem.objects.all()
 ```
 2. Fungsi yang telah dibuat di `views.py` dipetakan dengan kode untuk _routing_ pada `urls.py` baik pada [katalog](katalog) maupun [project_django](project_django). Dengan kode _routing_, fungsi `show_katalog(request)` akan dipanggil ketika _client/user_ melakukan _request_ terhadap URL katalog
 - Tambahkan di `urlpatterns` pada direktori [katalog](katalog)
 ```python
    path('', show_katalog, name='show_katalog'),
 ```
 - Tambahkan di `urlpatterns` pada direktori [project_django](project_django)
 ```python
     path('katalog/', include('katalog.urls'))
 ```
 3. Pemetaan data yang didapatkan ke HTML dilakukan dengan menambahkan sintaks `context` pada _return block_ fungsi `show_katalog(request)` di `views.py`
 ```python
 return render(request, "katalog.html", context)
 ```
 4. Deployment dilakukan dengan membuat aplikasi Heroku. Untuk _set-up_, tambahkan _repository secret_ di Github dengan pasangan nama aplikasi dan API key akun Heroku. Setelah _set-up_ selesai, lakukan _command_ `add`, `commit`, `push`, dan aplikasi akan dideploy.

# Tugas 3 - Vladi Jingga Mentari (2106635631)

https://tugas2jingga.herokuapp.com/mywatchlist/html/

## Apa saja perbedaan JSON, XML, dan HTML?

**HTML**
HTML (_Hyper Text Markup Language_) adalah bahasa _markup_ yang digunakan sebagai _building block_ untuk membangun sebuah web. HTML digunakan untuk men-_display_ data dalam berbagai bentuk (teks, gambar, dsb.) di internet. HTML juga mendefinisikan arti dan struktur dari sebuah konten web. 

HTML hanya menampilkan data, sedangkan data yang ditampilkan oleh HTML dapat berupa JSON atau HTML.

**JSON**
JSON (_Javascript Object Notation_) adalah format yang digunakan untuk menyimpan dan mentransmisikan data, yaitu sebagai pasangan _key-value_ dan _array_. JSON didasari oleh bahasa JavaScript dan cenderung mudah untuk dipahami dan di-_generate_. 

**XML**
XML (_eXtensible Markup Language_) adalah bahasa _markup_ yang digunakan untuk menyimpan data. Berbeda dengan HTML yang juga merupakan bahasa _markup_, XML tidak memiliki _tags_ yang sudah terdefinisi. XML adalah format berbasis teks sederhana untuk merepresentasikan informasi terstruktur. Selain itu, XML juga menyediakan _namespace support_.


| JSON        | XML           | HTML  |
| ------------- |:-------------:| -----:|
| digunakan untuk men-_carry_ data    | digunakan untuk men-_carry_ data | digunakan untuk menampilkan data |
| diturunkan dari JavaScript     | diturunkan dari SGML      |   diturunkan dari SGML |
| dinamik | dinamik      |    statis |
| tidak menggunakan tags | menggunakan tags yang didefinikan user      |    menggunakan tags _pre-defined_ |
| tidak men-_support _comments_ | men-_support_ _comments_    |  men-_support_ _comments_  |

## Mengapa kita memerlukan _Data Delivery_ dalam implementasi platform?

Penggunaan data dapat dibilang tak terpisahkan dari implementasi platform. _Data delivery_ sangat penting karena diperlukan untuk mengirimkan data dari satu stack ke stack lainnya. Contohnya, dalam implementasi platform, _Client_ dapat me-_request_ data ke _server_ dan data tersebut perlu dikirim ke _client_ sebagai respon. _Data delivery_ juga dapat menghemat ruang penyimpanan karena umumnya ada beberapa _file_ atau data yang tidak disimpan di _server_ melainkan di-_generate_ oleh program dengan XML dan JSON.

## Implementasi Tugas 3
1. Buat aplikasi Django **mywatchlist** dengan _command_ `python3 manage.py startapp mywatchlist`
2. Di [settings.py] pada project_django, tambahkan app baru **mywatchlist** ke list `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'example_app',
    'katalog',
    'mywatchlist',
]
```
3. Implementasi _routing_ pada aplikasi baru agar bisa diakses _localhost_ dengan mendaftarkan **mywatchlist** ke list `urlpatterns` di [project_django/urls.py].
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('katalog/', include('katalog.urls')),
    path('mywatchlist/', include('mywatchlist.urls')),
]
```
4. Buat `class` model di [mywatchlist/models.py] 
``` python
class MyWatchlist(models.Model):
    watched = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    release_date = models.CharField(max_length=255)
    review = models.TextField()
 ```
 5. Lakukan `makemigrations` dan `migrate` ke _database_ Django lokal
```python
python3 manage.py makemigrations
```
```python
python3 manage.py migrate
```

6. Buat _folder_ `fixtures` dan buat _file_ JSON yang memuat data _watchlist_. 

```python
[
    {
        "model": "mywatchlist.mywatchlist",
        "pk": 1,
        "fields": {
            "watched": true,
            "title": "Everything Everywhere All At Once",
            "rating": 4.8,
            "release_date": "June 22, 2022",
            "review": "So far the best execution for a Multiverse theme. An emotional rollercoaster, with top notch humor and scenes that will make you cry multiple times. "
        }
    }
]
``` 
Buat data seperti di atas untuk paling tidak 10 film.

7. _Load_ data dengan _command_
`python3 manage.py loaddata initial_mywatchlist_data.json`
8. Buat fungsi dalam `views.py` untuk me-_render_ halaman web dengan data dan implementasikan juga fungsi untuk mengembalikan data dalam XML dan JSON.
```python
from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_watchlist = MyWatchlist.objects.all()
    context = { 
        'list_item': data_watchlist,
        'nama': 'Vladi Jingga Mentari',
        'student_id': '2106635631'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
9. Buat folder _templates_ dan _file_ HTML di dalam folder tersebut, lalu isi sesuai dengan _fields_ yang telah dibuat di [models.py]
```python3
{% extends 'base.html' %}

 {% block content %}

  <h1>Assignment 3 PBP/PBD</h1>

  <h5>Name: </h5>
  <p>{{nama}}</p>

  <h5>Student ID: </h5>
  <p>{{student_id}}</p>

  <table>
    <tr>
      <th>Watched</th>
      <th>Title</th>
      <th>Rating</th>
      <th>Release Date</th>
      <th>Review</th>

    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for item in list_item %}
    <tr>
        <th>{{item.watched}}</th>
        <th>{{item.title}}</th>
        <th>{{item.rating}}</th>
        <th>{{item.release_date}}</th>
        <th>{{item.review}}</th>
    </tr>
    {% endfor %}
  </table>

 {% endblock content %}
```
10. Implementasi _routing_ URL dalam [mywatchlist/urls.py] untuk tiap path HTML, JSON, dan XML dan masukkan fungsi yang dibuat di views.py pada tiap _path_.
```python
    path('html/', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
 ```
 11. Deploy dengan melakukan `git add`, `commit`, dan `push`.

## Screenshot dari Postman
<img width="1434" alt="Screen Shot 2022-09-22 at 11 36 54" src="https://user-images.githubusercontent.com/52811288/191659412-b97f4b74-1ce5-452e-b39d-672d83217752.png">
<img width="1440" alt="Screen Shot 2022-09-22 at 11 37 23" src="https://user-images.githubusercontent.com/52811288/191659458-d8ada279-ad6e-422a-845a-6977fcafed5d.png"><img width="1435" alt="Screen Shot 2022-09-22 at 11 37 48" src="https://user-images.githubusercontent.com/52811288/191659495-a61610ae-814a-4286-9e3d-6cc8d2cba915.png">

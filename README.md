# Lab 1 - Vladi Jingga Mentari (2106635631)

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

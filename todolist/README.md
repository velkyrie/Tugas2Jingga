# Tugas 4 - Vladi Jingga Mentari (2106635631)

https://tugas2jingga.herokuapp.com/todolist

### CSRF Token
`{% csrf_token %}` diimplementasikan untuk menghindari serangan _Cross Site Request Forgery attack_ pada web berbasis Django. 
`{% csrf_token %}` men-_generate_ suatu _token_ unik dan rahasia pada sisi server ketika me-render halaman serta memastikan untuk melakukan _cross-check_ 
untuk _request_ _form_ yang masuk. Jika _request_ yang masuk tidak menganduk token (berarti tidak berasal dari _server_), _request_ tersebut tidak akan dieksekusi. 
Secara spesifik, `{% csrf_token %}` digunakan pada _template_ yang menggunakan POST form di dalam URL internal. 
Tidak adanya CSRF Token pada _form_ dapat membuka celah untuk serangan CSRF pada halaman web, contohnya seperti _form_ yang bukan berasal dari server yang dapat 
membuat user melakukan _action_ yang tidak terduga dan tidak diinginkan. Akan tetapi, Django akan secara otomatis memberikan 403 Forbidden Error.
<img width="794" alt="Screen Shot 2022-09-29 at 10 28 47" src="https://user-images.githubusercontent.com/52811288/192932295-730af3fe-734d-4cea-b643-34ef311e6180.png">


### Elemen <form> secara manual?
Kita dapat membuat elemen <form> secara manual tanpa menggunakan _generator_ seperti {{ form.as_table }}.
Karena pada umumnya form terdiri dari label dan input, kita bisa memanfaatkan tag yang sudah ada di HTML yaitu `<label>` dan `<input>`. 
```html
<form>
  <label for="name">Name: </label><br>
  <input type="text" id="name" name="name"><br>
  <label for="pw">Password: </label><br>
  <input type="text" id="pw" name="pw"><br>
</form>
```
Pada contoh di atas, tipe input yang digunakan adalah _text area_. Selain _text area_, kita juga bisa menggunakan tipe lain seperti _checkbox_, _radio button_, dan lain sebagainya.
  
### Proses Alur data
1. User memasukkan data ke _input field_ pada HTML form lalu klik tombol untuk _submit_
2. Data dikirim ke _server_
3. Data diproses oleh fungsi-fungsi pada `views.py`
4. Objek model dibuat menggunakan `Model.objects.create()` untuk disimpan di _database_
5. Data yang telah disimpan bisa diakses `views.py` sesuai user yang telah diautentikasi
6. Data di-_render_ pada _template_ HTML yang telah "dipilih" 
7. Data dapat dilihat pada halaman web yang ditampilkan hasil _render_ HTML
  
## Implementasi
 1. Membuat aplikasi `todolist` dengan `python manage.oy startapp todolist`, lalu tambahkan `todolist` ke `INSTALLED_APPS`
  di `/project_django/settings.py`
 2. Membuat fungsi `show_todolist` di `/todolist/views.py` untuk menampilkan halaman utama `todolist`,
 menambahkan `path('', show_todolist, name='show_todolist')`, pada `/todolist/urls.py`, dan menambahkan `path('todolist/', include('todolist.urls'))` di `/project_django/urls.py`
 3. Buat model `Task` dengan atribut user, date, title, dan description, makemigrations, lalu migrate ke database
 ```python
 from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
 ```
 4. Buat fungsi pada `/todolist/views.py` seperti pada tutorial 4 untuk meng-_handle_ registrasi akun, _login_, dan _logout_. 
 Tambahkan `@login_required(login_url='/todolist/login/')` di atas fungsi `show_todolist` sehingga halaman utama `todolist` hanya bisa diakses setelah login
 5. Di folder `templates`, buat `login.html`, `register.html` serta `todolist.html` untuk tampilannya
 6. Membuat fungsi baru di `views.py` untuk meng-_handle_ _task creation_, tambahkan `@login_required(login_url='/todolist/login/')`
 agar hanya bisa diakses akun yang sudah diautentikasi. Buat juga _template_ `create_task.html` untuk _task creation_ pada `/todolist/templates`
 7. Tambahkan _routing_ untuk fungsi pembuatan _task_, registrasi, login, dan logout
 8. Add, commit, dan push ke github dan deployment akan berjalan secara otomatis
 9. Registrasi pada halaman web yang telah dideploy dan buat _dummy data_
 ```
JinggaDjango
mentari123

VladiDjango
casajasmine17
 ```

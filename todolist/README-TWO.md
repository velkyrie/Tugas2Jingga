# Tugas 5 - Vladi Jingga Mentari (2106635631)

https://tugas2jingga.herokuapp.com/todolist

## _Asynchronous Programming_ vs _Synchronous Programming_
**_Synchronous Programming_**

_Tasks_ akan dijalankan satu-satu dan hanya akan dijalankan setelah _task_ sebelumnya selesai.
Ketika terjadi sebuah _event_, user harus menunggu hingga halaman memberikan _response_. 
Ketika kode berjalan, program akan mengikuti setiap langkah dari suatu algoritma. 
Program akan melakukannya secara berurutan dan akan menunggu operasi selesai sebelum melanjutkan ke operasi berikutnya.

**_Asynchronous Programming_**

_Tasks_ dapat dieksekusi secara bersamaan tanpa harus menunggu _task_ sebelumnya selesai.
Karena itu, user tetap bisa beraktivitas biasa walau terjadi sebuah _event_ tanpa harus menunggu halaman memberikan _response_. 
Response akan langsung ditampilkan ketika _task_ selesai diproses. 

## _Event-Driven Programming_

_Event-Driven Programming_ adalah suatu paradigma yang memungkinkan program berjalan karena sebuah _event_. _Event_
tersebut dapat di-_trigger_ _action_ dari user seperti mengeklik objek-objek _call-to-action_ seperti `button`, `a`, `checkbox`, dan lain sebagainya. 
Pada tugas kali ini, ada banyak contoh penerapan _event-driven programming_ seperti saat user mengeklik tombol `login`, `register`, `submit`, `add`, dan juga `logout`.

## _Asynchronous Programming_ pada AJAX

AJAX atau _Asynchronous JavaScript and XML_ memungkinkan web app untuk mengirim dan mengambil data dari server secara asinkronus tanpa
mengganggu tampilan dan _behavior_ page. AJAX melakukan _data decoupling_ (atau pertukaran data) _interchange layer_ dari _presentation layer_ sehingga halaman
dapat berganti konten secara dinamis tanpa harus me-_reload_ seluruh halaman. 

## Implementasi _Checklist_
 ### AJAX GET
- membuat `view` baru yang mengembalikan seluruh data task dalam bentuk JSON.
```python
@login_required(login_url='/todolist/login/')
def get_todo_json(request):
    todo = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", todo), content_type="application/json")
    
```
-  membuat path `/todolist/json` yang mengarah ke view yang baru dibuat pada `/todolist/urls.py`
``` python
    ...
    path('json/', get_todo_json, name='get_todo_json'),
    ...
```
- melakukan pengambilan task menggunakan AJAX GET.
```javascript
const getTodo = () => {
            $.get("{% url 'todolist:get_todo_json' %}", data => {
                $.each(data, (i, value) => {
                    $("#mainBody").append(card(value));
                });
            });
        };
```

### AJAX POST
- membuat sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.
```html
<div class="card-body p-2 text-center">
  <button class="card-todo sm-2 mb-3 text-white container-sm"><h1><a class="link-primary" data-toggle="modal" data-target="#myModal">+ add</a></h1></button>
</div>
```
-  membuat _view_ baru untuk menambahkan task baru ke dalam database.
```python
@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todo = Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            is_finished=False,
            date=datetime.datetime.today())
        return JsonResponse(
            {
                'pk': todo.id,
                'fields': {
                    'title': todo.title,
                    'description': todo.description,
                    'is_finished': todo.is_finished,
                    'date': todo.date,
                },
            },
            status=200,
        )
```
- membuat path `/todolist/add` yang mengarah ke view yang baru kamu buat.
```python
    ...
    path('create-task/', create_task, name='create_task'),
    ...
```
-  mengubungkan form yang telah dibuat di dalam modal ke path `/todolist/add`

```html
<!--- form dalam modal --->
<form method="POST" id="createForm">
                    {% csrf_token %}
                    <div class="mb-md-5">
                        <p class="text-white-50 mb-md-4">stay <u>organized</u>, add a new to-do. </p>

                        <div class="form mb-4">
                            <input type="text" name="title" id="title" placeholder="Task" class="form-control">
                        </div>

                        <div class="form mb-4">
                            <textarea type="text" name="description" id="description" placeholder="Description"
                                class="form-control"></textarea>
                        </div>
                    </div>

                    <button class="btn btn-outline-light btn-lg px-3" type="submit" name="submit" value="Create Task">+
                        Add</button>
                </form>
```

menghubungkan ke path, menutup modal setelah penambahan task selesai, dan melakukan _refresh_ pada halaman secara asinkronus untuk menampilkan _list_ terbaru tanpa _reload_
```javascript

        $("#createForm").submit(e => {

            const csrf_token = document.querySelector(
                "[name=csrfmiddlewaretoken]"
            ).value;
            
            let title = $("#title").val()
            let description = $("#description").val()

            if (title && description) {
                e.preventDefault();

                $.ajax({
                    type: "POST",
                    url: "{% url 'todolist:create_task' %}",
                    headers: { "X-CSRFToken": csrf_token }, 
                    mode: "same-origin",
                    async: true,
                    data: {
                        title: title,
                        description: description,
                    },
                    success: response => {
                        $("#createForm").trigger("reset"); //me-refresh secara asinkronus
                        $("#mainBody").append(card(response)); //append task baru ke card
                        closeModal(); #menutup modal
                    },
                });
            } else {
                alert("Fields cannot be empty!");
            }

        });
```
menutup modal dengan fungsi `closeModal()`
```javascript
const closeModal = e => {
            $('.modal').removeClass('in');
            $('.modal').attr("aria-hidden", "true");
            $('.modal').css("display", "none");
            $('.modal-backdrop').remove();
            $('body').removeClass('modal-open');
        };
```

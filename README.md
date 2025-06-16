# 🐍 Django Challenge – Junior Fullstack Interview (20 min)

Bienvenido/a. Este es el primer reto técnico para el puesto de Fullstack Developer. Aquí trabajaremos con código de Django para evaluar tu razonamiento, conocimiento del framework y manejo de Python.

> ⚠️ No es necesario que este proyecto pueda ejecutarse. Tu código será evaluado **solo leyendo lo que escribas**. Concéntrate en la estructura, claridad y lógica del código.

---

## 📁 Estructura del reto

Este mini módulo llamado `users` ya incluye algunos archivos:

- `models.py`: contiene el modelo `User`.
- `serializers.py`: contiene el serializer para `User`.
- `views.py`: contiene una vista base para listar usuarios.
- `urls.py`: incluye la ruta `/api/users/`.

---

## 🧪 Tu reto

Queremos filtrar los usuarios por edad mínima y mejorar el output de la API.

### ✅ Tareas:

1. **Agrega un parámetro de consulta** `min_age` a la vista en `views.py`:
   - Si el parámetro está presente, filtra los usuarios cuya edad sea **mayor o igual** a `min_age`.
   - Si no está presente, retorna todos los usuarios.

2. **Ordena los resultados por fecha de creación** (`date_joined`), de más reciente a más antiguo.

3. **Agrega un campo adicional** en el serializer llamado `full_name`, que concatene el `first_name` y `last_name`.

---

## 💡 Notas:

- Puedes asumir que los modelos, imports y configuraciones necesarias están disponibles.
- Usa Django REST Framework (`serializers.Serializer`, `APIView`, etc.).
- En caso de duda, escribe tu razonamiento como comentario.

---

## 🕒 Tiempo estimado: 20 minutos

Cuando termines, realiza un commit con tus cambios. Si te queda tiempo, puedes dejar comentarios explicando tu razonamiento.

¡Éxito!

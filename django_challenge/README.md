# 🐍 Django Challenge – Junior Fullstack Interview (25 min)

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

1. **Filtrado por edad mínima**:
   - Agrega un parámetro de consulta `min_age` a la vista `UserListAPIView`.
   - Si el parámetro está presente, filtra los usuarios cuya edad sea **mayor o igual** a `min_age`.
   - Si no está presente, retorna todos los usuarios.

2. **Ordenamiento**:
   - Ordena los usuarios por el más reciente al más antiguo.

3. **Campo `full_name` en el serializer**:
   - Agrega un campo que concatene `first_name` y `last_name`.

4. **Campo adicional `is_adult`**:
   - Agrega un campo booleano al serializer que devuelva `True` si el usuario tiene 18 años o más, y `False` en caso contrario.

---

## 💡 Notas:

- Puedes asumir que los modelos, imports y configuraciones necesarias están disponibles.
- Usa Django REST Framework (`serializers.Serializer`, `APIView`, etc.).

---

## 🕒 Tiempo estimado: 25 minutos

---------------------------------

## ⭐ Reto adicional (opcional si terminas antes)

Si terminas los pasos anteriores y aún tienes tiempo, intenta resolver el siguiente reto adicional:

### 🧩 Agrega una estadística al endpoint

Modifica la vista `UserListAPIView` para que, además de retornar la lista de usuarios, también devuelva un campo llamado `"average_age"` que indique el **promedio de edad** de los usuarios en el queryset final (ya filtrado, si aplica).

📌 La respuesta JSON debería tener esta estructura:

```json
{
  "average_age": 27.5,
  "users": [
    {
      "first_name": "Ana",
      "last_name": "García",
      "age": 22,
      "date_joined": "2023-11-10T12:00:00Z",
      "full_name": "Ana García",
      "is_adult": true
    },
    ...
  ]
}



Cuando termines, realiza un commit con tus cambios. Si te queda tiempo, puedes dejar comentarios explicando tu razonamiento, esto nos ayudara a entender mas tu manera de razonar y resolver problemas.

¡Éxito!

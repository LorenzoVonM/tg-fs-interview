# ⚛️ React Challenge – Junior Fullstack Interview (20–25 min)

Bienvenido/a. Este es el segundo reto técnico para el puesto de Fullstack Developer. Aquí trabajaremos con un componente de React para evaluar tu razonamiento, conocimiento del framework y manejo de componentes.

> ⚠️ No es necesario que este proyecto funcione al ejecutarse. Tu código será evaluado **únicamente por lo que escribas**. Concéntrate en la estructura, claridad y lógica.

---

## 📁 Estructura del reto

El archivo principal del reto es:

`src/components/UserList.jsx`

Este componente debe hacer una petición a un API y mostrar los usuarios en una lista.

---

## 🧪 Tu reto

Queremos consumir una API que retorna una lista de usuarios, y mostrarla al usuario.

### ✅ Tareas:

1. **Petición HTTP al backend**:
   - Usa `useEffect` para hacer un `fetch()` a la URL `/api/users/`.
   - Guarda la respuesta (un array de usuarios) en el estado.

2. **Renderizado**:
   - Muestra una lista de los usuarios en pantalla, incluyendo:
     - Nombre completo (`full_name`)
     - Edad
     - Si es mayor de edad (`is_adult`: muestra "✅" o "❌")

3. **Filtrado por edad**:
   - Agrega un input de texto arriba de la lista donde el usuario pueda escribir una edad mínima (`min_age`).
   - Al cambiar el valor, vuelve a hacer la petición con el parámetro `min_age` como query param (`/api/users/?min_age=21`).

---

## 💡 Notas:

- Puedes asumir que la API responde con un JSON como este:

```
[
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
```

- No es necesario que el código funcione al ejecutarse, lo importante es la lógica que plantees.


## ⭐ Reto adicional 

Si terminas todo y aún tienes tiempo, intenta lo siguiente:

### 🧩 Agrega manejo de carga y errores:

1. **Loading**
   - Mientras los datos están siendo cargados, muestra un mensaje `"Cargando usuarios..."`.

2. **Error**
   - Si ocurre un error al hacer `fetch()` (por ejemplo, si la API no responde), muestra un mensaje de error: `"No se pudo obtener la lista de usuarios."`

Puedes usar estados adicionales como `isLoading` y `hasError`, o cualquier estrategia con la que te sientas cómodo/a.

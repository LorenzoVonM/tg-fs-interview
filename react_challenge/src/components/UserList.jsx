import React, {useEffect, useState} from "react";

function UserList() {
  // Para guardar el resultado del fetch
  const [users, setUsers] = useState([]);
  //Se necesita una const para guardar el valor del input


  //Hay que modificarlo para incluir el campo minAga
  useEffect(() => {
    // De igual forma hay que agregarlo a la url 
    fetch("/api/users/")
    .then((Response) => Response.json())
    .then((date) => setUsers(data))
    .catch((error) =>
    console.error("Error al obtener los usuarios: ", error));

  }, [])

  return (
    <div>
      <input type="number" placeholder="Edad mínima" />
      <ul>
        {users.map(users, index) => (<li key = {index}>{users.full_name} - Edad: {users.age} - Es adulto: {users.is_adult ? "✅" : "❌"}</li>)}
      </ul>
    </div>
  );
}

export default UserList;
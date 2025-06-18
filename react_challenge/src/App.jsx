
import React, {useEffect, useState} from "react";
import UserList from "./components/UserList";


function App() {

    // States
    const [users, setUsers] = useState([])
    const [minAge, setMinAge] = useState(0)

    // Loading state
    const [loading, setLoading] = useState(false)

    // Funtion to get users from API
    const fetchUsers = async () => {
        setLoading(true)
        try {
            // fetch users with query param 'minAge'
            const response = await fetch('http:localhost:8000/api/users/?min_age=${minAge}')
            
            // get data in json format
            const data = await response.json()
            setUsers(data.users) // Supouse the API return { users []}
        } catch (error) {
            console.error('No se pudo obtener la lista de usuarios.')
        } finally {
            setLoading(false)
        }
    }

    useEffect(() => {
        fetchUsers()
    }, [])

  return (
    <div>
      <h1>Lista de usuarios</h1>
      <input
        type="number"
        value={minAge}
        onChange={(e) => setMinAge(e.target.value)}
        />

        <button onClick={fetchUsers}> Filtrar </button>

        {/* Chechking loading state */}
        {loading ? ( 
            <p>Cargando...</p>
        ) : 
        <ul>

            {users.map((user) => (
                <li key={user.full_name}>
                    {user.full_name} - {user.age} años - {user.is_Adult ? '✅' : '❌'} 

                </li>
            ))}
        </ul>
        
        }



      <UserList />
    </div>
  );
}

export default App;
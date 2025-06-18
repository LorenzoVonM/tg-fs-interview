import React from "react";
import {useEffect, useState} from 'react';


function UserList() {
  const [users, setUsers] = useState();

  fetch_users = () => {
    fetch('.../api/users/')
  }
  
  useEffect (() => {
    let returned_users = fetch_users()
    setUsers(returned_users);
  }

  )

  const listUsers = users.map(user =>
  <ul key={user.id}>
    {user.full_name}
    {}
  </ul>
);

  return (
    <div>
      <input type="number" placeholder="Edad mínima" />
      <ul>
        {u}
      </ul>
    </div>
  );
}

export default UserList;
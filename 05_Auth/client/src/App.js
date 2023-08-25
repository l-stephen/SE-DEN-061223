import {useEffect, useState} from "react";
import './App.css';

function App() {
    const [name, setName] = useState("")
    const [password, setPassword] = useState("")
    const [user, setUser] = useState(null)

    useEffect(() => {
        fetch("/check_session")
        .then(r => r.json())
        .then(user => setUser(user))
    })

    function handleSubmit(e){
        e.preventDefault()
        fetch("/signin", {
            method: "POST",
            headers:{
                "Content-Type": "application/json"
            },
            body: JSON.stringify({name: name, password: password})
        })
        .then(res => res.json())
        .then(data => setUser(data))
    }
    function handleUsername(e){
        setName(e.target.value)
      }
    
      function handlePassword(e){
        setPassword(e.target.value)
    }

    function handleLogout(e){
        e.preventDefault()
        fetch("/logout", {
            method: "DELETE",
            headers:{
                "Content-Type": "application/json",
            }
        })
        .then(setUser(null))
    }

    if(user){
        return (
            <>
            <h1>Welcome, {user.name}</h1>
            <form onSubmit={handleSubmit}>
                <button>Logout</button>
            </form>
            </>
        )
    }
    else{
        return (
            <form onSubmit={handleSubmit}>
                <h2>Username</h2>
                <input type="text" value={name} onChange={handleUsername}/>
                <h2>Password</h2>
                <input type="text" value = {password} onChange={handlePassword}/>
                <button type="submit">Login</button>
                <br></br>
                <button onClick = {handleLogout} type="submit">Logout</button>
            </form>
        )
    }

}

export default App;

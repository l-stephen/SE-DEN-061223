import {useEffect, useState} from "react";
import './App.css';

function App() {
    const [name, setName] = useState("")
    const [password, setPassword] = useState("")
    const [newName, setNewName] = useState("")
    const [newPassword, setNewPassword] = useState("")
    const [user, setUser] = useState(null)

    useEffect(() => {
        // auto-login
        fetch("/check_session").then((r) => {
          if (r.ok) {
            r.json().then((user) => setUser(user));
          }
        });
      }, []);

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
    function handleNewUsername(e){
        setNewName(e.target.value)
    }
    
      function handleNewPassword(e){
        setNewPassword(e.target.value)
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

    function handleSignup(e){
        e.preventDefault()
        fetch("/signup", {
            method: "POST",
            headers:{
                "Content-Type": "application/json"
            },
            body: JSON.stringify({name: newName, password: newPassword})
        })
        .then(res => res.json())
        .then(data => setUser(data))
    }

    if(user){
        return (
            <>
            <h1>Welcome, {user.name}</h1>
            <button onClick={handleLogout}>Logout</button>
            </>
        )
    }
    else{
        return (
            <>
            <form onSubmit={handleSubmit}>
                <h2>Username</h2>
                <input type="text" value={name} onChange={handleUsername}/>
                <h2>Password</h2>
                <input type="text" value = {password} onChange={handlePassword}/>
                <button type="submit">Login</button>
            </form>
            <br></br>
            <form onSubmit={handleSignup}>
                <h2>Username</h2>
                <input type="text" value={newName} onChange={handleNewUsername}/>
                <h2>Password</h2>
                <input type="text" value = {newPassword} onChange={handleNewPassword}/>
                <button type="submit">Sign Up</button>
            </form>
            </>
        )
    }

}

export default App;

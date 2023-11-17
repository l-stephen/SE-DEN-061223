
import {useEffect, useState} from 'react'
import EditProductionForm from "./components/EditProductionForm"
function App(){
  const [productions, setProductions] = useState([])
  const [title, setTitle] = useState("")
  const [genre, setGenre] = useState("")
  const [description, setDescription] = useState("")
  const [editProduction, setEditProduction] = useState(false);
  const [production_edit, setProductionEdit] = useState(false)

  function handleTitle(e){
    setTitle(e.target.value)
  }

  function handleGenre(e){
    setGenre(e.target.value)
  }

  function handleDescription(e){
    setDescription(e.target.value)
  }

  useEffect(()=> {
    fetch("/productions")
    .then(res => res.json())
    .then(setProductions)

  }, [])

  const handleSubmit = async (event) => {
    event.preventDefault();

    const newProduction = {
      title,
      genre,
      description,
    };

    // Send a POST request to create the new production
    try {
      const response = await fetch('/productions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newProduction),
      });

      const createdProduction = await response.json();
      await setProductions((prevState) => [...prevState, createdProduction]); // Update state after the request is complete

      // Clear the form fields after submitting
      setTitle('');
      setGenre("")
      setDescription('');
    } catch (error) {
      console.error('Error creating production:', error);
    }
  };
  
  const handleEdit = (production) => {
    setEditProduction(true)
    setProductionEdit(production)
  }

  const handleDelete = (id) => {
    fetch(`/productions/${id}`, {
      method: "DELETE"
    })
    .then((res) => {
      if (res.ok) {
        setProductions((prevState) => prevState.filter((prod) => prod.id !== id));
      } else {
        console.error('Failed to delete production. Status:', res.status);
      }
    })
    .catch((error) => {
      console.error('Error deleting production:', error);
    });
  }

  return (
    <div>
      {editProduction ? (
        <EditProductionForm production={production_edit} setEditProduction={setEditProduction} setProductions={setProductions} />
      ):(
      <form onSubmit={handleSubmit}>
        <label>Title:</label>
        <input type="text" name="title" value={title} onChange={handleTitle} />

        <label>Genre:</label>
        <input type="text" name="genre" value={genre} onChange={handleGenre} />

        <label>Description:</label>
        <textarea name="description" value={description} onChange={handleDescription} />

        <button type="submit">Create Production</button>
      </form>)
      }

      <hr />
      {productions.map((production) => (
        <div key={production.id}>
          <h2>{production.title}</h2>
          <p>{production.genre}</p>
          <p>{production.description}</p>
          <button onClick={() => handleEdit(production)}>Edit</button>
          <button onClick={() => handleDelete(production.id)}>Delete</button>
        </div>
      ))}
    </div>
  )
}


export default App



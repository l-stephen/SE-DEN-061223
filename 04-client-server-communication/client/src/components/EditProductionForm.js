import {useState} from "react"
function EditProductionForm({production, setEditProduction, setProductions}){

    const [title, setTitle] = useState(production.title);
    const [genre, setGenre] = useState(production.genre);
    const [description, setDescription] = useState(production.description);

    const handleTitleChange = (e) => {
        setTitle(e.target.value);
      };
    
      const handleGenreChange = (e) => {
        setGenre(e.target.value);
      };
    
      const handleDescriptionChange = (e) => {
        setDescription(e.target.value);
      };

      function handleSubmit(e){
        e.preventDefault()
        const updatedProduction = {
            title,
            genre,
            description,
          };

        fetch(`/productions/${production.id}`, {
            method: "PATCH",
            headers:{"Content-Type": "application/json"},
            body: JSON.stringify(updatedProduction)
        })
        .then(res=>res.json())
        .then((updatedData)=>{
            setProductions((prevProductions) =>
                prevProductions.map((prod) =>
                    prod.id === updatedData.id ? updatedData : prod
                )
        );
        setEditProduction(false);
        })
        .catch((error) => {
            console.error("Error updating production:", error);
          });
      }

      return (
        <form onSubmit={handleSubmit}>
          <label>Title:</label>
          <input type="text" name="title" value={title} onChange={handleTitleChange} />
    
          <label>Genre:</label>
          <input type="text" name="genre" value={genre} onChange={handleGenreChange} />
    
          <label>Description:</label>
          <textarea
            name="description"
            value={description}
            onChange={handleDescriptionChange}
          ></textarea>
    
          <button type="submit">Update Production</button>
        </form>
      );

}

export default EditProductionForm
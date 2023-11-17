import  {useParams, useNavigate } from 'react-router-dom'
import {useEffect, useState} from 'react'
import styled from 'styled-components'

function ProductionDetail({handleEdit, deleteProduction}) {
  const [production, setProduction] = useState({cast_members:[]})
  const [error, setError] = useState(null)
  const params = useParams()
  // const history = useNavigate()

  //6. Get One Production
  


  //7. Create a Delete Button and add a fetch request that will delete a production 

  
  const {id, title, genre, image,description, crew_members} = production 
  return (
      <CardDetail id={id}>
        <h1>{title}</h1>
          <div className='wrapper'>
            <div>
              <h3>Genre:</h3>
              <p>{genre}</p>
              <h3>Description:</h3>
              <p>{description}</p>
              <h2>Cast Members</h2>
              <ul>
              {/* {cast_members && cast_members.map(cast => (
                <li key={cast.id}>{`${cast.role} : ${cast.name}`}</li>
              ))} */}
              </ul>
            </div>
            <img alt = " " src={image}/>
          </div>
      {/* <button onClick={()=> handleEdit(production)} >Edit Production</button>
      <button onClick={()=> handleDelete(production)} >Delete Production</button> */}

      </CardDetail>
    )
  }
  
  export default ProductionDetail
  const CardDetail = styled.li`
    display:flex;
    flex-direction:column;
    justify-content:start;
    font-family:Arial, sans-serif;
    margin:5px;
    h1{
      font-size:60px;
      border-bottom:solid;
      border-color:#42ddf5;
    }
    .wrapper{
      display:flex;
      div{
        margin:10px;
      }
    }
    img{
      width: 300px;
    }
    button{
      background-color:#42ddf5;
      color: white;
      height:40px;
      font-family:Arial;
      font-size:30px;
      margin-top:10px;
    }
  `
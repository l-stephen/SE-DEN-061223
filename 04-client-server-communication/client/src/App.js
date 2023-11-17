// 📚 Review With Students:
    // Request response cycle
    //Note: This was build using v5 of react-router-dom
import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider, useNavigate } from 'react-router-dom'
import {createGlobalStyle} from 'styled-components'
import {useEffect, useState} from 'react'
import Home from './components/Home'
import ProductionForm from './components/ProductionForm'
import ProductionEdit from './components/ProductionEdit'
import Navigation from './components/Navigation'
import ProductionDetail from './components/ProductionDetail'
import NotFound from './components/NotFound'

function App(){
      //Note: This may be a good opportunity to refactor with context
  const [productions, setProductions] = useState([])
  const [production_edit, setProductionEdit] = useState(false)
  // const navigate = useNavigate()
  //4. GET Productions
  //navigate to client/src/components/ProductionForm.js


  const addProduction = (production) => setProductions(current => [...current,production])
  const updateProduction = (updated_production) => setProductions(productions => productions.map(production => production.id == updated_production.id? updated_production : production))
  const deleteProduction = (deleted_production) => setProductions(productions => productions.filter((production) => production.id !== deleted_production.id) )

  const handleEdit = (production) => {
    setProductionEdit(production)
    // navigate(`/productions/edit/${production.id}`)
  }

  const  router = createBrowserRouter(
    createRoutesFromElements(
      <Route path ="/" element={<Navigation />}>
        <Route index element={<Home productions={productions} />}/>
        <Route  path='/productions/new' element={<ProductionForm addProduction={addProduction}/>}/>
        <Route  path='/productions/edit/:id' elemebt={<ProductionEdit updateProduction={updateProduction} production_edit={production_edit}/>}/>
        <Route path='/productions/:id' element={<ProductionDetail handleEdit={handleEdit} deleteProduction={deleteProduction} />}/>
        <Route path="*" element={<NotFound />} />
      </Route>
    )
  )

  return (
    <div>
    <RouterProvider router ={router}/>
    </div>
  )
}


export default App

const GlobalStyle = createGlobalStyle`
  body{
    background-color: black; 
    color:white;
  }
  `


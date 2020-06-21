import React, { Component } from "react";
import NavMenu from './components/NavMenu';
import Footer from './components/footer';
import Cabecera from './components/cabecera';
import Visita from './components/visita';
import LinVisita from './components/LinVisita';

import axios from "axios";
import {
  BrowserRouter as Router,
  Route,  
  Switch
} from 'react-router-dom'
import './App.css';



class App extends Component {
    constructor(props) {
      super(props)
      this.state = {
        visitas: []
      }
    }

    componentWillMount() {
      this.refresh();
    }

    refresh = () => {
      axios
        .get("http://localhost:8000/api_visitas/visitas/")
        .then(res => this.setState({
          visitas: res.data
        }))
        .catch(err => console.log(err));
    };
    
  //-------------------------------------------------------------------------------
  render() { 
    let estiloCabecera = {
      width: '100%',
      color: '#fff',
      backgroundColor: '#52565e'
    },estiloSeccion={
        marginTop: '10px'
    },estirar100={
      width: '100%'
    };   
    if (this.state.visitas.length > 0) {   
      return (        
        <body className = "App-body" >
          <NavMenu />
          <Cabecera />          
          < div className = "App-Container container ">  

            <div class="row" style={estirar100}>    
              <div class="col-lg-3">
                  <div class="card mb-3" style={estiloCabecera}>
                      <div class="row ">
                          <div class="col-md-12">
                        <h4 style={estiloSeccion} align="center">Menú lateral</h4>
                          </div>
                      </div>
                  </div>
                  <div class="list-group">            
                  </div>
              </div>   

              <div class="col-lg-9">
                  <div class="row">
                    <div class="card mb-3" style={estiloCabecera}>
                      <div class="row ">
                        <div class="col-md-12">
                          <h4 style={estiloSeccion} align="center">Visitas Granada</h4>
                        </div>
                      </div>
                    </div>
                                        
                      <Router>
                        <Switch>
                          <Route path="/" exact>
                            {
                            this.state.visitas.map((visita) => {
                                return <LinVisita 
                                        key={visita.id}
                                        id={visita.id}
                                        nombre={visita.nombre}
                                        foto={visita.foto}
                                        likes={visita.likes}
                                        descripcion={visita.descripcion} />
                            })
                            }
                          </Route>
                          <Route path="/visita/:id" exact component={Visita} >
                          </Route>
                        </Switch>
                      </Router>                            
                    
                  </div> 
              </div>
            </div>
          </div> 

          <Footer />       
        </body>
      )    
    } else {
      return <p className="text-center">No hay visitas que mostrar</p>
    }
  }
}
export default App;
import React, { Component } from "react";
import './cabecera.css';
import ugr from './ugr.png';
import axios from "axios";

class Cabecera extends React.Component {   

    constructor(props) {
        super(props)
        this.state = {
            visitas: [],
            comentarios: []
        }
    }

    componentWillMount() {
        axios
            .get("http://localhost/api_visitas/visitas/")
            .then(res => this.setState({
                visitas: res.data
            }))
            .catch(err => console.log(err));
        axios
            .get("http://localhost/api_visitas/comentarios/")
            .then(res => this.setState({
                comentarios: res.data
            }))
            .catch(err => console.log(err));
    }  
    
    render() {                

        return (
            <div className="jumbotron jumbo_img">
                <div className="container">
                    <img src={ugr} width="150px" height="150px" alt="UGR"></img>
                    <div className="row">
                        <div className="col-lg-2 linDatos font-weight-bold">
                            <p>{this.state.visitas.length}</p>
                        </div>
                        <div className="col-lg-2 linDatos font-weight-bold">
                            <p>{this.state.comentarios.length}</p>
                        </div>
                    </div>
                    <div className="row">
                        <div className="col-lg-2 cabDatos">
                            <p>Visitas</p>
                        </div>
                        <div className="col-lg-2 cabDatos">
                            <p>Comentarios</p>
                        </div>
                    </div>                
                </div> 
            </div>    
        )
    }
}
export default Cabecera;
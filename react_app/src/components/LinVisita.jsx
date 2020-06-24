import React from 'react';
import { Router, Route, Link, BrowserRouter } from 'react-router-dom';
import Visita from './visita';
import axios from "axios";

class LinVisita extends React.Component {

    constructor(props) {
        super(props)        
    }    

    render() {
        let cardheight = {
            height: '130px'    
        },
        estiloEstirar = {
            width: '100%'
        },
        rojo = {
            color: 'red',
            marginRight:'5px'
        }, estiloSeccion = {
            marginTop: '10px',
            width: '100%'

        }

    return(
        <div id="visita_card" class="card mb-3" style={estiloSeccion}>
            <div class="row no-gutters" style={estiloEstirar}>
                <div class="col-md-5" >
                    <img src={this.props.foto} class="card-img" alt="" width="250px" height="180px">
                    </img>                    
                </div>
                <div class="col-md-7">
                    <div class="card-body" style={cardheight}>
                        <h4 class="card-title"><a href={"/visita/" + this.props.id + "/"}>{this.props.nombre}</a></h4>
                        <p class="card-text" align="justify">{this.props.descripcion}</p>
                    </div> 

                    <div class="card-footer" style={estiloEstirar}>
                        <small class="text-muted"><i class='fa fa-heart' style={rojo}></i>
                            <label id="num_likes">{this.props.likes}</label>
                        </small>
                        <a href={"/visita/" + this.props.id + "/"}>
                            <button type="button"
                                class="btn btn-primary btn-sm float-right"
                                data_but="btn-xs">
                                <i class='fa fa fa-search-plus'></i> Ver en Detalle</button></a>
                    </div>
                </div>
            </div>
        </div> 
    )
  }
}

export default LinVisita
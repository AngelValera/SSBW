import React, { Component } from "react";
import axios from "axios";
import './visita.css';

class Visita extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            visita: [],
            likes: 0                                   
        }
    }

    componentWillMount() {
        this.refresh();
    }

    refresh = () => {        
        axios
            .get("http://localhost/api_visitas/visitas/" + this.props.match.params.id +"/")
            .then(res => this.setState({
                visita: res.data,
                likes: res.data.likes                
            }))
            .catch(err => console.log(err));
    };

    sumar_Like(){
        var ilikes = this.state.likes + 1;
        fetch('http://localhost/api_visitas/likes/' + this.state.visita.id + '/', {
            method: 'PUT',
            body: JSON.stringify({
                "id": this.state.visita.id,
                "likes": ilikes
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function (response) {
            console.log(response)
        });  
        this.setState({ likes: ilikes });
    }

    restar_Like(){
        var ilikes = this.state.likes - 1;
        fetch('http://localhost/api_visitas/likes/' + this.state.visita.id + '/', {
            method: 'PUT',
            body: JSON.stringify({
                "id": this.state.visita.id,
                "likes": ilikes
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function (response) {
            console.log(response)            
        });
        this.setState({ likes: ilikes });       
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
            marginRight: '5px'
        }, estiloSeccion = {
            marginTop: '10px',
            width: '100%'

        },separarBotones ={
            marginRight: '5px'
        }

    
        return (  
            <div id="visita_card" class="card mb-3" style={estiloSeccion}>
                <div class="row no-gutters" style={estiloEstirar}>
                    <div class="col-md-5" >
                        <img src={this.state.visita.foto} class="card-img" alt="" width="250px" height="180px">
                        </img>
                    </div>
                    <div class="col-md-7">
                        <div class="card-body" style={cardheight}>
                            <h4 class="card-title"><a href={"/visita/" + this.state.visita.id + "/"}>{this.props.nombre}</a></h4>
                            <p class="card-text" align="justify">{this.state.visita.descripcion}</p>
                        </div>

                        <div class="card-footer" style={estiloEstirar}>
                            <small class="text-muted"><i class='fa fa-heart' style={rojo}></i>
                                <label id="num_likes">{this.state.likes}</label>
                            </small>
                            
                            <button id="btn_Dislike" type="button" class="btn btn-secondary btn-sm float-right"
                                data_but="btn-xs" onClick={this.restar_Like.bind(this)}>
                                <i class='fa fa-thumbs-o-down'></i> No me gusta</button>
                            
                            <button id="btn_Like" type="button" class="btn btn-secondary btn-sm float-right"
                                data_but="btn-xs" style={separarBotones} 
                                onClick={this.sumar_Like.bind(this)}>
                                <i class='fa fa-thumbs-o-up'></i> Me gusta</button>
                        </div>
                    </div>
                </div>
            </div>
        )      
    }
}
export default Visita;
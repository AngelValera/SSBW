import React, {Component} from 'react';

class NavMenu extends React.Component {

    render() {

        return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
            <div className="container">
                <a className="navbar-brand" href="/">Visitas Granada</a>            
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive"
                    aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarResponsive">
                    <ul className="navbar-nav ml-auto">
                        <li className="nav-item active">
                        <a className="nav-link" href="/">Inicio
                            <span className="sr-only">(current)</span></a>
                        </li>                        
                    </ul>
                </div>
            </div>
        </nav> 
        )
    }
}
export default NavMenu;
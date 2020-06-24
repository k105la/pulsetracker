import React, { Component } from 'react';
import firebase from "firebase";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { AuthProvider } from "./components/Auth/Auth";
import Login from "./components/Login/Login";
import Home from "./components/Home/Home";
import PrivateRoute from "./components/PrivateRoute";
import './App.css';


class App extends Component {
  constructor (props){
    super(props);
    this.state = {
      user: {}
    }
  }
  componentDidMount() { 
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        this.setState({user: user});
        document.body.style.background = "white"; 

       } else {
         this.setState({user: null})
         document.body.style.background = "#FF75B5"; 
       }
    })
 }

  render () {
  return (
    <AuthProvider>
      <Router>
        <div>
          <PrivateRoute exact path="/" component={Home} />
          <Route exact path="/login" component={Login} />
        </div>
      </Router>
    </AuthProvider>
    );
  } 
}

export default App;
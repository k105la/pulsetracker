import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {app} from "./config/fire";
import firebase from "firebase";
import axios from "axios";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { AuthProvider } from "./Auth";
import Login from "./Login";
import Home from "./Home";
import PrivateRoute from "./PrivateRoute";

const auth = app.auth();
let provider = new firebase.auth.GoogleAuthProvider();

const signInWithGoogle = () => {
  auth.signInWithPopup(provider).then(function(res) {

    let user = res.user;
    console.log(user);
    console.log(user.uid);
  })
};

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
        axios.get(`http://127.0.0.1:5000/${user.uid}`)
        .then(res => {
          const heartrate = res.data;
                console.log(heartrate)
         })
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
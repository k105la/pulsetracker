import React, { Component } from 'react';
import './App.css';
import firebase from "firebase";
import axios from "axios";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { AuthProvider } from "./components/Auth/Auth";
import Login from "./components/Login/Login";
import Home from "./components/Home/Home";
import PrivateRoute from "./components/PrivateRoute";


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
       } else {
         this.setState({user: null})
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
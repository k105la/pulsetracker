import React, { Component } from "react";
import {app} from "../Auth/config/fire";
import firebase from "firebase";
import axios from "axios";
import Button from 'react-bootstrap/Button'
import Navbar from 'react-bootstrap/Navbar'
import logo from './logo/LOGO.png'

class Home extends Component {
  componentDidMount() { 
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        this.setState({user: user});
        axios.get(`http://127.0.0.1:5000/${user.uid}`)
        .then(res => {
          const heartrate = res.data;
          this.setState({hr: heartrate})
          console.log(heartrate)
         })
       } else {
         this.setState({user: null})
         this.setState({hr: 0})
       }
    })
 }
  constructor(props) {
  super(props);
  this.state = {
    user: {},
    hr: 0
    }
  }
  render() {
  return (
    <div>
 <Navbar bg="dark">
    <Navbar.Brand href="#">
      <img
        src={logo}
        width="175"
        height="30"
        className="d-inline-block align-top"
        alt="React Bootstrap logo"
      />
    </Navbar.Brand>
  </Navbar>
      <h1>Home</h1>
  <h3> {this.state.user.displayName} <br/>heart rate: {this.state.hr} </h3>
  <input
              type="file"
         
              name="file"
              accept="video/*"
              capture="environment"
              id="upload"
            />
      <Button variant="outline-dark" onClick={() => app.auth().signOut()}>Sign out</Button>
    </div>
  );
  }
};

export default Home;
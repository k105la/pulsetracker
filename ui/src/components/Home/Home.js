import React, { Component } from "react";
import {app} from "../Auth/config/fire";
import firebase from "firebase";
import axios from "axios";
import Button from '@material-ui/core/Button';
import logo from './images/LOGO.png'
import IconButton from '@material-ui/core/IconButton';
import PhotoCamera from '@material-ui/icons/PhotoCamera';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';

import "./Home.css"

class Home extends Component {
  componentDidMount() { 
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        this.setState({user: user});
       } else {
         this.setState({user: null})
       }
    })
 }

 uploadToFirebase() {
   
  firebase.auth().onAuthStateChanged((user) => {
    if (user) {
      axios.get(`http://127.0.0.1:5000/${user.uid}`)
      .then(res => {
        const heartrate = res.data;
        this.setState({hr: heartrate})
        console.log(heartrate);
       })
     } else {
       this.setState({hr: 0});
     }
  })
 }
  constructor(props) {
  super(props);
  this.state = {
    user: {},
    hr: 0
    }
    this.uploadToFirebase = this.uploadToFirebase.bind(this);
  }
  render() {
  return (


  <div className="container">
  <img
        src={logo}
        width="100%"
        height="50%"
        className="pulse d-inline-block align-top"
        alt="React Bootstrap logo"
      />
       <h2> Welcome, {this.state.user.displayName} </h2>

      <p className="top-text">Let's check your pulse! </p>
      <p>Place your finger over your camera <br/> for 15-30 seconds</p>

  <h1 className="heartrateData"> {this.state.hr}</h1>
  <p> <b> Heart Beats per Minute </b><br/> were logged by the algorithm</p>
  <input accept="image/*" className="upload-input" id="icon-button-file" type="file" />
      <label htmlFor="icon-button-file" className="camara-button">
        <IconButton color="default" aria-label="upload picture" component="span">
          <PhotoCamera />
        </IconButton>
      </label>
<br/>
      <Button
        className="upload-button"
        variant="contained"
        color="default"
        onClick={this.uploadToFirebase}
        startIcon={<CloudUploadIcon />}
      >
        Upload
      </Button>
      
      <Button id="sign-out-button" onClick={() => app.auth().signOut()}>Sign out</Button>


    </div>
  );
  }
};

export default Home;
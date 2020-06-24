import React, { Component } from "react";
import {app} from "../Auth/config/fire";
import firebase from "firebase";
import axios from "axios";
import Button from '@material-ui/core/Button';
import logo from './images/LOGO.png'
import IconButton from '@material-ui/core/IconButton';
import PhotoCamera from '@material-ui/icons/PhotoCamera';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import CircularProgress from '@material-ui/core/CircularProgress';
import "./Home.css"

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      user: {},
      hr: 0,
      prog: 0
    }
      this.retrievePulse = this.retrievePulse.bind(this);
      this.uploadVideoToFirebase = this.uploadVideoToFirebase.bind(this);
  }
  
 componentDidMount() { 
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        document.getElementById("user-uid").textContent = user.uid;
        this.setState({user: user});
       } else {
         this.setState({user: null})
       }
    })
 }

 uploadVideoToFirebase(event) {
  const storage = firebase.storage().ref();
  let file = event.target.files[0];
  let blob = file.slice(0, file.size, "video/quicktime");
  let newFile = new File([blob], "hr_test.MOV", { type: "video/quicktime" });

  console.log(newFile);
  firebase.auth().onAuthStateChanged((user) => {
    if(user) {
      let pulseBoxStorage = storage.child("data/" + user.uid);
      pulseBoxStorage.listAll().then((res) => {
          res.prefixes.forEach((folderRef) => {
            // console.log(folderRef);
          }) 
        
          res.items.forEach((itemRef) => {
            let pulseBoxCurrentStorage = storage.child(itemRef.location.path_);
            pulseBoxCurrentStorage.delete().then(() => {
              console.log("Cleaning " + user.uid + " storage box.")
            });
          });

      });

      let pulseBoxData = storage.child("data/" + user.uid + "/" + newFile.name);
      pulseBoxData.put(newFile).on("state_changed", (snapshot) => {
        let progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
        this.setState({prog: progress})
        if (progress === 100) {
          this.setState({prog: 0})
        }
        console.log(this.state.prog)
      })



    }


  })
 }

 retrievePulse() {
  firebase.auth().onAuthStateChanged((user) => {
    this.setState({loading: true}, () => {
      if (user) {
        axios.get(`http://127.0.0.1:5000/${user.uid}`)
        .then(res => {
          const heartrate = res.data;
          this.setState({hr: heartrate})
          this.setState({loading: false})
          console.log(heartrate);
         })
       } else {
         this.setState({hr: 0});
       }
    })
  })
 }

  render() {
    const loading = this.state.loading;
    const progessValue = this.state.prog;
  return (
  <div className="container">
      <img
        src={logo}
        width="100%"
        height="50%"
        className="pulse d-inline-block align-top"
        alt="PulseTracker logo"
      />
    { progessValue 
    ? <div className="progress-circle"> <CircularProgress variant="static" value={this.state.prog} /> </div>
    : <div>

       <h2 className="welcome-text"> Welcome, {this.state.user.displayName} </h2>

       <div className="uid hidden" id="uid-badge">
        <span className="uid-tag badge badge-pill badge-dark">UID</span>
        <span id="user-uid"></span>
        <br/>
        <button className="btn btn-outline-dark btn-sm" id="copy-button">
          Copy UID
        </button>
      </div>

      <p className="top-text">Let's check your pulse! </p>
      <p>Place your finger over your camera <br/> for 15-30 seconds</p>
 <div className="pulse-view">
  {loading ? <CircularProgress /> : <h1 className="heartrateData"> {this.state.hr}</h1>}
  <p> <b> Heart Beats per Minute </b><br/> were logged by the algorithm</p>
  </div>
  <input accept="video/*" onChange={this.uploadVideoToFirebase} className="upload-input" id="icon-button-file" type="file" ref={(ref) => this.fileUpload = ref}/>
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
        onClick={this.retrievePulse}
        startIcon={<CloudUploadIcon />}
      >
        Upload
      </Button>
      
      <Button id="sign-out-button" onClick={() => app.auth().signOut()}>Sign out</Button>
  </div>
  }
    </div>
    );
  }  
};

export default Home;
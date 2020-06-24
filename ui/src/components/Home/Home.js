import React, { Component } from "react";
import {app} from "../Auth/config/fire";
import firebase from "firebase";
import axios from "axios";
import logo from './images/LOGO.png'
import IconButton from '@material-ui/core/IconButton';
import PhotoCamera from '@material-ui/icons/PhotoCamera';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import CircularProgress from '@material-ui/core/CircularProgress';
import FileCopyIcon from '@material-ui/icons/FileCopy';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import BottomNavigation from '@material-ui/core/BottomNavigation';
import BottomNavigationAction from '@material-ui/core/BottomNavigationAction';
import "./Home.css";

const styles = {
  largeIcon: {
    width: 50,
    height: 50,
  },
};


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
      </div>

      <p className="top-text">Let's check your pulse! </p>
      <p>Place your finger over your camera <br/> for 15-30 seconds</p>
 <div className="pulse-view">
  {loading ? <div className="pulse-data-spinner"><CircularProgress /> </div>: <h1 className="pulse-data"> {this.state.hr}</h1>}
  <p> <b> Heart Beats per Minute </b><br/> were logged by the algorithm</p>
  </div>
  <input accept="video/*" onChange={this.uploadVideoToFirebase} className="upload-input" id="icon-button-file" type="file" ref={(ref) => this.fileUpload = ref}/>
      <label htmlFor="icon-button-file" className="camara-button">
        <IconButton color="default" aria-label="upload picture" component="span" >
          <PhotoCamera style={styles.largeIcon}/>
        </IconButton>
      </label>
<br/>


  </div>
  }
     <BottomNavigation className="stick-to-bottom" showLabels>
      <BottomNavigationAction label="Copy UID" icon={<FileCopyIcon />} />
      <BottomNavigationAction label="Upload" onClick={this.retrievePulse} icon={<CloudUploadIcon />} />    
      <BottomNavigationAction label="Sign out" onClick={() => app.auth().signOut()} icon={<ExitToAppIcon />} />
    </BottomNavigation>
    </div>
    );
  }  
};

export default Home;
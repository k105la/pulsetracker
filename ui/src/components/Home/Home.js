import React, { Component } from "react";
import {app} from "../Auth/config/fire";
import firebase from "firebase";

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
  constructor(props) {
  super(props);
  this.state = {
    user: {}
    }
  }
  render() {
  return (
    <div>
      <h1>Home</h1>
      <button onClick={() => app.auth().signOut()}>Sign out</button>
    </div>
  );
  }
};

export default Home;
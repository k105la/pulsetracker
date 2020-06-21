import React, { useCallback, useContext } from "react";
import { withRouter, Redirect } from "react-router";
import {app} from "./config/fire";
import { AuthContext } from "./Auth.js";

import firebase from "firebase"
  const auth = app.auth();
  let provider = new firebase.auth.GoogleAuthProvider();

  const Login = ({ history }) => {
    const handleLogin = useCallback(
      async event => {
        event.preventDefault();
    
        try {
          await auth.signInWithPopup(provider)
          history.push("/");
        } catch (error) {
          alert(error);
        }
      },
      [history]
    );
  
    const { currentUser } = useContext(AuthContext);
  
    if (currentUser) {
      return <Redirect to="/" />;
    }

    return (
        <div>
          <h1>Log in</h1>
            <button onClick={handleLogin}>Log in</button>
        </div>
      );
    };
    
    export default withRouter(Login);
  
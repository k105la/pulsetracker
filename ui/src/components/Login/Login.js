import React, { useCallback, useContext } from 'react';
import { withRouter, Redirect } from 'react-router';
import { app } from '../Auth/config/fire';
import { AuthContext } from '../Auth/Auth.js';
import firebase from 'firebase';
import Button from '@material-ui/core/Button';
import image from './logo/LOGO.png';
import './Login.css';

const auth = app.auth();
let provider = new firebase.auth.GoogleAuthProvider();

const Login = ({ history }) => {
  const handleLogin = useCallback(
    async (event) => {
      event.preventDefault();

      try {
        await auth.signInWithPopup(provider);
        history.push('/');
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
    <div className="container">
      <img className="pulse-logo" src={image} width="100%" alt="pulsetracker" />
      <h6 className="pulse-intro-text">
        An open source tool built for monitoring heart rate.
      </h6>
      <br />
      <Button
        className="sign-in-button"
        variant="outlined"
        onClick={handleLogin}
        size="large"
      >
        Continue with Google
      </Button>
    </div>
  );
};

export default withRouter(Login);

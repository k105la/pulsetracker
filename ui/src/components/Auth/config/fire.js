//import firebase from "firebase";
import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/storage';

export const app = firebase.initializeApp({
  apiKey: 'AIzaSyBoCLNFNU2-_J6NQtbLD7GGy30zRvkzBmk',
  authDomain: 'pulse-box.firebaseapp.com',
  databaseURL: 'https://pulse-box.firebaseio.com',
  projectId: 'pulse-box',
  storageBucket: 'pulse-box.appspot.com',
  messagingSenderId: '118237267477',
  appId: '1:118237267477:web:ccee5e3ab7928a8ce4301c',
  measurementId: 'G-0Q1RSLYZVN',
});

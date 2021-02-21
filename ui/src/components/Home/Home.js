import React, { Component } from 'react';
import { app } from '../Auth/config/fire';
import firebase from 'firebase';
import IconButton from '@material-ui/core/IconButton';
import PhotoCamera from '@material-ui/icons/PhotoCamera';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import CircularProgress from '@material-ui/core/CircularProgress';
import FileCopyIcon from '@material-ui/icons/FileCopy';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import BottomNavigation from '@material-ui/core/BottomNavigation';
import BottomNavigationAction from '@material-ui/core/BottomNavigationAction';
// Addded chart for displaying data
import Plot from 'react-plotly.js';
import { Logo } from '../../utils/imgUrl';
import AlertButton from '../AlertButton/AlertButton.js';
import './Home.css';

let hr_arr = [];
let count_arr = [];

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
      prog: 0,
      count: 0
    };
    this.retrievePulse = this.retrievePulse.bind(this);
    this.uploadVideoToFirebase = this.uploadVideoToFirebase.bind(this);
  }

  componentDidMount() {
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        document.getElementById('user-uid').textContent = user.uid;
        this.setState({ user: user });
      } else {
        this.setState({ user: null });
      }
    });
  }

  uploadVideoToFirebase(event) {
    const storage = firebase.storage().ref();
    let file = event.target.files[0];
    let blob = file.slice(0, file.size, 'video/quicktime');
    let newFile = new File([blob], 'hr_test.MOV', { type: 'video/quicktime' });

    console.log(newFile);
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        let pulseBoxStorage = storage.child('data/' + user.uid);
        pulseBoxStorage.listAll().then((res) => {
          res.prefixes.forEach((folderRef) => {});

          res.items.forEach((itemRef) => {
            let pulseBoxCurrentStorage = storage.child(itemRef.location.path_);
            pulseBoxCurrentStorage.delete().then(() => {
              console.log('Cleaning ' + user.uid + ' storage box.');
            });
          });
        });

        let pulseBoxData = storage.child(
          'data/' + user.uid + '/' + newFile.name
        );
        pulseBoxData.put(newFile).on('state_changed', (snapshot) => {
          let progress =
            (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
          this.setState({ prog: progress });
          if (progress === 100) {
            this.setState({ prog: 0 });
	  }
        });
      }
    });
  }

  retrievePulse() {
    firebase.auth().onAuthStateChanged((user) => {
      this.setState({ loading: true }, () => {
        if (user) {
          fetch(`https://pulsetracker-api.herokuapp.com/${user.uid}`)
            .then((res) => res.json())
            .then((result) => {
              
	      const heartrate = result.pulse;
              this.setState({ hr: heartrate });
              this.setState({ loading: false });
	      hr_arr.push(this.state.hr);
	      console.log(hr_arr);
               
	      this.setState({ count: this.state.count + 1})
	      count_arr.push(this.state.count);
	      console.log(count_arr);
	    });
        } else {
          this.setState({ hr: 0 });
        }
      });
    });
  }

  copyUID() {
    let copyText = document.getElementById('user-uid');
    let textArea = document.createElement('textarea');
    textArea.value = copyText.textContent;
    console.log(textArea.value);
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    textArea.remove();
  }

  render() {
    const loading = this.state.loading;
    const progessValue = this.state.prog;
    return (
      <div className="container">
        <img
          src={Logo}
          width="100%"
          height="50%"
          className="pulse d-inline-block align-top"
          alt="PulseTracker logo"
        />
        {progessValue ? (
          <div className="progress-circle">
            {' '}
            <CircularProgress variant="static" value={this.state.prog} />{' '}
          </div>
        ) : (
          <div>
            <h2 className="welcome-text">
              {' '}
              Welcome, {this.state.user.displayName}{' '}
            </h2>

            <div className="uid hidden" id="uid-badge">
              <span className="uid-tag badge badge-pill badge-dark">UID</span>
              <span id="user-uid"></span>
            </div>

            <AlertButton/>
            <div className="pulse-view">
              {loading ? (
                <div className="pulse-data-spinner">
                  <CircularProgress />{' '}
                </div>
              ) : (
	<Plot data={[
              {
                x: count_arr,
                y: hr_arr,
                type: 'scatter',
                mode: 'lines+markers',
                marker: { color: 'blue' },
              },
            ]}
            layout={{
              width: 400,
              height: 280,
              title: '',
              yaxis: {
                title: {
                  text: 'heartrate(bpm)',
                  font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f',
                  },
                },
              },
              xaxis: {
                title: {
                  text: 'timestep',
                  font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f',
                  },
                },
              },
            }}
          />
              
	      )}
       
            </div>
            <input
              accept="video/*"
              onChange={this.uploadVideoToFirebase}
              className="upload-input"
              id="icon-button-file"
              type="file"
              ref={(ref) => (this.fileUpload = ref)}
            />
            <label htmlFor="icon-button-file" className="camara-button">
              <IconButton
                data-testid="camera-button"
                color="default"
                aria-label="upload picture"
                component="span"
              >
                <PhotoCamera style={styles.largeIcon} />
              </IconButton>
            </label>
            <br />
          </div>
        )}
        <BottomNavigation className="stick-to-bottom" showLabels>
          <BottomNavigationAction
            data-testid="copy-button"
            label="Copy UID"
            onClick={this.copyUID}
            icon={<FileCopyIcon />}
          />
          <BottomNavigationAction
            data-testid="upload-button"
            label="Upload"
            onClick={this.retrievePulse}
            icon={<CloudUploadIcon />}
          />
          <BottomNavigationAction
            data-testid="sign-out-button"
            label="Sign out"
            onClick={() => app.auth().signOut()}
            icon={<ExitToAppIcon />}
          />
        </BottomNavigation>
      </div>
    );
  }
}

export default Home;

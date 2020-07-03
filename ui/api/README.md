![Imgur](https://i.imgur.com/E3s6RUi.png)
PulseTracker's API Service: https://pulsetracker-api.herokuapp.com/

### Deploying Service (must have admin privileges)
Inside this directory run:


```console
akilhylton:~$ heroku container:login
akilhylton:~$ heroku git:remote -a pulsetracker-api
akilhylton:~$ heroku container:push web -a pulsetracker-api
akilhylton:~$ heroku container:release web -a pulsetracker-api
```

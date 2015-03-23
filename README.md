# dockerized
a container for a utility letting you know who started at Docker recently and why, from the comfort of your terminal, without going to a browser. You could run it as a cron job as well, piping the output to an email notification.

## Usage
```docker run -ti chanezon/dockerized```
will list people who started recently, a link and title of their starting blog post

```docker run -ti chanezon/dockerized Willis -v```
will output the text of the complete blog post for a specific person.

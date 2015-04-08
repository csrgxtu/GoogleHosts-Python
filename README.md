GoogleHosts-Python
============
An project that finds out the usable Google IP address in your district. this project is implemented in Python 2.7.x.

### Usage
To start using **GoogleHosts-Python**, following the instructions:
```bash
cd GoogleHosts-Python/src
```
```bash
nohup python main.py &
```
or
```bash
./main.py
```
The result will be output to the console and in the same time will output to the *data/ipsok.txt*.

### Why
Cause I live in China, and the GFW -- Great Fire Wall blocked the services provided by Google, especially the search service. I am a developer, so I constantly need to find something using Google Search.

Through the struggle of accessing the Google Search service, comes to this project -- **GoogleHosts-Python**, now i am using this project find usable Google IP addresses and then using the Google Search Services.

### How
As we all know, Google's Search using HTTPS in port 443, so just start an socket try to connect to the 443 of an Google IP address, if connected, means it is available to you, otherwise no.

Roughly simple, but still a lot needs to be processed.

First, you need to find all available Google IP Address. check out [Google IP address ranges](https://support.google.com/a/answer/60764?hl=en).

Second, for each IP address you got, you need to start a socket to test the 443 port.

Third, Google have about 220000 IP address, so you need concurrent to make your program run faster. check out [An introduction to parallel programming](http://sebastianraschka.com/Articles/2014_multiprocessing_intro.html).

Fourth, even through you got some IP addresses with an open 443 port, still not enough, you need to check out if it is really a Google Search enabled IP address.

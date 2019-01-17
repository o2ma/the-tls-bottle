apt-get update
apt-get --assume-yes install python-pip
pip install bottle
pip install gevent
openssl req -new -x509 -days 1095 -nodes -newkey rsa:2048 -out server.crt -keyout server.key
firefox https://127.0.0.1:5000 &
python ./tls-server.py

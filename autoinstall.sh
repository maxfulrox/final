#!/bin/sh
apt update
apt install -y unzip xvfb libxi6 libgconf-2-4
apt install -y default-jdk 
apt install -y curl
apt install -y python
apt install -y python-pip
apt install -y python3-pip
pip install selenium
pip install subprocess.run
pip install mysql-connector-python

#install chrome
curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
apt -y update
apt -y install google-chrome-stable

#install ChromeDrive
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin/chromedriver
chown root:root /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver

#Download Required Jar Files
wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar
wget http://www.java2s.com/Code/JarDownload/testng/testng-6.8.7.jar.zip
unzip testng-6.8.7.jar.zip


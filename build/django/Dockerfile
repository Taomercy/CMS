FROM taomercy/ubuntu-python3.7.4-nginx-django3:latest
COPY ~/.ssh/id_rsa.pub ~/.ssh/id_rsa.pub
COPY . /home/CMS/
RUN pip3 install -r /home/CMS/requirements.txt && apt-get install uwsgi -y
EXPOSE 7000

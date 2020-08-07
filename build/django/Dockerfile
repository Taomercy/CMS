FROM taomercy/ubuntu-python3.7.4-nginx-django3:latest
COPY ./ssh/* /root/.ssh/
COPY . /home/CMS/
RUN pip3 install -r /home/CMS/requirements.txt && apt-get update && apt-get install git -y
COPY ./ssh/ssh_config /etc/ssh/ssh_config
EXPOSE 7000

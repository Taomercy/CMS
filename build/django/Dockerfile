FROM taomercy/ubuntu-python3.7.4-nginx-django3:latest
COPY ../CMS /home/CMS/
RUN pip3 install -r /home/CMS/requirements.txt && apt-get install uwsgi -y
EXPOSE 80 8000

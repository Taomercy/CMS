FROM nginx
EXPOSE 70 7000 7070 7001
RUN rm -rf /etc/nginx/conf.d/*.conf
ADD nginx.conf /etc/nginx/
RUN mkdir -p /etc/nginx/sites-available/
ADD default /etc/nginx/sites-available/

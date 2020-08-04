FROM nginx
EXPOSE 80 8000 8080
RUN rm -rf /etc/nginx/conf.d/*.conf
ADD nginx.conf /etc/nginx/
RUN mkdir -p /etc/nginx/sites-available/
ADD default /etc/nginx/sites-available/

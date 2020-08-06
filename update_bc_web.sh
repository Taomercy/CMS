#!/bin/bash
project_path=/home/ec2-user/CMS
port=1112
web_container_id=`docker ps -a | grep "cms_web" | awk '{print $1}'`
if [[ ! -n ${web_container_id} ]];then
    echo "no container"
    exit 1
fi

#docker stop ${web_container_id}

pushd ${project_path}
    git pull
    docker cp ${project_path} ${web_container_id}:/home/
popd

#docker run -itd -p ${port}:${port} --net=host pythonbc_web:latest /bin/bash

docker exec -d ${web_container_id} python3 /home/CMS/manage.py runserver 0.0.0.0:${port}

docker ps -a | grep ${web_container_id}



## Dockerfile for the `miracle` app

### Requirements

The Dockerfile assumes the following conditions (if you are not using `nginx`, see the end of the documentation):

* `nginx` is running as the `nginx` user (uid 1001)
    - Change line 9 in the Dockerfile if uid is different
* Unix socket for the `miracle` app is at `/home/miracle/socket/uwsgi.sock`, the `socket` folder is initially empty and owned by `ngnix`. Change `miracle.conf` if you want to use a different path.
* Database is provided by the `postgresql` container. Change `local.py` if your database host is different

### Usage

```bash
# Build image
git clone --depth 1 https://github.com/warmdev/miracle-docker.git
cd miracle-docker
sudo docker build -t miracle .
# Setup the database container first
sudo docker pull postgresql
sudo docker run --name miracle-db -e POSTGRES_USER=miracle -e POSTGRES_PASSWORD=CHANGEME -d postgres
# Take note of the container id
sudo docker exec -i -t container_id /bin/sh -c 'exec psql -U miracle -c "CREATE DATABASE miracle_metadata"'
sudo docker exec -i -t container_id /bin/sh -c 'exec psql -U miracle -c "CREATE DATABASE miracle_data"'
# Run the app and linking the db container
sudo docker run -v /home/miracle/socket:/opt/miracle/socket --link miracle-db:postgres -d miracle
# Copy `miracle.conf` to the nginx folder
sudo mv miracle.conf /etc/nginx/sites-enabled/
sudo service nginx restart
# Server will be live at port 9999
```

### If you are not using `nginx`

* Uncomment line 8 of `miracle.sh` and comment off line 9
* Uncomment line 28 of the Dockerfile
* Build the Docker image
* Run the docker containers using command below. Server will be live at `http://localhost:8888`

```
sudo docker run -p 8888:8888 --link miracle-db:postgres -d miracle
```


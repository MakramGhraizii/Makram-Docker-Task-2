# Makram-Docker-Task-2
For the Docker-compose file:
image: specifies the docker image to use for the service. minio/minio in this case. or '.' for local image
command: ovverides the def command and runs it from /data directory.
ports: maps ports
environment: sets env variables in both services
volumes: mounts volumes for data persistence
networks: connects both services to a specific network: bridge in this case.
healthcheck: monitors and checks the status of the containers: with intevals, timeouts, and retries.

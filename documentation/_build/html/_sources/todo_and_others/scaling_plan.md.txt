# CI/CD and Scaling

- **Development Docker:** [Done] set development Dockerfile, and run docker containers on docker compose with nginx in development.
- **Production Docker and Load Balancer:** [Planned] in the cloud will use docker prod file for services, use AWS ALB load balancer.
- **Testing:** [In progress] Unit test for all microservices, with a test when other microservices are called/events emitted.
- **Message Broker:** [Planned] Have Kafka added for event communication, with the message being stored, restored.
- **CI to Merge Code:** [Planned] there will be a master-dev branch, pushing code to the master-dev branch will do testing, and the ability to merge code. Could be done via Jenkins/Github Actions.
- **CD to Kubernetes:** [Planned] pushing code from master-dev to master will run the testing, in Jenkins/Github Actions. If the code is merged, then the docker container will be built, pushed to DockerHub, will deploy code to AWS EKS cluster. Will either use AWS CodePipeline or Jenkins to build the container and push to AWS EKS.
- **Service Mesh:** [Planned] Add Istio service Mesh.
- **Monitoring Service:** [Planned] Add Prometheus, Grafana.
- **Logging Stack:** [Planned] Add ELK stack for logging and monitoring.
- **Redis Cache:** [Planned] to add Redis. Add cache to load balancer, proxy, authentication and different levels.
- **Database Level:** [Planned] sharding, partitioning, lazy loading, indexing.

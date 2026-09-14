# Jenkins

Jenkins is an automation platform that allows us to build, test and deploy software using pipelines.

Note: It is not limited with pipeline of code it can be used to automate any task.

Jenkins provide web groovy where we can create and customize the functionalities.

## Jenkins Infrastructure

### Master Server
- Controls Pipelines
- Schedules Builds

### Agents/Minions
- Perform the Build

```bash
A develop commit code to repo 
-> Jenkins master gets aware and trigger pipeline -> Distribute the build to one of the agents to run (Which can be selected based on config labels)
-> Agent runs Build
```

### Agent Types:
- Pernament Agents (Dedicated Servers for running jobs)
- Cloud Agents (Ephemeral/Dynamic Agents Spin up on demand)

### Build Types
- Freestyle Build (Simplest method to create a build, 'Feels' like shell scripting)
- Pipelines (Use the Groovy Syntax, Use Stages to break down components of builds)

## Installation with Docker

### Build jenkins BlueOcean Docker image
```bash
docker build -t myjenkins-blueocean:2.332.3-1 .
```

### Create the network jenkins
```bash
docker network create jenkins
```

### To run the container
```bash
docker run --name jenkins-blueocean --restart=on-failure --detach `
--network jenkins --env DOCKER_HOST=tcp://docker:2376 `
--env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 `
--volume jenkins-data:/var/jenkins_home `
--volume jenkins-docker-certs:/certs/client:ro `
--publish 8080:8080 --publish 50000:50000 myjenkins-blueocean:2.332.3-1
```

### Unlock jenkins with Administrator Password
```bash
docker exec jenkins-blueocean cat /var/jenkins_home/secrets/initialAdminPassword
```
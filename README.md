# KafkaBasic

This project demonstrates a basic integration of Kafka with Django, where location updates are produced and consumed through Kafka using Docker.

## Table of Contents
- [KafkaBasic](#kafkabasic)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Getting Started](#getting-started)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Set Up Docker](#2-set-up-docker)
    - [3. Start Docker Containers](#3-start-docker-containers)
    - [4. Kafka Topics](#4-kafka-topics)
        - [Add your Google Map API](#add-your-google-map-api)
    - [Running the Producer and Consumer](#running-the-producer-and-consumer)
        - [Running the Producer](#running-the-producer)
        - [Running the Consumer](#running-the-consumer)
    - [Project Structure](#project-structure)


## Prerequisites
Before you get started, ensure you have the following installed on your system:
- Docker
- Docker Compose
- Python 3.x
- Django

## Getting Started

### 1. Clone the Repository

First, pull the repository from GitHub:

```bash
git clone git@github.com:dvsbharadva/Kafkabasic.git
cd Kafkabasic
```

### 2. Set Up Docker
Ensure that Docker and Docker Compose are installed on your machine. You can check if Docker is installed by running:

```bash
docker --version
docker-compose --version
```
If not installed, follow the official Docker installation guide: [Install Docker](https://docs.docker.com/get-docker/)

### 3. Start Docker Containers
You can start Kafka and Zookeeper using Docker Compose. In the root directory of the project, you will find a `docker-compose.yml` file. Run the following command to bring up Kafka and Zookeeper:

```bash
docker-compose up -d
```
This command will start Kafka and Zookeeper in detached mode.

Verify the services are running:

```bash
docker ps
```
### 4. Kafka Topics
To create Kafka topics such as location_update, you'll need to access the Kafka container and run the Kafka topic commands.

Create a topic:
```bash
docker exec -it <kafka-container-id> bash
kafka-topics.sh --create --topic location_update --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

To list topics:
```bash
kafka-topics.sh --list --bootstrap-server localhost:9092
```
##### Add your Google Map API
Copy your Google Map API to the `templates/index.html ` file and paste it here:
```bash
<script src="https://maps.googleapis.com/maps/api/js?key=<GOOGLE_MAP_API_KEY>" async></script>
```

### Running the Producer and Consumer
##### Running the Producer
The producer sends location updates to Kafka's `location_update` topic. To run the producer:

1. Activate your virtual environment and install the necessary Python packages.
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
2. Run the producer script:
```bash
python kafka_producer.py
```
This script will start sending simulated location updates to the `location_update` Kafka topic.

##### Running the Consumer
The consumer listens for location updates from the Kafka topic `location_update` and saves them to the database. Run the following command to start the consumer:

```bash
python3 manage.py kafka_consumer
```

The consumer will continuously poll Kafka for messages. Any valid location data will be saved to the Django model `LocationUpdate`.

### Project Structure
```
Kafkabasic/
├── home/
│   ├── migrations/
│   ├── models.py               # Django models including LocationUpdate
│   └── ...
├── kafkabasic/
│   ├── settings.py             # Django settings
│   └── ...
├── management/
│   ├── commands/
│   │   ├── kafka_consumer.py    # Kafka consumer script
│   └── ...
├── kafka_producer.py            # Kafka producer script
├── docker-compose.yml           # Docker configuration for Kafka and Zookeeper
├── requirements.txt             # Python dependencies
└── README.md
```
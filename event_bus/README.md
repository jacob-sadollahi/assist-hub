### README: Kafka & Kafka UI with Docker Compose (Updated for `confluent-kafka`)

This is provides a `docker-compose.yml` file for setting up Kafka and Kafka UI. The Kafka service uses the Bitnami Kafka image, and Kafka UI provides an easy-to-use web interface for managing Kafka clusters. This version includes instructions for using the `confluent-kafka` Python package to interact with Kafka.

---

## 🛠 Features

- **Kafka**: A lightweight setup with both controller and broker roles in one container.
- **Kafka UI**: A modern, browser-based interface to interact with Kafka.
- **Python Integration**: Instructions for using the `confluent-kafka` library for Kafka interaction.

---

## 📦 Services and Ports

| Service   | Description                 | Port  |
|-----------|-----------------------------|-------|
| Kafka     | Kafka broker and controller | 9092  |
| Kafka UI  | Web interface for Kafka     | 8080  |

---

## 🚀 Getting Started

Follow these steps to set up and run Kafka and Kafka UI on your machine.

### 1️⃣ Prerequisites

Ensure that the following are installed on your machine:
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Python**: Version 3.6 or later ([Install Python](https://www.python.org/downloads/))

---

### 2️⃣ Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>/event_bus
```

---

### 3️⃣ Start the Services

Run the following command to start the Kafka and Kafka UI services:

```bash
docker-compose up -d
```

---

### 4️⃣ Access the Services

1. **Kafka UI**:  
   Open your browser and navigate to [http://localhost:8080](http://localhost:8080).  
   You can view and manage Kafka clusters here.

2. **Kafka Broker**:  
   Kafka broker is running on port `9092`. Use it to produce or consume messages.


---

## 🔄 Stopping the Services

To stop the services, run:

```bash
docker-compose down
```

This will stop and remove the containers but keep the data in the volume.

---

## 📂 Data Persistence

Kafka data is stored in the Docker volume `kafka-data`. To remove the data completely, you can delete the volume:

```bash
docker-compose down -v
```

---

## 🐍 Using Kafka in Python with [`confluent-kafka`](https://github.com/confluentinc/confluent-kafka-python)

The `confluent-kafka` library is a performant Python client for Kafka, powered by `librdkafka`.

### Installation

Install the library:

```bash
pip install confluent-kafka
```

---

### Example Usage

#### Basic AdminClient Example
Create topics:

```python
from confluent_kafka.admin import AdminClient, NewTopic

a = AdminClient({'bootstrap.servers': 'kafka'})

new_topics = [NewTopic(topic, num_partitions=3, replication_factor=1) for topic in ["topic1", "topic2"]]
# Note: In a multi-cluster production scenario, it is more typical to use a replication_factor of 3 for durability.

# Call create_topics to asynchronously create topics. A dict
# of <topic,future> is returned.
fs = a.create_topics(new_topics)

# Wait for each operation to finish.
for topic, f in fs.items():
    try:
        f.result()  # The result itself is None
        print("Topic {} created".format(topic))
    except Exception as e:
        print("Failed to create topic {}: {}".format(topic, e))
```

---



## 🛠 Troubleshooting


- **edit file /etc/hosts**: Add the following line in /etc/hosts  
  127.0.0.1   kafka

- **Kafka UI not connecting to Kafka**: Ensure Kafka UI points to the correct `bootstrapServers`.  
  Update the `KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS` environment variable in `docker-compose.yml` if necessary.

- **Kafka port conflict**: If port `9092` is already in use, modify the `ports` section of the Kafka service in `docker-compose.yml`.

- **Python Errors with `confluent-kafka`**: Ensure `librdkafka` is installed correctly. For detailed installation instructions, refer to the [`confluent-kafka` documentation](https://github.com/confluentinc/confluent-kafka-python).

--- 

## 🌟 Feedback & Contributions

Feel free to submit issues or pull requests if you encounter any problems or have suggestions for improvements. Happy Kafka-ing! 🎉
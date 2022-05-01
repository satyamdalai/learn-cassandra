# Learning Cassandra

## Steps

1. Clone this repo.
2. Install the dependecies using `pip install -r requirements.txt`
3. Install Docker and run cassandra using `docker run --name learn-cassandra -p 9042:9042 cassandra -d`
4. Access the cassandra shell in a separate terminal by using the command `docker exec -ti learn-cassandra cqlsh`
5. Follow the **step 3** from this [link](https://cassandra.apache.org/_/quickstart.html)
6. Run the program using `python main.py`

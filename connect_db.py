import json

import psycopg2
import psycopg2.extras

json_graph = None
with open('./data.json') as f:
  json_graph = json.load(f)

def get_data_to_insert(json_graph):
    philos = set([el['philo'] for el in json_graph])
    for p in json_graph:
        for el in p['influenced'] + p['influences']:
            philos.add(el)
    philos = list(philos)

    name_to_id = {name:i+1 for i,name in enumerate(philos)}

    edges = set()
    for philo_entry in json_graph:
        name = philo_entry['philo']
        influences = philo_entry['influences']
        influenced = philo_entry['influenced']

        curr_philo_id = name_to_id[name]
        for influence in influences:
            edges.add((name_to_id[influence], curr_philo_id))
        for ph in influenced:
            edges.add((curr_philo_id, name_to_id[ph]))

    edges_list = list(edges)
    names = []
    for i,name in enumerate(philos):
        spl = name.split('/')
        last = spl[-1]
        first_last = last.split('_')
        if len(first_last) < 2:
            names.append((i+1, first_last))
        else:
            names.append((i+1, ' '.join(first_last),))

    print(len(edges_list))
    print(len(names))
    return {'edges': edges_list, 'names': names}

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "abc-123",
                                  host = "127.0.0.1",
                                  port = "6667",
                                  database = "philo-graph")

    cursor = connection.cursor()

    data_to_insert = get_data_to_insert(json_graph)
    edges = data_to_insert['edges']
    names = data_to_insert['names']

    cursor.execute('DELETE FROM philo_edges')
    cursor.execute('DELETE FROM philos')

    psycopg2.extras.execute_values(cursor, "INSERT INTO philos VALUES %s", names)

    cursor.execute("SELECT * FROM philos", )
    # records = cursor.fetchall()
    # print(records)

    psycopg2.extras.execute_values(cursor, "INSERT INTO philo_edges VALUES %s", edges)

    connection.commit()

    # record = cursor.fetchone()
    # print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
# finally:
#     if connection:
#         cursor.close()
    #closing database connection.
        # if(connection):
        #     cursor.close()
        #     connection.close()
        #     print("PostgreSQL connection is closed")

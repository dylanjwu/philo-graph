
CREATE TABLE philos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE philo_edges (
    influences_node_id INTEGER NOT NULL,
    influenced_node_id INTEGER NOT NULL,
    CONSTRAINT fk_influences FOREIGN KEY (influences_node_id) REFERENCES philos (id),
    CONSTRAINT fk_influenced FOREIGN KEY (influenced_node_id) REFERENCES philos (id),
    PRIMARY KEY(influences_node_id, influenced_node_id)
);


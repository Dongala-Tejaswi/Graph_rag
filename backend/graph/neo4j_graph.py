from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Neo4j Configuration
URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

# Create Neo4j Driver
driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

def create_graph():
    query = """
    MERGE (r:Technology {name:'Redis'})
    MERGE (f:Framework {name:'FastAPI'})
    MERGE (n:Database {name:'Neo4j'})
    MERGE (m:AI {name:'GraphRAG'})

    MERGE (r)-[:WORKS_WITH]->(f)
    MERGE (n)-[:USED_IN]->(r)
    MERGE (m)-[:USES]->(n)
    """

    with driver.session() as session:
        session.run(query)

    print("✅ Graph Created Successfully")


def get_graph_context(user_query):
    query = """
    MATCH (a)-[r]->(b)
    RETURN a.name AS source,
           type(r) AS relation,
           b.name AS target
    """

    results = []

    with driver.session() as session:
        data = session.run(query)

        for row in data:
            text = (
                f"{row['source']} "
                f"{row['relation']} "
                f"{row['target']}"
            )

            results.append(text)

    return results


def close_driver():
    driver.close()


if __name__ == "__main__":
    create_graph()

    print("\n📌 Graph Context:")
    context = get_graph_context("GraphRAG")

    for item in context:
        print(item)

    close_driver()
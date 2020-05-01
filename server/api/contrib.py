import os
from typing import Any
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import datetime

current_folder = os.path.dirname(__file__)
query_path = os.path.join(current_folder, "get_contribs.graphql")
with open(query_path, "r") as f:
    query = gql(f.read())


def send_query(username: str, from_str: str, to_str: str, token: str, cursor: str):
    params = {
        "username": username,
        # datetime.datetime.strptime(from_str, "%Y-%m-%dT%H:%M:%SZ"),
        "from": from_str,
        # datetime.datetime.strptime(to_str, "%Y-%m-%dT%H:%M:%SZ"),
        "to": to_str,
        "cursor": cursor,
    }

    _transport = RequestsHTTPTransport(
        url='https://api.github.com/graphql',
        use_json=True,
        headers={
            "Content-type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    )

    client = Client(
        transport=_transport,
        fetch_schema_from_transport=True,
    )
    result = client.execute(query, variable_values=params)
    return result


def post(body: Any):
    dates_projects: dict = {}
    hasNextPage = True
    while hasNextPage:
        result: Any = send_query(
            body["username"], body["from"], body["to"], body["token"], "")
        repositoryContributions: Any = result["user"]["contributionsCollection"]["repositoryContributions"]
        nodes: Any = repositoryContributions["nodes"]
        for node in nodes:
            current_date: str = str(node["occurredAt"])
            current_project: str = node["repository"]["name"]
            if current_date in dates_projects:
                dates_projects[current_date].append(current_project)
            else:
                dates_projects[current_date] = [current_project]
        hasNextPage = repositoryContributions["pageInfo"]["hasNextPage"]

    return dates_projects

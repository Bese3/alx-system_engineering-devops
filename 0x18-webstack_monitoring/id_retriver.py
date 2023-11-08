#!/usr/bin/python3
"""
Get all dashboards returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.list_dashboards(
        filter_shared=False,
    )
    response = response['dashboards'][0]['id']
    # print(response)
    with open('2-setup_datadog', mode='w', encoding='utf-8') as file:
        file.write(str(response) + "\n")

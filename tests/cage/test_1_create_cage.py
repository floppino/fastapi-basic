import yaml
from tests.test_init import client

"""
#########################################
#             Create a cage             #
#########################################
"""


# Create a cage with data from test_data.yaml
def test_create_cage(request):
    # Configure test info in the report
    request.node._method = "POST"
    request.node._route = "/cage"
    request.node._title = "Test create a cage"
    request.node._description = "Pass if the response is the cage data"

    # Request
    with open("tests/test_data.yaml", "r") as yaml_file:
        data = yaml.safe_load(yaml_file)
        cage_data = data["create_cage"][0]
        post_response = client.post("/cage", json=cage_data)

        # Save response
        request.node._effective_status_code = post_response.status_code

        # Verify the result
        request.node._expected_status_code = 201
        assert "cage_id" in post_response.json() and post_response.status_code == 201

        # Save the log
        request.node._full_response = post_response.json()

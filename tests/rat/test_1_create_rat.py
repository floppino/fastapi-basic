import yaml

from tests.test_init import client

"""
#########################################
#             Create a rat              #
#########################################
"""


# Create a rat with data from test_data.yaml
def test_create_rat(request):
    # Configure test info in the report
    request.node._method = "POST"
    request.node._route = "/rat"
    request.node._title = "Test create a rat"
    request.node._description = "Pass if the response is the rat data"

    # Request

    with open("tests/test_data.yaml", "r") as yaml_file:
        data = yaml.safe_load(yaml_file)
        rat_data = data["create_rat"][0]
        post_response = client.post("/rat", json=rat_data)

        # Save response
        request.node._effective_status_code = post_response.status_code

        # Verify the result
        request.node._expected_status_code = 201
        assert "rat_id" in post_response.json() and post_response.status_code == 201

        # Save the log
        request.node._full_response = post_response.json()

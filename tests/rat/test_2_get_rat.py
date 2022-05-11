import yaml
from tests.test_init import client

"""
#########################################
#           Get all rats                #
#########################################
"""


# Get all created test rats
def test_get_rats(request):
    # Configure test info in the report
    request.node._method = "GET"
    request.node._route = "/rat"
    request.node._title = "Test get all rats"
    request.node._description = "Pass if the status code is 200"

    #Request
    with open("tests/test_data.yaml", "r") as yaml_file:
        rat_data = yaml.safe_load(yaml_file)
        get_response = client.get("/rat", json=rat_data)

        # Save response
        request.node._effective_status_code = get_response.status_code

        #Verify the result
        request.node._expected_status_code = 200
        assert get_response.status_code == 200

        # Save the log
        request.node._full_response = get_response.status_code
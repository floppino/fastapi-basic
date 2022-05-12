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
    get_response = client.get("/rat")

    # Save response
    request.node._effective_status_code = get_response.status_code

    #Verify the result
    request.node._expected_status_code = 200
    assert get_response.status_code == 200

    # Save the log
    request.node._full_response = get_response.status_code



"""
#########################################
#           Get a rat                #
#########################################
"""


# Get a rat
def test_get_rat(request):
    # Configure test info in the report
    request.node._method = "GET"
    request.node._route = "/rat"
    request.node._title = "Test get a rat"
    request.node._description = "Pass if the status code is 200"

    #Request
    get_all = client.get("/rat")
    rat_id = get_all.json()[-1]["rat_id"]

    # Get a rat
    get_response = client.get(f"/rat/{rat_id}")

    # Save response
    request.node._effective_status_code = get_response.status_code

    #Verify the result
    request.node._expected_status_code = 200
    assert get_response.status_code == 200

    # Save the log
    request.node._full_response = get_response.status_code
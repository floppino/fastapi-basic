import yaml
from tests.test_init import client

"""
#########################################
#           Get all cages               #
#########################################
"""

def test_get_cages(request):
    # Configure test info in the report
    request.node._method = "GET"
    request.node._route = "/cage"
    request.node._title = "Test get all cages"
    request.node._description = "Pass if the status code is 200"

    #Request
    get_response = client.get("/cage")

    # Save response
    request.node._effective_status_code = get_response.status_code

    #Verify the result
    request.node._expected_status_code = 200
    assert get_response.status_code == 200

    # Save the log
    request.node._full_response = get_response.status_code


"""
#########################################
#           Get a cage                  #
#########################################
"""

def test_get_cage(request):
    # Configure test info in the report
    request.node._method = "GET"
    request.node._route = "/cage"
    request.node._title = "Test get a cage"
    request.node._description = "Pass if the status code is 200"

    # Request
    get_all = client.get("/cage")
    cage_id = get_all.json()[-1]["cage_id"]

    # Get a cage
    get_response = client.get(f"/cage/{cage_id}")

    # Save response
    request.node._effective_status_code = get_response.status_code

    #Verify the result
    request.node._expected_status_code = 200
    assert get_response.status_code == 200

    # Save the log
    request.node._full_response = get_response.status_code


# Get a cage error 404
def test_get_cage_notfound(request):
    # Configure test info in the report
    request.node._method = "GET"
    request.node._route = "/cage"
    request.node._title = "Test get a cage error 404"
    request.node._description = "Pass if the status code is 404"

    #Request
    get_all = client.get("/cage")
    cage_id = get_all.json()[-1]["cage_id"] + 1

    # Get a cage
    get_response = client.get(f"/cage/{cage_id}")

    # Save response
    request.node._effective_status_code = get_response.status_code

    #Verify the result
    request.node._expected_status_code = 404
    assert get_response.status_code == 404

    # Save the log
    request.node._full_response = get_response.status_code


import yaml
from tests.test_init import client

"""
#########################################
#           Delete a resource           #
#########################################
"""


# Delete the created test rat
def test_delete_rat(request):
    # Configure test info in the report
    request.node._method = "DELETE"
    request.node._route = "/rat"
    request.node._title = "Test delete a rat"
    request.node._description = "Pass if the status code is 204"

    # Request
    # Get the rat id
    get_response = client.get("/rat")
    rat_id = get_response.json()[-1]["rat_id"]

    # Delete the rat
    del_response = client.delete(f"/rat/{rat_id}")

    # Save response
    request.node._effective_status_code = del_response.status_code

    # Verify the result
    request.node._expected_status_code = 204
    assert del_response.status_code == 204

    # Save the log
    request.node._full_response = del_response.status_code


# Delete a rat error 404
def test_delete_rat_error404(request):
    # Configure test info in the report
    request.node._method = "DELETE"
    request.node._route = "/rat"
    request.node._title = "Test delete a rat error 404"
    request.node._description = "Pass if the status code is 404"

    # Request
    # Get the rat id
    get_response = client.get("/rat")
    rat_id = get_response.json()[-1]["rat_id"] + 1

    # Delete the rat
    del_response = client.delete(f"/rat/{rat_id}")

    # Save response
    request.node._effective_status_code = del_response.status_code

    # Verify the result
    request.node._expected_status_code = 404
    assert del_response.status_code == 404

    # Save the log
    request.node._full_response = del_response.status_code

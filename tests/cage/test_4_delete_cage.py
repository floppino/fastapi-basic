from tests.test_init import client

"""
#########################################
#           Delete a cage               #
#########################################
"""


# Delete the created test cage
def test_delete_cage(request):
    # Configure test info in the report
    request.node._method = "DELETE"
    request.node._route = "/cage"
    request.node._title = "Test delete a cage"
    request.node._description = "Pass if the status code is 204"

    # Request
    get_response = client.get("/cage")
    cage_id = get_response.json()[-1]["cage_id"]

    # Delete the cage
    del_response = client.delete(f"/cage/{cage_id}")

    # Save response
    request.node._effective_status_code = del_response.status_code

    # Verify the result
    request.node._expected_status_code = 204
    assert del_response.status_code == 204

    # Save the log
    request.node._full_response = del_response.status_code

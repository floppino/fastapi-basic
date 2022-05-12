import yaml
from tests.test_init import client

"""
#########################################
#           Update a cage               #
#########################################
"""


# Update a cage
def test_update_cage(request):
    # Configure test info in the report
    request.node._method = "PUT"
    request.node._route = "/cage"
    request.node._title = "Test update a cage"
    request.node._description = "Pass if the status code is 200"

    get_response = client.get("/cage")
    cage_data = get_response.json()[-1]
    cage_id = cage_data["cage_id"]
    cage_data["cage_name"] = "Updated_cage"

    # Update a cage
    put_response = client.put(f"/cage/{cage_id}", json=cage_data)

    # Save response
    request.node._effective_status_code = put_response.status_code

    #Verify the result
    request.node._expected_status_code = 200
    assert put_response.status_code == 200

    # Save the log
    request.node._full_response = put_response.json()

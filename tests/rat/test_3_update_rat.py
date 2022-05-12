import yaml
from tests.test_init import client

"""
#########################################
#           Update a rat                #
#########################################
"""


# Update a rat
def test_update_rat(request):
    # Configure test info in the report
    request.node._method = "PUT"
    request.node._route = "/rat"
    request.node._title = "Test update a rat"
    request.node._description = "Pass if the status code is 200"

    get_response = client.get("/rat")
    rat_data = get_response.json()[-1]
    rat_id = rat_data["rat_id"]
    rat_data["rat_name"] = "Updated_rat"

    # Update a rat
    put_response = client.put(f"/rat/{rat_id}", json=rat_data)

    # Save response
    request.node._effective_status_code = put_response.status_code

    #Verify the result
    request.node._expected_status_code = 200
    assert put_response.status_code == 200

    # Save the log
    request.node._full_response = put_response.json()
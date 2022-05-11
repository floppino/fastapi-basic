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
    with open("tests/test_data.yaml", "r") as yaml_file:
        data = yaml.safe_load(yaml_file)
        # Take the resource email
        rat_name = data["create_rat"][0]["rat_name"]
        owner_id = data["create_rat"][0]["owner_id"]
        # Get the resource data
        get_response = client.get("/rat")
        rat_id = 0
        for rat in get_response.json():
            if rat_name in list(rat.values()) and owner_id in list(rat.values()):
                rat_id = rat["rat_id"]

        # Delete the resource
        del_response = client.delete(f"/rat/{rat_id}")

        # Save response
        request.node._effective_status_code = del_response.status_code

        # Verify the result
        request.node._expected_status_code = 204
        assert del_response.status_code == 204

        # Save the log
        request.node._full_response = del_response.status_code

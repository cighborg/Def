Python
# File: scim_automation.py
# Purpose: Automated Identity Lifecycle Management (SCIM 2.0)

import requests

def enforce_identity_governance(user_id, status):
    """
    Automated 'Kill-Switch' logic: 
    If a contractor's status changes in the HR system, this script 
    immediately de-provisions access across all federal cloud environments.
    """
    scim_url = "https://identity-gateway.fed-cloud.gov/scim/v2/Users/"
    
    payload = {
        "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
        "active": False if status == "terminated" else True
    }
    
    # This replaces manual (human) de-provisioning which often lags by days.
    response = requests.patch(f"{scim_url}{user_id}", json=payload)
    return response.status_code

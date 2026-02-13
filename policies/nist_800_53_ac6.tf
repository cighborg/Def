Terraform
# File: nist_800_53_ac6.tf
# Purpose: Automated Enforcement of 'Least Privilege'

# This Security-as-Code (SaC) template prevents any user from 
# being assigned permanent administrative rights.

resource "google_iam_denylist" "prevent_perm_admin" {
  display_name = "NIST-AC6-Enforcement"
  
  # Logic: Deny permanent 'Owner' roles to all non-automated entities
  denied_principals = ["user:*"]
  denied_permissions = ["roles/owner", "roles/editor"]
  
  constraint {
    expression = "request.time < timestamp('2026-01-01T00:00:00Z')"
    title      = "Enforce Just-In-Time (JIT) Access"
  }
}

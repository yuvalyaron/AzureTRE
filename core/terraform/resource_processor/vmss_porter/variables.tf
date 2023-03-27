variable "tre_id" {}
variable "location" {}
variable "acr_id" {}
variable "resource_group_name" {}
variable "resource_processor_subnet_id" {}
variable "resource_processor_vmss_porter_image_repository" {}
variable "docker_registry_server" {}
variable "service_bus_namespace_id" {}
variable "service_bus_namespace_fqdn" {}
variable "service_bus_resource_request_queue" {}
variable "service_bus_deployment_status_update_queue" {}
variable "mgmt_storage_account_name" {}
variable "mgmt_resource_group_name" {}
variable "terraform_state_container_name" {}
variable "app_insights_connection_string" {}
variable "key_vault_name" {}
variable "key_vault_url" {}
variable "key_vault_id" {}
variable "resource_processor_number_processes_per_instance" {}
variable "resource_processor_vmss_sku" {}
variable "arm_environment" {}
variable "subscription_id" {
  description = "The subscription id to create the resource processor permission/role. If not supplied will use the TF context."
  type        = string
  default     = ""
}

variable "rp_bundle_values" {
  type = map(string)
}

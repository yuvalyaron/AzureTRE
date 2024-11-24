data "azurerm_subscription" "current" {}

data "azurerm_client_config" "current" {}

# Random unique id
resource "random_string" "unique_id" {
  length      = 4
  min_numeric = 4
}

data "azurerm_container_registry" "mgmt_acr" {
  name                = var.acr_name
  resource_group_name = var.mgmt_resource_group_name
}

data "azurerm_key_vault" "encryption_kv" {
  count               = var.enable_cmk_encryption && var.external_key_store_id == null ? 1 : 0
  name                = var.encryption_kv_name
  resource_group_name = var.mgmt_resource_group_name
}

data "azurerm_key_vault_key" "encryption_key" {
  count        = var.enable_cmk_encryption ? 1 : 0
  name         = var.kv_encryption_key_name
  key_vault_id = local.key_store_id
}

data "http" "myip" {
  count = var.public_deployment_ip_address == "" ? 1 : 0
  url   = "https://ipecho.net/plain"
}

data "azurerm_monitor_diagnostic_categories" "api" {
  resource_id = azurerm_linux_web_app.api.id
  depends_on = [
    azurerm_linux_web_app.api,
    azurerm_service_plan.core,
  ]
}

data "azurerm_monitor_diagnostic_categories" "sb" {
  resource_id = azurerm_servicebus_namespace.sb.id
  depends_on = [
    azurerm_servicebus_namespace.sb
  ]
}

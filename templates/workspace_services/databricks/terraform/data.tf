data "azurerm_resource_group" "ws" {
  name = local.resource_group_name
}

data "azurerm_virtual_network" "ws" {
  name                = local.virtual_network_name
  resource_group_name = data.azurerm_resource_group.ws.name
}

data "azurerm_firewall" "firewall" {
  name                = local.firewall_name
  resource_group_name = local.core_resource_group_name
}
data "azurerm_subnet" "services" {
  name                 = "ServicesSubnet"
  virtual_network_name = data.azurerm_virtual_network.ws.name
  resource_group_name  = data.azurerm_virtual_network.ws.resource_group_name
}

data "azurerm_private_dns_zone" "databricks" {
  name                = module.cloud_settings.private_links["privatelink.azuredatabricks.net"]
  resource_group_name = local.core_resource_group_name
}

data "azurerm_subscription" "current" {}

data "azurerm_private_dns_zone" "blobcore" {
  name                = module.cloud_settings.private_links["privatelink.blob.core.windows.net"]
  resource_group_name = local.core_resource_group_name
}

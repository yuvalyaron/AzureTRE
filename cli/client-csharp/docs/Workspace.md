# TRE.Rest.Client.Model.Workspace
Workspace request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | GUID identifying the resource request | 
**TemplateName** | **string** | The resource template (bundle) to deploy | 
**TemplateVersion** | **string** | The version of the resource template (bundle) to deploy | 
**Properties** | **Object** | Parameters for the deployment | [optional] 
**IsActive** | **bool** |  | [optional] [default to true]
**IsEnabled** | **bool** |  | [optional] [default to true]
**ResourceType** | **ResourceType** |  | [optional] 
**Etag** | **string** | eTag of the document | 
**ResourcePath** | **string** |  | [optional] [default to ""]
**ResourceVersion** | **int** |  | [optional] [default to 0]
**User** | **Object** |  | [optional] 
**UpdatedWhen** | **decimal** |  | [optional] [default to 0M]
**History** | [**Collection&lt;ResourceHistoryItem&gt;**](ResourceHistoryItem.md) |  | [optional] 
**WorkspaceURL** | **string** | Main endpoint for workspace users | [optional] [default to ""]
**AuthInformation** | **Object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


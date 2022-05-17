# TRE.Rest.Client.Model.Operation
Operation model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | GUID identifying the operation | 
**ResourceId** | **string** | GUID identifying the resource | 
**ResourcePath** | **string** | Path of the resource undergoing change, i.e. &#39;/workspaces/guid/workspace-services/guid/&#39; | 
**ResourceVersion** | **int** | Version of the resource this operation relates to | [optional] [default to 0]
**Status** | **Status** |  | [optional] 
**Action** | **string** | Name of the action being performed on the resource, i.e. install, uninstall, start | 
**Message** | **string** |  | [optional] [default to ""]
**CreatedWhen** | **decimal** |  | [optional] 
**UpdatedWhen** | **decimal** |  | [optional] 
**User** | **Object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


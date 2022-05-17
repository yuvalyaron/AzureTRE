# TRE.Rest.Client.Api.WorkspacesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateAWorkspaceApiWorkspacesPost**](WorkspacesApi.md#createaworkspaceapiworkspacespost) | **POST** /api/workspaces | Create A Workspace
[**DeleteWorkspaceApiWorkspacesWorkspaceIdDelete**](WorkspacesApi.md#deleteworkspaceapiworkspacesworkspaceiddelete) | **DELETE** /api/workspaces/{workspace_id} | Delete Workspace
[**GetASingleResourceOperationByIdApiWorkspacesWorkspaceIdOperationsOperationIdGet**](WorkspacesApi.md#getasingleresourceoperationbyidapiworkspacesworkspaceidoperationsoperationidget) | **GET** /api/workspaces/{workspace_id}/operations/{operation_id} | Get A Single Resource Operation By Id
[**GetAllOperationsForAResourceApiWorkspacesWorkspaceIdOperationsGet**](WorkspacesApi.md#getalloperationsforaresourceapiworkspacesworkspaceidoperationsget) | **GET** /api/workspaces/{workspace_id}/operations | Get All Operations For A Resource
[**GetAllWorkspacesApiWorkspacesGet**](WorkspacesApi.md#getallworkspacesapiworkspacesget) | **GET** /api/workspaces | Get All Workspaces
[**GetWorkspaceByIdApiWorkspacesWorkspaceIdGet**](WorkspacesApi.md#getworkspacebyidapiworkspacesworkspaceidget) | **GET** /api/workspaces/{workspace_id} | Get Workspace By Id
[**InvokeActionOnAWorkspaceApiWorkspacesWorkspaceIdInvokeActionPost**](WorkspacesApi.md#invokeactiononaworkspaceapiworkspacesworkspaceidinvokeactionpost) | **POST** /api/workspaces/{workspace_id}/invoke-action | Invoke Action On A Workspace
[**UpdateAnExistingWorkspaceApiWorkspacesWorkspaceIdPatch**](WorkspacesApi.md#updateanexistingworkspaceapiworkspacesworkspaceidpatch) | **PATCH** /api/workspaces/{workspace_id} | Update An Existing Workspace


<a name="createaworkspaceapiworkspacespost"></a>
# **CreateAWorkspaceApiWorkspacesPost**
> OperationInResponse CreateAWorkspaceApiWorkspacesPost (WorkspaceInCreate workspaceInCreate)

Create A Workspace

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class CreateAWorkspaceApiWorkspacesPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspacesApi(config);
            var workspaceInCreate = new WorkspaceInCreate(); // WorkspaceInCreate | 

            try
            {
                // Create A Workspace
                OperationInResponse result = apiInstance.CreateAWorkspaceApiWorkspacesPost(workspaceInCreate);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspacesApi.CreateAWorkspaceApiWorkspacesPost: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceInCreate** | [**WorkspaceInCreate**](WorkspaceInCreate.md)|  | 

### Return type

[**OperationInResponse**](OperationInResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="deleteworkspaceapiworkspacesworkspaceiddelete"></a>
# **DeleteWorkspaceApiWorkspacesWorkspaceIdDelete**
> OperationInResponse DeleteWorkspaceApiWorkspacesWorkspaceIdDelete (string workspaceId)

Delete Workspace

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class DeleteWorkspaceApiWorkspacesWorkspaceIdDeleteExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspacesApi(config);
            var workspaceId = "workspaceId_example";  // string | 

            try
            {
                // Delete Workspace
                OperationInResponse result = apiInstance.DeleteWorkspaceApiWorkspacesWorkspaceIdDelete(workspaceId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspacesApi.DeleteWorkspaceApiWorkspacesWorkspaceIdDelete: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceId** | **string**|  | 

### Return type

[**OperationInResponse**](OperationInResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getasingleresourceoperationbyidapiworkspacesworkspaceidoperationsoperationidget"></a>
# **GetASingleResourceOperationByIdApiWorkspacesWorkspaceIdOperationsOperationIdGet**
> OperationInResponse GetASingleResourceOperationByIdApiWorkspacesWorkspaceIdOperationsOperationIdGet (string workspaceId, string operationId)

Get A Single Resource Operation By Id

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetASingleResourceOperationByIdApiWorkspacesWorkspaceIdOperationsOperationIdGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspacesApi(config);
            var workspaceId = "workspaceId_example";  // string | 
            var operationId = "operationId_example";  // string | 

            try
            {
                // Get A Single Resource Operation By Id
                OperationInResponse result = apiInstance.GetASingleResourceOperationByIdApiWorkspacesWorkspaceIdOperationsOperationIdGet(workspaceId, operationId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspacesApi.GetASingleResourceOperationByIdApiWorkspacesWorkspaceIdOperationsOperationIdGet: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceId** | **string**|  | 
 **operationId** | **string**|  | 

### Return type

[**OperationInResponse**](OperationInResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getalloperationsforaresourceapiworkspacesworkspaceidoperationsget"></a>
# **GetAllOperationsForAResourceApiWorkspacesWorkspaceIdOperationsGet**
> OperationInList GetAllOperationsForAResourceApiWorkspacesWorkspaceIdOperationsGet (string workspaceId)

Get All Operations For A Resource

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetAllOperationsForAResourceApiWorkspacesWorkspaceIdOperationsGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspacesApi(config);
            var workspaceId = "workspaceId_example";  // string | 

            try
            {
                // Get All Operations For A Resource
                OperationInList result = apiInstance.GetAllOperationsForAResourceApiWorkspacesWorkspaceIdOperationsGet(workspaceId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspacesApi.GetAllOperationsForAResourceApiWorkspacesWorkspaceIdOperationsGet: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceId** | **string**|  | 

### Return type

[**OperationInList**](OperationInList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getallworkspacesapiworkspacesget"></a>
# **GetAllWorkspacesApiWorkspacesGet**
> WorkspacesInList GetAllWorkspacesApiWorkspacesGet ()

Get All Workspaces

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetAllWorkspacesApiWorkspacesGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspacesApi(config);

            try
            {
                // Get All Workspaces
                WorkspacesInList result = apiInstance.GetAllWorkspacesApiWorkspacesGet();
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspacesApi.GetAllWorkspacesApiWorkspacesGet: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WorkspacesInList**](WorkspacesInList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="getworkspacebyidapiworkspacesworkspaceidget"></a>
# **GetWorkspaceByIdApiWorkspacesWorkspaceIdGet**
> WorkspaceInResponse GetWorkspaceByIdApiWorkspacesWorkspaceIdGet (string workspaceId)

Get Workspace By Id

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetWorkspaceByIdApiWorkspacesWorkspaceIdGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspacesApi(config);
            var workspaceId = "workspaceId_example";  // string | 

            try
            {
                // Get Workspace By Id
                WorkspaceInResponse result = apiInstance.GetWorkspaceByIdApiWorkspacesWorkspaceIdGet(workspaceId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspacesApi.GetWorkspaceByIdApiWorkspacesWorkspaceIdGet: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceId** | **string**|  | 

### Return type

[**WorkspaceInResponse**](WorkspaceInResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="invokeactiononaworkspaceapiworkspacesworkspaceidinvokeactionpost"></a>
# **InvokeActionOnAWorkspaceApiWorkspacesWorkspaceIdInvokeActionPost**
> OperationInResponse InvokeActionOnAWorkspaceApiWorkspacesWorkspaceIdInvokeActionPost (string workspaceId, string action)

Invoke Action On A Workspace

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class InvokeActionOnAWorkspaceApiWorkspacesWorkspaceIdInvokeActionPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspacesApi(config);
            var workspaceId = "workspaceId_example";  // string | 
            var action = "action_example";  // string | 

            try
            {
                // Invoke Action On A Workspace
                OperationInResponse result = apiInstance.InvokeActionOnAWorkspaceApiWorkspacesWorkspaceIdInvokeActionPost(workspaceId, action);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspacesApi.InvokeActionOnAWorkspaceApiWorkspacesWorkspaceIdInvokeActionPost: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceId** | **string**|  | 
 **action** | **string**|  | 

### Return type

[**OperationInResponse**](OperationInResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="updateanexistingworkspaceapiworkspacesworkspaceidpatch"></a>
# **UpdateAnExistingWorkspaceApiWorkspacesWorkspaceIdPatch**
> OperationInResponse UpdateAnExistingWorkspaceApiWorkspacesWorkspaceIdPatch (string workspaceId, ResourcePatch resourcePatch, string etag = null)

Update An Existing Workspace

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class UpdateAnExistingWorkspaceApiWorkspacesWorkspaceIdPatchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspacesApi(config);
            var workspaceId = "workspaceId_example";  // string | 
            var resourcePatch = new ResourcePatch(); // ResourcePatch | 
            var etag = "etag_example";  // string |  (optional) 

            try
            {
                // Update An Existing Workspace
                OperationInResponse result = apiInstance.UpdateAnExistingWorkspaceApiWorkspacesWorkspaceIdPatch(workspaceId, resourcePatch, etag);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspacesApi.UpdateAnExistingWorkspaceApiWorkspacesWorkspaceIdPatch: " + e.Message );
                Debug.Print("Status Code: "+ e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceId** | **string**|  | 
 **resourcePatch** | [**ResourcePatch**](ResourcePatch.md)|  | 
 **etag** | **string**|  | [optional] 

### Return type

[**OperationInResponse**](OperationInResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


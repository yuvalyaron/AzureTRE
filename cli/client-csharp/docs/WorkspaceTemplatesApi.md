# TRE.Rest.Client.Api.WorkspaceTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetWorkspaceTemplateByNameApiWorkspaceTemplatesWorkspaceTemplateNameGet**](WorkspaceTemplatesApi.md#getworkspacetemplatebynameapiworkspacetemplatesworkspacetemplatenameget) | **GET** /api/workspace-templates/{workspace_template_name} | Get Workspace Template By Name
[**GetWorkspaceTemplatesApiWorkspaceTemplatesGet**](WorkspaceTemplatesApi.md#getworkspacetemplatesapiworkspacetemplatesget) | **GET** /api/workspace-templates | Get Workspace Templates
[**RegisterWorkspaceTemplateApiWorkspaceTemplatesPost**](WorkspaceTemplatesApi.md#registerworkspacetemplateapiworkspacetemplatespost) | **POST** /api/workspace-templates | Register Workspace Template


<a name="getworkspacetemplatebynameapiworkspacetemplatesworkspacetemplatenameget"></a>
# **GetWorkspaceTemplateByNameApiWorkspaceTemplatesWorkspaceTemplateNameGet**
> WorkspaceTemplateInResponse GetWorkspaceTemplateByNameApiWorkspaceTemplatesWorkspaceTemplateNameGet (string workspaceTemplateName, bool? isUpdate = null)

Get Workspace Template By Name

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetWorkspaceTemplateByNameApiWorkspaceTemplatesWorkspaceTemplateNameGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspaceTemplatesApi(config);
            var workspaceTemplateName = "workspaceTemplateName_example";  // string | 
            var isUpdate = false;  // bool? |  (optional)  (default to false)

            try
            {
                // Get Workspace Template By Name
                WorkspaceTemplateInResponse result = apiInstance.GetWorkspaceTemplateByNameApiWorkspaceTemplatesWorkspaceTemplateNameGet(workspaceTemplateName, isUpdate);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspaceTemplatesApi.GetWorkspaceTemplateByNameApiWorkspaceTemplatesWorkspaceTemplateNameGet: " + e.Message );
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
 **workspaceTemplateName** | **string**|  | 
 **isUpdate** | **bool?**|  | [optional] [default to false]

### Return type

[**WorkspaceTemplateInResponse**](WorkspaceTemplateInResponse.md)

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

<a name="getworkspacetemplatesapiworkspacetemplatesget"></a>
# **GetWorkspaceTemplatesApiWorkspaceTemplatesGet**
> ResourceTemplateInformationInList GetWorkspaceTemplatesApiWorkspaceTemplatesGet ()

Get Workspace Templates

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetWorkspaceTemplatesApiWorkspaceTemplatesGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspaceTemplatesApi(config);

            try
            {
                // Get Workspace Templates
                ResourceTemplateInformationInList result = apiInstance.GetWorkspaceTemplatesApiWorkspaceTemplatesGet();
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspaceTemplatesApi.GetWorkspaceTemplatesApiWorkspaceTemplatesGet: " + e.Message );
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

[**ResourceTemplateInformationInList**](ResourceTemplateInformationInList.md)

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

<a name="registerworkspacetemplateapiworkspacetemplatespost"></a>
# **RegisterWorkspaceTemplateApiWorkspaceTemplatesPost**
> WorkspaceTemplateInResponse RegisterWorkspaceTemplateApiWorkspaceTemplatesPost (WorkspaceTemplateInCreate workspaceTemplateInCreate)

Register Workspace Template

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class RegisterWorkspaceTemplateApiWorkspaceTemplatesPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspaceTemplatesApi(config);
            var workspaceTemplateInCreate = new WorkspaceTemplateInCreate(); // WorkspaceTemplateInCreate | 

            try
            {
                // Register Workspace Template
                WorkspaceTemplateInResponse result = apiInstance.RegisterWorkspaceTemplateApiWorkspaceTemplatesPost(workspaceTemplateInCreate);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspaceTemplatesApi.RegisterWorkspaceTemplateApiWorkspaceTemplatesPost: " + e.Message );
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
 **workspaceTemplateInCreate** | [**WorkspaceTemplateInCreate**](WorkspaceTemplateInCreate.md)|  | 

### Return type

[**WorkspaceTemplateInResponse**](WorkspaceTemplateInResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


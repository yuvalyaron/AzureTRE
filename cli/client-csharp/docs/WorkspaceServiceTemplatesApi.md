# TRE.Rest.Client.Api.WorkspaceServiceTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetWorkspaceServiceTemplateByNameApiWorkspaceServiceTemplatesServiceTemplateNameGet**](WorkspaceServiceTemplatesApi.md#getworkspaceservicetemplatebynameapiworkspaceservicetemplatesservicetemplatenameget) | **GET** /api/workspace-service-templates/{service_template_name} | Get Workspace Service Template By Name
[**GetWorkspaceServiceTemplatesApiWorkspaceServiceTemplatesGet**](WorkspaceServiceTemplatesApi.md#getworkspaceservicetemplatesapiworkspaceservicetemplatesget) | **GET** /api/workspace-service-templates | Get Workspace Service Templates
[**RegisterWorkspaceServiceTemplateApiWorkspaceServiceTemplatesPost**](WorkspaceServiceTemplatesApi.md#registerworkspaceservicetemplateapiworkspaceservicetemplatespost) | **POST** /api/workspace-service-templates | Register Workspace Service Template


<a name="getworkspaceservicetemplatebynameapiworkspaceservicetemplatesservicetemplatenameget"></a>
# **GetWorkspaceServiceTemplateByNameApiWorkspaceServiceTemplatesServiceTemplateNameGet**
> WorkspaceServiceTemplateInResponse GetWorkspaceServiceTemplateByNameApiWorkspaceServiceTemplatesServiceTemplateNameGet (string serviceTemplateName, bool? isUpdate = null)

Get Workspace Service Template By Name

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetWorkspaceServiceTemplateByNameApiWorkspaceServiceTemplatesServiceTemplateNameGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspaceServiceTemplatesApi(config);
            var serviceTemplateName = "serviceTemplateName_example";  // string | 
            var isUpdate = false;  // bool? |  (optional)  (default to false)

            try
            {
                // Get Workspace Service Template By Name
                WorkspaceServiceTemplateInResponse result = apiInstance.GetWorkspaceServiceTemplateByNameApiWorkspaceServiceTemplatesServiceTemplateNameGet(serviceTemplateName, isUpdate);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspaceServiceTemplatesApi.GetWorkspaceServiceTemplateByNameApiWorkspaceServiceTemplatesServiceTemplateNameGet: " + e.Message );
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
 **serviceTemplateName** | **string**|  | 
 **isUpdate** | **bool?**|  | [optional] [default to false]

### Return type

[**WorkspaceServiceTemplateInResponse**](WorkspaceServiceTemplateInResponse.md)

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

<a name="getworkspaceservicetemplatesapiworkspaceservicetemplatesget"></a>
# **GetWorkspaceServiceTemplatesApiWorkspaceServiceTemplatesGet**
> ResourceTemplateInformationInList GetWorkspaceServiceTemplatesApiWorkspaceServiceTemplatesGet ()

Get Workspace Service Templates

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetWorkspaceServiceTemplatesApiWorkspaceServiceTemplatesGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspaceServiceTemplatesApi(config);

            try
            {
                // Get Workspace Service Templates
                ResourceTemplateInformationInList result = apiInstance.GetWorkspaceServiceTemplatesApiWorkspaceServiceTemplatesGet();
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspaceServiceTemplatesApi.GetWorkspaceServiceTemplatesApiWorkspaceServiceTemplatesGet: " + e.Message );
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

<a name="registerworkspaceservicetemplateapiworkspaceservicetemplatespost"></a>
# **RegisterWorkspaceServiceTemplateApiWorkspaceServiceTemplatesPost**
> WorkspaceServiceTemplateInResponse RegisterWorkspaceServiceTemplateApiWorkspaceServiceTemplatesPost (WorkspaceServiceTemplateInCreate workspaceServiceTemplateInCreate)

Register Workspace Service Template

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class RegisterWorkspaceServiceTemplateApiWorkspaceServiceTemplatesPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new WorkspaceServiceTemplatesApi(config);
            var workspaceServiceTemplateInCreate = new WorkspaceServiceTemplateInCreate(); // WorkspaceServiceTemplateInCreate | 

            try
            {
                // Register Workspace Service Template
                WorkspaceServiceTemplateInResponse result = apiInstance.RegisterWorkspaceServiceTemplateApiWorkspaceServiceTemplatesPost(workspaceServiceTemplateInCreate);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling WorkspaceServiceTemplatesApi.RegisterWorkspaceServiceTemplateApiWorkspaceServiceTemplatesPost: " + e.Message );
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
 **workspaceServiceTemplateInCreate** | [**WorkspaceServiceTemplateInCreate**](WorkspaceServiceTemplateInCreate.md)|  | 

### Return type

[**WorkspaceServiceTemplateInResponse**](WorkspaceServiceTemplateInResponse.md)

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


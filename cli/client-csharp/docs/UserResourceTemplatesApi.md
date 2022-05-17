# TRE.Rest.Client.Api.UserResourceTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetUserResourceTemplateByNameAndWorkspaceServiceApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesUserResourceTemplateNameGet**](UserResourceTemplatesApi.md#getuserresourcetemplatebynameandworkspaceserviceapiworkspaceservicetemplatesservicetemplatenameuserresourcetemplatesuserresourcetemplatenameget) | **GET** /api/workspace-service-templates/{service_template_name}/user-resource-templates/{user_resource_template_name} | Get User Resource Template By Name And Workspace Service
[**GetUserResourceTemplatesApplicableToTheWorkspaceServiceTemplateApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesGet**](UserResourceTemplatesApi.md#getuserresourcetemplatesapplicabletotheworkspaceservicetemplateapiworkspaceservicetemplatesservicetemplatenameuserresourcetemplatesget) | **GET** /api/workspace-service-templates/{service_template_name}/user-resource-templates | Get User Resource Templates Applicable To The Workspace Service Template
[**RegisterUserResourceTemplateApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesPost**](UserResourceTemplatesApi.md#registeruserresourcetemplateapiworkspaceservicetemplatesservicetemplatenameuserresourcetemplatespost) | **POST** /api/workspace-service-templates/{service_template_name}/user-resource-templates | Register User Resource Template


<a name="getuserresourcetemplatebynameandworkspaceserviceapiworkspaceservicetemplatesservicetemplatenameuserresourcetemplatesuserresourcetemplatenameget"></a>
# **GetUserResourceTemplateByNameAndWorkspaceServiceApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesUserResourceTemplateNameGet**
> UserResourceTemplateInResponse GetUserResourceTemplateByNameAndWorkspaceServiceApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesUserResourceTemplateNameGet (string serviceTemplateName, string userResourceTemplateName, bool? isUpdate = null)

Get User Resource Template By Name And Workspace Service

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetUserResourceTemplateByNameAndWorkspaceServiceApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesUserResourceTemplateNameGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new UserResourceTemplatesApi(config);
            var serviceTemplateName = "serviceTemplateName_example";  // string | 
            var userResourceTemplateName = "userResourceTemplateName_example";  // string | 
            var isUpdate = false;  // bool? |  (optional)  (default to false)

            try
            {
                // Get User Resource Template By Name And Workspace Service
                UserResourceTemplateInResponse result = apiInstance.GetUserResourceTemplateByNameAndWorkspaceServiceApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesUserResourceTemplateNameGet(serviceTemplateName, userResourceTemplateName, isUpdate);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling UserResourceTemplatesApi.GetUserResourceTemplateByNameAndWorkspaceServiceApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesUserResourceTemplateNameGet: " + e.Message );
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
 **userResourceTemplateName** | **string**|  | 
 **isUpdate** | **bool?**|  | [optional] [default to false]

### Return type

[**UserResourceTemplateInResponse**](UserResourceTemplateInResponse.md)

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

<a name="getuserresourcetemplatesapplicabletotheworkspaceservicetemplateapiworkspaceservicetemplatesservicetemplatenameuserresourcetemplatesget"></a>
# **GetUserResourceTemplatesApplicableToTheWorkspaceServiceTemplateApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesGet**
> ResourceTemplateInformationInList GetUserResourceTemplatesApplicableToTheWorkspaceServiceTemplateApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesGet (string serviceTemplateName)

Get User Resource Templates Applicable To The Workspace Service Template

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetUserResourceTemplatesApplicableToTheWorkspaceServiceTemplateApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new UserResourceTemplatesApi(config);
            var serviceTemplateName = "serviceTemplateName_example";  // string | 

            try
            {
                // Get User Resource Templates Applicable To The Workspace Service Template
                ResourceTemplateInformationInList result = apiInstance.GetUserResourceTemplatesApplicableToTheWorkspaceServiceTemplateApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesGet(serviceTemplateName);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling UserResourceTemplatesApi.GetUserResourceTemplatesApplicableToTheWorkspaceServiceTemplateApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesGet: " + e.Message );
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
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="registeruserresourcetemplateapiworkspaceservicetemplatesservicetemplatenameuserresourcetemplatespost"></a>
# **RegisterUserResourceTemplateApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesPost**
> UserResourceTemplateInResponse RegisterUserResourceTemplateApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesPost (string serviceTemplateName, UserResourceTemplateInCreate userResourceTemplateInCreate)

Register User Resource Template

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class RegisterUserResourceTemplateApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new UserResourceTemplatesApi(config);
            var serviceTemplateName = "serviceTemplateName_example";  // string | 
            var userResourceTemplateInCreate = new UserResourceTemplateInCreate(); // UserResourceTemplateInCreate | 

            try
            {
                // Register User Resource Template
                UserResourceTemplateInResponse result = apiInstance.RegisterUserResourceTemplateApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesPost(serviceTemplateName, userResourceTemplateInCreate);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling UserResourceTemplatesApi.RegisterUserResourceTemplateApiWorkspaceServiceTemplatesServiceTemplateNameUserResourceTemplatesPost: " + e.Message );
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
 **userResourceTemplateInCreate** | [**UserResourceTemplateInCreate**](UserResourceTemplateInCreate.md)|  | 

### Return type

[**UserResourceTemplateInResponse**](UserResourceTemplateInResponse.md)

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


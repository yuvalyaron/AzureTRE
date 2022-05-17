# TRE.Rest.Client.Api.SharedServiceTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetSharedServiceTemplateByNameApiSharedServiceTemplatesSharedServiceTemplateNameGet**](SharedServiceTemplatesApi.md#getsharedservicetemplatebynameapisharedservicetemplatessharedservicetemplatenameget) | **GET** /api/shared-service-templates/{shared_service_template_name} | Get Shared Service Template By Name
[**GetSharedServiceTemplatesApiSharedServiceTemplatesGet**](SharedServiceTemplatesApi.md#getsharedservicetemplatesapisharedservicetemplatesget) | **GET** /api/shared-service-templates | Get Shared Service Templates
[**RegisterSharedServiceTemplateApiSharedServiceTemplatesPost**](SharedServiceTemplatesApi.md#registersharedservicetemplateapisharedservicetemplatespost) | **POST** /api/shared-service-templates | Register Shared Service Template


<a name="getsharedservicetemplatebynameapisharedservicetemplatessharedservicetemplatenameget"></a>
# **GetSharedServiceTemplateByNameApiSharedServiceTemplatesSharedServiceTemplateNameGet**
> SharedServiceTemplateInResponse GetSharedServiceTemplateByNameApiSharedServiceTemplatesSharedServiceTemplateNameGet (string sharedServiceTemplateName)

Get Shared Service Template By Name

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetSharedServiceTemplateByNameApiSharedServiceTemplatesSharedServiceTemplateNameGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new SharedServiceTemplatesApi(config);
            var sharedServiceTemplateName = "sharedServiceTemplateName_example";  // string | 

            try
            {
                // Get Shared Service Template By Name
                SharedServiceTemplateInResponse result = apiInstance.GetSharedServiceTemplateByNameApiSharedServiceTemplatesSharedServiceTemplateNameGet(sharedServiceTemplateName);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SharedServiceTemplatesApi.GetSharedServiceTemplateByNameApiSharedServiceTemplatesSharedServiceTemplateNameGet: " + e.Message );
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
 **sharedServiceTemplateName** | **string**|  | 

### Return type

[**SharedServiceTemplateInResponse**](SharedServiceTemplateInResponse.md)

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

<a name="getsharedservicetemplatesapisharedservicetemplatesget"></a>
# **GetSharedServiceTemplatesApiSharedServiceTemplatesGet**
> ResourceTemplateInformationInList GetSharedServiceTemplatesApiSharedServiceTemplatesGet ()

Get Shared Service Templates

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetSharedServiceTemplatesApiSharedServiceTemplatesGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new SharedServiceTemplatesApi(config);

            try
            {
                // Get Shared Service Templates
                ResourceTemplateInformationInList result = apiInstance.GetSharedServiceTemplatesApiSharedServiceTemplatesGet();
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SharedServiceTemplatesApi.GetSharedServiceTemplatesApiSharedServiceTemplatesGet: " + e.Message );
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

<a name="registersharedservicetemplateapisharedservicetemplatespost"></a>
# **RegisterSharedServiceTemplateApiSharedServiceTemplatesPost**
> SharedServiceTemplateInResponse RegisterSharedServiceTemplateApiSharedServiceTemplatesPost (SharedServiceTemplateInCreate sharedServiceTemplateInCreate)

Register Shared Service Template

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class RegisterSharedServiceTemplateApiSharedServiceTemplatesPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new SharedServiceTemplatesApi(config);
            var sharedServiceTemplateInCreate = new SharedServiceTemplateInCreate(); // SharedServiceTemplateInCreate | 

            try
            {
                // Register Shared Service Template
                SharedServiceTemplateInResponse result = apiInstance.RegisterSharedServiceTemplateApiSharedServiceTemplatesPost(sharedServiceTemplateInCreate);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SharedServiceTemplatesApi.RegisterSharedServiceTemplateApiSharedServiceTemplatesPost: " + e.Message );
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
 **sharedServiceTemplateInCreate** | [**SharedServiceTemplateInCreate**](SharedServiceTemplateInCreate.md)|  | 

### Return type

[**SharedServiceTemplateInResponse**](SharedServiceTemplateInResponse.md)

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


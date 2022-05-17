# TRE.Rest.Client.Api.SharedServicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateASharedServiceApiSharedServicesPost**](SharedServicesApi.md#createasharedserviceapisharedservicespost) | **POST** /api/shared-services | Create A Shared Service
[**DeleteSharedServiceApiSharedServicesSharedServiceIdDelete**](SharedServicesApi.md#deletesharedserviceapisharedservicessharedserviceiddelete) | **DELETE** /api/shared-services/{shared_service_id} | Delete Shared Service
[**GetASingleResourceOperationByIdApiSharedServicesSharedServiceIdOperationsOperationIdGet**](SharedServicesApi.md#getasingleresourceoperationbyidapisharedservicessharedserviceidoperationsoperationidget) | **GET** /api/shared-services/{shared_service_id}/operations/{operation_id} | Get A Single Resource Operation By Id
[**GetAllOperationsForAResourceApiSharedServicesSharedServiceIdOperationsGet**](SharedServicesApi.md#getalloperationsforaresourceapisharedservicessharedserviceidoperationsget) | **GET** /api/shared-services/{shared_service_id}/operations | Get All Operations For A Resource
[**GetAllSharedServicesApiSharedServicesGet**](SharedServicesApi.md#getallsharedservicesapisharedservicesget) | **GET** /api/shared-services | Get All Shared Services
[**GetSharedServiceByIdApiSharedServicesSharedServiceIdGet**](SharedServicesApi.md#getsharedservicebyidapisharedservicessharedserviceidget) | **GET** /api/shared-services/{shared_service_id} | Get Shared Service By Id
[**InvokeActionOnASharedServiceApiSharedServicesSharedServiceIdInvokeActionPost**](SharedServicesApi.md#invokeactiononasharedserviceapisharedservicessharedserviceidinvokeactionpost) | **POST** /api/shared-services/{shared_service_id}/invoke-action | Invoke Action On A Shared Service
[**UpdateAnExistingSharedServiceApiSharedServicesSharedServiceIdPatch**](SharedServicesApi.md#updateanexistingsharedserviceapisharedservicessharedserviceidpatch) | **PATCH** /api/shared-services/{shared_service_id} | Update An Existing Shared Service


<a name="createasharedserviceapisharedservicespost"></a>
# **CreateASharedServiceApiSharedServicesPost**
> OperationInResponse CreateASharedServiceApiSharedServicesPost (SharedServiceInCreate sharedServiceInCreate)

Create A Shared Service

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class CreateASharedServiceApiSharedServicesPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new SharedServicesApi(config);
            var sharedServiceInCreate = new SharedServiceInCreate(); // SharedServiceInCreate | 

            try
            {
                // Create A Shared Service
                OperationInResponse result = apiInstance.CreateASharedServiceApiSharedServicesPost(sharedServiceInCreate);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SharedServicesApi.CreateASharedServiceApiSharedServicesPost: " + e.Message );
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
 **sharedServiceInCreate** | [**SharedServiceInCreate**](SharedServiceInCreate.md)|  | 

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

<a name="deletesharedserviceapisharedservicessharedserviceiddelete"></a>
# **DeleteSharedServiceApiSharedServicesSharedServiceIdDelete**
> OperationInResponse DeleteSharedServiceApiSharedServicesSharedServiceIdDelete (string sharedServiceId)

Delete Shared Service

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class DeleteSharedServiceApiSharedServicesSharedServiceIdDeleteExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new SharedServicesApi(config);
            var sharedServiceId = "sharedServiceId_example";  // string | 

            try
            {
                // Delete Shared Service
                OperationInResponse result = apiInstance.DeleteSharedServiceApiSharedServicesSharedServiceIdDelete(sharedServiceId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SharedServicesApi.DeleteSharedServiceApiSharedServicesSharedServiceIdDelete: " + e.Message );
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
 **sharedServiceId** | **string**|  | 

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

<a name="getasingleresourceoperationbyidapisharedservicessharedserviceidoperationsoperationidget"></a>
# **GetASingleResourceOperationByIdApiSharedServicesSharedServiceIdOperationsOperationIdGet**
> OperationInResponse GetASingleResourceOperationByIdApiSharedServicesSharedServiceIdOperationsOperationIdGet (string sharedServiceId, string operationId)

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
    public class GetASingleResourceOperationByIdApiSharedServicesSharedServiceIdOperationsOperationIdGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new SharedServicesApi(config);
            var sharedServiceId = "sharedServiceId_example";  // string | 
            var operationId = "operationId_example";  // string | 

            try
            {
                // Get A Single Resource Operation By Id
                OperationInResponse result = apiInstance.GetASingleResourceOperationByIdApiSharedServicesSharedServiceIdOperationsOperationIdGet(sharedServiceId, operationId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SharedServicesApi.GetASingleResourceOperationByIdApiSharedServicesSharedServiceIdOperationsOperationIdGet: " + e.Message );
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
 **sharedServiceId** | **string**|  | 
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

<a name="getalloperationsforaresourceapisharedservicessharedserviceidoperationsget"></a>
# **GetAllOperationsForAResourceApiSharedServicesSharedServiceIdOperationsGet**
> OperationInList GetAllOperationsForAResourceApiSharedServicesSharedServiceIdOperationsGet (string sharedServiceId)

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
    public class GetAllOperationsForAResourceApiSharedServicesSharedServiceIdOperationsGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new SharedServicesApi(config);
            var sharedServiceId = "sharedServiceId_example";  // string | 

            try
            {
                // Get All Operations For A Resource
                OperationInList result = apiInstance.GetAllOperationsForAResourceApiSharedServicesSharedServiceIdOperationsGet(sharedServiceId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SharedServicesApi.GetAllOperationsForAResourceApiSharedServicesSharedServiceIdOperationsGet: " + e.Message );
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
 **sharedServiceId** | **string**|  | 

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

<a name="getallsharedservicesapisharedservicesget"></a>
# **GetAllSharedServicesApiSharedServicesGet**
> SharedServicesInList GetAllSharedServicesApiSharedServicesGet ()

Get All Shared Services

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetAllSharedServicesApiSharedServicesGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new SharedServicesApi(config);

            try
            {
                // Get All Shared Services
                SharedServicesInList result = apiInstance.GetAllSharedServicesApiSharedServicesGet();
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SharedServicesApi.GetAllSharedServicesApiSharedServicesGet: " + e.Message );
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

[**SharedServicesInList**](SharedServicesInList.md)

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

<a name="getsharedservicebyidapisharedservicessharedserviceidget"></a>
# **GetSharedServiceByIdApiSharedServicesSharedServiceIdGet**
> SharedServiceInResponse GetSharedServiceByIdApiSharedServicesSharedServiceIdGet (string sharedServiceId)

Get Shared Service By Id

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class GetSharedServiceByIdApiSharedServicesSharedServiceIdGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new SharedServicesApi(config);
            var sharedServiceId = "sharedServiceId_example";  // string | 

            try
            {
                // Get Shared Service By Id
                SharedServiceInResponse result = apiInstance.GetSharedServiceByIdApiSharedServicesSharedServiceIdGet(sharedServiceId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SharedServicesApi.GetSharedServiceByIdApiSharedServicesSharedServiceIdGet: " + e.Message );
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
 **sharedServiceId** | **string**|  | 

### Return type

[**SharedServiceInResponse**](SharedServiceInResponse.md)

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

<a name="invokeactiononasharedserviceapisharedservicessharedserviceidinvokeactionpost"></a>
# **InvokeActionOnASharedServiceApiSharedServicesSharedServiceIdInvokeActionPost**
> OperationInResponse InvokeActionOnASharedServiceApiSharedServicesSharedServiceIdInvokeActionPost (string sharedServiceId, string action)

Invoke Action On A Shared Service

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class InvokeActionOnASharedServiceApiSharedServicesSharedServiceIdInvokeActionPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new SharedServicesApi(config);
            var sharedServiceId = "sharedServiceId_example";  // string | 
            var action = "action_example";  // string | 

            try
            {
                // Invoke Action On A Shared Service
                OperationInResponse result = apiInstance.InvokeActionOnASharedServiceApiSharedServicesSharedServiceIdInvokeActionPost(sharedServiceId, action);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SharedServicesApi.InvokeActionOnASharedServiceApiSharedServicesSharedServiceIdInvokeActionPost: " + e.Message );
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
 **sharedServiceId** | **string**|  | 
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

<a name="updateanexistingsharedserviceapisharedservicessharedserviceidpatch"></a>
# **UpdateAnExistingSharedServiceApiSharedServicesSharedServiceIdPatch**
> SharedServiceInResponse UpdateAnExistingSharedServiceApiSharedServicesSharedServiceIdPatch (string sharedServiceId, ResourcePatch resourcePatch, string etag = null)

Update An Existing Shared Service

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using TRE.Rest.Client.Api;
using TRE.Rest.Client.Client;
using TRE.Rest.Client.Model;

namespace Example
{
    public class UpdateAnExistingSharedServiceApiSharedServicesSharedServiceIdPatchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            // Configure OAuth2 access token for authorization: oauth2
            config.AccessToken = "YOUR_ACCESS_TOKEN";

            var apiInstance = new SharedServicesApi(config);
            var sharedServiceId = "sharedServiceId_example";  // string | 
            var resourcePatch = new ResourcePatch(); // ResourcePatch | 
            var etag = "etag_example";  // string |  (optional) 

            try
            {
                // Update An Existing Shared Service
                SharedServiceInResponse result = apiInstance.UpdateAnExistingSharedServiceApiSharedServicesSharedServiceIdPatch(sharedServiceId, resourcePatch, etag);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling SharedServicesApi.UpdateAnExistingSharedServiceApiSharedServicesSharedServiceIdPatch: " + e.Message );
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
 **sharedServiceId** | **string**|  | 
 **resourcePatch** | [**ResourcePatch**](ResourcePatch.md)|  | 
 **etag** | **string**|  | [optional] 

### Return type

[**SharedServiceInResponse**](SharedServiceInResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


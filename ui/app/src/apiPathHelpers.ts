import { ApiEndpoint } from "./models/apiEndpoints";
import { ResourceType } from "./models/resourceType";
import { Workspace } from "./models/workspace";
import { WorkspaceService } from "./models/workspaceService";

/**
 * Construct API path for templates of specified resourceType
 * @param resourceType 
 * @param parentResource
 * @returns API templates path
 */
export const getTemplatesPath = (resourceType: ResourceType, parentResource?: Workspace | WorkspaceService): string => {
    switch (resourceType) {
        case ResourceType.Workspace:
            return ApiEndpoint.WorkspaceTemplates;
        case ResourceType.WorkspaceService:
            return ApiEndpoint.WorkspaceServiceTemplates;
        case ResourceType.SharedService:
            return ApiEndpoint.SharedServiceTemplates;
        case ResourceType.UserResource:
            if (!parentResource) {
                throw Error('Parent workspace service must be passed as prop when creating user resource.');
            }
            return `${ApiEndpoint.WorkspaceServiceTemplates}/${parentResource.templateName}/${ApiEndpoint.UserResourceTemplates}`;
        default:
            throw Error('Unsupported resource type.');
    }
}

/**
 * Construct API path for resources of specified resourceType
 * @param resourceType
 * @param parentResource
 * @returns API resources path
 */
export const getResourcesPath = (resourceType: ResourceType, parentResource?: Workspace | WorkspaceService): string => {
    switch (resourceType) {
        case ResourceType.Workspace:
            return ApiEndpoint.Workspaces;
        case ResourceType.SharedService:
            return ApiEndpoint.SharedServices;
        default:
            if (!parentResource) {
                throw Error('A parentResource must be passed as prop if creating a workspace-service or user-resource');
            }
            return `${parentResource.resourcePath}/${resourceType}`;
    }
}

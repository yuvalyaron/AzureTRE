import React, { useContext, useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { ApiEndpoint } from '../../models/apiEndpoints';
import { useAuthApiCall, HttpMethod } from '../../hooks/useAuthApiCall';
import { UserResource } from '../../models/userResource';
import { WorkspaceService } from '../../models/workspaceService';
import { ResourceDebug } from '../shared/ResourceDebug';
import { MessageBar, MessageBarType, Pivot, PivotItem, PrimaryButton, Spinner, SpinnerSize, Stack } from '@fluentui/react';
import { ResourcePropertyPanel } from '../shared/ResourcePropertyPanel';
import { ComponentAction, Resource } from '../../models/resource';
import { ResourceCardList } from '../shared/ResourceCardList';
import { LoadingState } from '../../models/loadingState';
import { WorkspaceContext } from '../../contexts/WorkspaceContext';
import { ResourceType } from '../../models/resourceType';
import { ResourceHistory } from '../shared/ResourceHistory';
import { ResourceHeader } from '../shared/ResourceHeader';
import { useComponentManager } from '../../hooks/useComponentManager';
import { ResourceOperationsList } from '../shared/ResourceOperationsList';
import { CreateUpdateResourceContext } from '../../contexts/CreateUpdateResourceContext';

interface WorkspaceServiceItemProps {
  workspaceService?: WorkspaceService,
  setUserResource: (userResource: UserResource) => void
}

export const WorkspaceServiceItem: React.FunctionComponent<WorkspaceServiceItemProps> = (props: WorkspaceServiceItemProps) => {
  const { workspaceServiceId } = useParams();
  const [userResources, setUserResources] = useState([] as Array<UserResource>)
  const [workspaceService, setWorkspaceService] = useState({} as WorkspaceService)
  const [loadingState, setLoadingState] = useState(LoadingState.Loading);
  const workspaceCtx = useContext(WorkspaceContext);
  const createFormCtx = useContext(CreateUpdateResourceContext);
  const navigate = useNavigate();
  const apiCall = useAuthApiCall();
  const componentAction = useComponentManager(
    workspaceService,
    (r: Resource) => setWorkspaceService(r as WorkspaceService),
    (r: Resource) => navigate(`/${ApiEndpoint.Workspaces}/${workspaceCtx.workspace.id}/${ApiEndpoint.WorkspaceServices}`)
  );

  useEffect(() => {
    const getData = async () => {
      try {
        // did we get passed the workspace service, or shall we get it from the api?
        if (props.workspaceService && props.workspaceService.id) {
          setWorkspaceService(props.workspaceService);
        } else {
          let ws = await apiCall(`${ApiEndpoint.Workspaces}/${workspaceCtx.workspace.id}/${ApiEndpoint.WorkspaceServices}/${workspaceServiceId}`, HttpMethod.Get, workspaceCtx.workspaceClientId);
          setWorkspaceService(ws.workspaceService);
        }

        // get the user resources
        const u = await apiCall(`${ApiEndpoint.Workspaces}/${workspaceCtx.workspace.id}/${ApiEndpoint.WorkspaceServices}/${workspaceServiceId}/${ApiEndpoint.UserResources}`, HttpMethod.Get, workspaceCtx.workspaceClientId)
        setUserResources(u.userResources);
        setLoadingState(LoadingState.Ok);
      } catch {
        setLoadingState(LoadingState.Error);
      }
    };
    getData();
  }, [apiCall, props.workspaceService, workspaceCtx.workspace.id, workspaceCtx.workspaceClientId, workspaceServiceId]);

  const addUserResource = (u: UserResource) => {
    let ur = [...userResources];
    ur.push(u);
    setUserResources(ur);
  }

  const updateUserResource = (u: UserResource) => {
    let ur = [...userResources];
    let i = ur.findIndex((f: UserResource) => f.id === u.id);
    ur.splice(i, 1, u);
    setUserResources(ur);
  }

  const removeUserResource = (u: UserResource) => {
    let ur = [...userResources];
    let i = ur.findIndex((f: UserResource) => f.id === u.id);
    ur.splice(i, 1);
    setUserResources(ur);
  }

  switch (loadingState) {
    case LoadingState.Ok:
      return (
        <>
          <ResourceHeader resource={workspaceService} componentAction={componentAction} />
          <Pivot aria-label="User Resource Menu" className='tre-panel'>
            <PivotItem
              headerText="Overview"
              headerButtonProps={{
                'data-order': 1,
                'data-title': 'Overview',
              }}
            >
              <ResourcePropertyPanel resource={workspaceService} />

              <ResourceDebug resource={workspaceService} />
            </PivotItem>
            <PivotItem headerText="History">
              <ResourceHistory history={workspaceService.history} />
            </PivotItem>
            <PivotItem headerText="Operations">
              <ResourceOperationsList resource={workspaceService} />
            </PivotItem>
          </Pivot>

          <Stack className="tre-panel">
            <Stack.Item>
              <Stack horizontal horizontalAlign="space-between">
                <h1>User Resources</h1>
                <PrimaryButton iconProps={{ iconName: 'Add' }} text="Create new" disabled={!workspaceService.isEnabled || componentAction === ComponentAction.Lock} title={!workspaceService.isEnabled ? 'Service must be enabled first' : 'Create a User Resource'}
                  onClick={() => {
                    createFormCtx.openCreateForm({
                      resourceType: ResourceType.UserResource,
                      resourceParent: props.workspaceService,
                      onAdd: (r: Resource) => addUserResource(r as UserResource),
                      workspaceClientId: workspaceCtx.workspaceClientId
                    })
                  }} />
              </Stack>
            </Stack.Item>
            <Stack.Item>
              {
                userResources &&
                <ResourceCardList
                  resources={userResources}
                  selectResource={(r: Resource) => props.setUserResource(r as UserResource)}
                  updateResource={(r: Resource) => updateUserResource(r as UserResource)}
                  removeResource={(r: Resource) => removeUserResource(r as UserResource)}
                  emptyText="This workspace service contains no user resources." />
              }
            </Stack.Item>
          </Stack>
        </>
      );
    case LoadingState.Error:
      return (
        <MessageBar
          messageBarType={MessageBarType.error}
          isMultiline={true}
        >
          <h3>Error retrieving workspace</h3>
          <p>There was an error retrieving this workspace. Please see the browser console for details.</p>
        </MessageBar>
      );
    default:
      return (
        <div style={{ marginTop: '20px' }}>
          <Spinner label="Loading Workspace Service" ariaLive="assertive" labelPosition="top" size={SpinnerSize.large} />
        </div>
      )
  }
};

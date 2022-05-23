import { Icon, mergeStyles, Panel, PanelType, PrimaryButton } from '@fluentui/react';
import React, { useContext, useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Operation } from '../../../models/operation';
import { ResourceType } from '../../../models/resourceType';
import { Workspace } from '../../../models/workspace';
import { WorkspaceService } from '../../../models/workspaceService';
import { NotificationsContext } from '../../../contexts/NotificationsContext';
import { ResourceForm } from './ResourceForm';
import { getResourcesPath, getTemplatesPath } from '../../../apiPathHelpers';

interface UpdateResourceProps {
  isOpen: boolean,
  onClose: () => void,
  resourceType: ResourceType,
  parentResource?: Workspace | WorkspaceService
}

interface PageTitle {
  resourceForm: string,
  updating: string
}

const updatingIconClass = mergeStyles({
  fontSize: 100,
  height: 100,
  width: 100,
  margin: '0 25px',
  color: 'deepskyblue',
  padding: 20
});

export const UpdateResource: React.FunctionComponent<UpdateResourceProps> = (props: UpdateResourceProps) => {
  const [page, setPage] = useState('resourceForm' as keyof PageTitle);
  const [selectedTemplate, setTemplate] = useState('');
  const [deployOperation, setDeployOperation] = useState({} as Operation);
  const opsContext = useContext(NotificationsContext);
  const navigate = useNavigate();

  useEffect(() => {
    const clearState = () => {
      setPage('resourceForm');
      setDeployOperation({} as Operation);
      setTemplate('');
    }

    // Clear state on panel close
    if (!props.isOpen) {
      clearState();
    }
  }, [props.isOpen]);

  // Render a panel title depending on sub-page
  const pageTitles: PageTitle = {
    resourceForm: 'Update ' + props.resourceType,
    updating: ''
  }

  const resourceUpdating = (operation: Operation) => {
    setDeployOperation(operation);
    setPage('updating');
    // Add deployment operation to notifications operation poller
    opsContext.addOperation(operation);
  }

  const templatesPath = getTemplatesPath(props.resourceType, props.parentResource);
  const resourcesPath = getResourcesPath(props.resourceType, props.parentResource);

  // Render the current panel sub-page
  let currentPage;
  switch(page) {
    case 'resourceForm':
      currentPage = <ResourceForm 
        templateName={selectedTemplate}
        templatePath={`${templatesPath}/${selectedTemplate}`}
        resourcesPath={resourcesPath}
        onCreateResource={resourceUpdating}
      />; break;
    case 'updating':
      currentPage = <div style={{ textAlign: 'center', paddingTop: 100 }}>
        <Icon iconName="CloudAdd" className={updatingIconClass} />
        <h1>Updating {props.resourceType}...</h1>
        <p>Check the notifications panel for deployment progress.</p>
        <PrimaryButton text="Go to resource" onClick={() => navigate(deployOperation.resourcePath)}/>
      </div>; break;
  }

  return (
    <>
      <Panel
        headerText={pageTitles[page]}
        isOpen={props.isOpen}
        onDismiss={props.onClose}
        type={PanelType.medium}
        closeButtonAriaLabel="Close"
      >
        { currentPage }
      </Panel>
    </>
  );
};

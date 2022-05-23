import { Icon, mergeStyles, Panel, PanelType, PrimaryButton } from '@fluentui/react';
import React, { useContext, useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Operation } from '../../../models/operation';
import { ResourceType } from '../../../models/resourceType';
import { Workspace } from '../../../models/workspace';
import { WorkspaceService } from '../../../models/workspaceService';
import { NotificationsContext } from '../../../contexts/NotificationsContext';
import { ResourceForm } from './ResourceForm';
import { SelectTemplate } from './SelectTemplate';
import { getResourcesPath, getTemplatesPath } from '../../../apiPathHelpers';

interface CreateResourceProps {
  isOpen: boolean,
  onClose: () => void,
  resourceType: ResourceType,
  parentResource?: Workspace | WorkspaceService
}

interface PageTitle {
  selectTemplate: string,
  resourceForm: string,
  creating: string
}

const creatingIconClass = mergeStyles({
  fontSize: 100,
  height: 100,
  width: 100,
  margin: '0 25px',
  color: 'deepskyblue',
  padding: 20
});

export const CreateResource: React.FunctionComponent<CreateResourceProps> = (props: CreateResourceProps) => {
  const [page, setPage] = useState('selectTemplate' as keyof PageTitle);
  const [selectedTemplate, setTemplate] = useState('');
  const [deployOperation, setDeployOperation] = useState({} as Operation);
  const opsContext = useContext(NotificationsContext);
  const navigate = useNavigate();

  useEffect(() => {
    const clearState = () => {
      setPage('selectTemplate');
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
    selectTemplate: 'Choose a template',
    resourceForm: 'Create a new ' + props.resourceType,
    creating: ''
  }

  const selectTemplate = (templateName: string) => {
    setTemplate(templateName);
    setPage('resourceForm');
  }

  const resourceCreating = (operation: Operation) => {
    setDeployOperation(operation);
    setPage('creating');
    // Add deployment operation to notifications operation poller
    opsContext.addOperation(operation);
  }

  const templatesPath = getTemplatesPath(props.resourceType, props.parentResource);
  const resourcesPath = getResourcesPath(props.resourceType, props.parentResource);

  // Render the current panel sub-page
  let currentPage;
  switch(page) {
    case 'selectTemplate':
      currentPage = <SelectTemplate templatesPath={templatesPath} onSelectTemplate={selectTemplate}/>; break;
    case 'resourceForm':
      currentPage = <ResourceForm 
        templateName={selectedTemplate}
        templatePath={`${templatesPath}/${selectedTemplate}`}
        resourcesPath={resourcesPath}
        onCreateResource={resourceCreating}
      />; break;
    case 'creating':
      currentPage = <div style={{ textAlign: 'center', paddingTop: 100 }}>
        <Icon iconName="CloudAdd" className={creatingIconClass} />
        <h1>Creating {props.resourceType}...</h1>
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

import logo from './logo.svg';
import './App.css';
import {
  provideFASTDesignSystem,
  fastCard,
  fastButton
} from '@microsoft/fast-components';
import { provideReactWrapper } from '@microsoft/fast-react-wrapper';
import React from 'react';


const { wrap } = provideReactWrapper(
  React,
  provideFASTDesignSystem()
);

export const FastCard = wrap(fastCard());
export const FastButton = wrap(fastButton())

function App() {
  return (
    <FastCard>
      <h2>FAST React</h2>
      <FastButton appearance="accent" onClick={() => console.log("clicked")}>Click Me</FastButton>
    </FastCard>
  );
}

export default App;

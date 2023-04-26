import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

// import Car from './car'
import Car from './cars'
// import DropDownDemo from './dropdown'
import DropDownDemo from './drop'

import { SignupPage, SignupPageV2 } from './signup-form';

ReactDOM.render(
  // <Car color='I am a main prop' price='100'>
  //   <h1> I am a child prop </h1>
  // </Car>,
  // <Car></Car>,
  // <DropDownDemo bxCl='transparent'></DropDownDemo>,
  // <SignupPage></SignupPage>,
  <SignupPageV2></SignupPageV2>,
  document.getElementById('root')
);

import React from 'react';
import ReactDOM from 'react-dom';

import { render } from "react-dom";
import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from "react-router-dom";


import { UserRegistration } from './user/registration'
import { UserLogin } from './user/login'
import { Dashboard } from './dashboard/dashboard';
import { Accounts } from './account/accounts';
import { AppMenu } from './dashboard/menus';
import { NotActivated } from './account/not-activated';
import { Depsoits } from './deposit/depsoits';
import { Sub } from './deposit/submit';
import { Withdraw } from './withdraw/withdraw';
import { Transfer } from './transfer/transfer'; 
import { Create } from './creat_account/create._account';
import { Status } from './status/status';
import { Balance } from './balance/balance';

import 'bootstrap/dist/css/bootstrap.min.css';

const router = (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<UserLogin />}></Route>
      <Route path="reg" element={<UserRegistration />}></Route>
      <Route path="dash" element={<Dashboard />}>
        <Route path="" element={<AppMenu />} />
        <Route path="accounts" element={<Accounts />} />
        <Route path="notactivated" element={<NotActivated />} />
        <Route path="deposits" element={<Depsoits/>}/>
        <Route path="submits" element={<Sub/>}/>
        <Route path="withdraw" element={<Withdraw/>}/>
        <Route path="transfer" element={<Transfer/>}/>
        <Route path="account" element={<Create/>}/>
        <Route path="status" element={<Status/>}/>
        <Route path="balance" element={<Balance/>}/>
        
      </Route>
    </Routes>
  </BrowserRouter>
)

ReactDOM.render(
  router,
  document.getElementById('root')
);
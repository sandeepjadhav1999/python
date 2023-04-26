import React from 'react';
import ReactDOM from 'react-dom';

import { LoginPage } from './login/login';
import { DashboardPage } from './dashboard/dashboard'
import { CrmUser } from './users/users';
import { Customer } from './customer/customer';
import { Registration } from './customer/registration';
import { Sub } from './customer/submits';
import { Update } from './customer/update';
import { Subs } from './customer/subm';
import { Block } from './customer/block';
import { List } from './customer/lists';
import { Kitchen } from './kitchen/kitchen';
import { Add } from './kitchen/add';
import { Delete } from './kitchen/delete';
import { Show } from './kitchen/show';
import { AddMessage } from './kitchen/submit';
import { DeleteMsg } from './kitchen/submites';
import { Menu } from './menu/menu';
import { Order } from './order/order';
import { Promotion } from './promotion/promotion';
import { PromotionAdd } from './promotion/add';
import { PromotionList } from './promotion/show';
import { Congo } from './promotion/submit';


import { BrowserRouter, Routes, Route } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';


const routes = (
  <BrowserRouter>
    <Routes>
      <Route path='/' element={<LoginPage />}></Route>
      <Route path='/dash' element={<DashboardPage />}>
        <Route path='users' element={<CrmUser />} />
        <Route path='customer' element={<Customer />} />
        <Route path='reg' element={<Registration />} />
        <Route path='submits' element={<Sub />} />
        <Route path='update' element={<Update />} />
        <Route path='submit' element={<Subs />} />
        <Route path='block' element={<Block />} />
        <Route path='list' element={<List />} />
        <Route path='kitchen' element={<Kitchen />} />
        <Route path='add' element={<Add />} />
        <Route path='delete' element={<Delete />} />
        <Route path='kitche' element={<Show />} />
        <Route path='kitsuccess' element={<AddMessage />} />
        <Route path='kitdelete' element={<DeleteMsg />} />
        <Route path='menu' element={<Menu />} />
        <Route path='order' element={<Order />} />
        <Route path='promotion' element={<Promotion />} />
        <Route path='insert' element={<PromotionAdd />} />
        <Route path='promotions' element={<PromotionList />} />
        <Route path='congo' element={<Congo />} />

        

        
      </Route>
    </Routes>
  </BrowserRouter>
)


ReactDOM.render(
  routes,
  document.getElementById('root')
);
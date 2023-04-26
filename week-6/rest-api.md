# APIs REQUIRED FOR CMR SYSTEM

## Admin Resource
- Activate User                                     ->PUT
- Deactivate User                                   ->PuT

## customer Resource
- create the new customer                           -> POST
- block customer                                    -> PUT
- update customer -> PUT
- show order histroy from customer ID               -> GET
- check mobile is available in databse or not       -> GET
- list  customers by location                       -> GET
- list coustomer bt Age                             -> GET

## order Resource
- create new order                                  ->POST
- update order                                      ->PUT
- cancel order                                      ->PUT
- List orders for perticular Kitchen                ->GET


## Menu Resource
- create new menu item                              -> POST
- update menu item                                  ->PUT
- delelte menu item                                 ->DELETE
- list menu from name                               ->GET

## Promotion Resoruce
- create new promotion                              ->POST
- update promotion                                  ->PUT
- delete promotion                                  ->DELETE
- lsit all promotion                                ->GET
- send promotion to selected customer               ->POST
- send promotion to all customer                    ->PUT
- send age wise promotion                           ->PUT
- send age location promotion                       ->PUT
- send promotion to top 10 customer                 ->PUT
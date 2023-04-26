import react from 'react'
import {apiListCrmMenu} from './menuapi'
import {useEffect,useState,useCallback} from 'react'
import {useNavigate} from 'react-router'
import Button from 'react-bootstrap/Button'

export function Menu() {

    const naviagte=useNavigate()
    const [formdata,setFormData]=useState({customer_id_mobile:''})
    const [items,setItems]=useState([])
    const [total,setTotal]=useState(0)
    const [qty,setQty]=useState(0)
    const [itemslist,setItemsList]=useState([])
    const [isCartSuccess,setCartSuccess]=useState(false)
    const [couponcode,setCouponCode]=useState('')

    const onChangeCouponCode=(e)=>{setCouponCode(e.target.value)}


    const OnCustomerChange=ev=>setFormData({...formdata,customer_id_mobile:ev.target.value})

    useEffect(()=>{
        apiListCrmMenu().then(json=>{
            const its=json['res']

            setItems(its)
        })
    },[])
    

    const incrementCount=e=>{
        setTotal(prevState=>prevState+e.price)
        setQty(prevState=>prevState+e.quantity)
        e.count=e.count+1
        setItemsList(prevState=>[...prevState,e.item_name])
    }

    const decrementCount=e=>{
        if (total == 0 && qty==0) return 0
        const index=itemslist.indexOf(e.item_name);
        if (index >-1){
            itemslist.splice(index,1)
        }
        return [setTotal(prevState=>prevState-e.price),
                setQty(prevState=>prevState-e.quantity),e.count=e.count-1
                ];
    }


    function back() {
        window.location.href='/dash';
        
    }

    const onSubmit=()=>{
        console.log(itemslist)

        makeorderpostrequest()
        naviagte('/dash')
    }

        const makeorderpostrequest= useCallback(()=> {
            console.log(couponcode)
            if (couponcode == '24SAS') {
                var newtotal=total*0.75
             }
             else if (couponcode =='24AAA'){
                 var newtotal=total*0.50
             }
             else if (couponcode =='24DDD'){
                 var newtotal=total*0.70
             }
             else {
                 var newtotal=total
             }
            console.log(couponcode)
            const itemsdetails={
                customer_id_mobile:formdata['customer_id_mobile'],
                total_quantities:qty,
                total_price:newtotal
               }
                console.log(JSON.stringify(itemsdetails))
                setCartSuccess(false)
                fetch('http://localhost:5000/menu',{method:'POST',
                body:JSON.stringify(itemsdetails),
                headers:{'Accept':'application/json','Content-Type':'application/json'}})
                    .then(res=>{
                        if(!res.ok){
                            naviagte('/dash/kitdelete')
                        }
                    })
                    .then(dt=>{
                        setCartSuccess(true)
                        console.log(dt)
                    })
                    .catch(err=>{
                        setCartSuccess(false)
                        console.log(err)
                    })
            },[isCartSuccess,qty,total,formdata,couponcode])


            const trItems = items.map((ac, index) => {
                return (
                    <tr key={index}>
                        <td >{index + 1}</td>
                        {/* <td>{ac.order_id}</td> */}
                        <td>{ac.item_name}</td>
                        <td>{ac.price}</td>
                        <td>
                            <button onClick={()=> decrementCount(ac)}>-</button>
                            {ac.count}
                            <button onClick={()=> incrementCount(ac)}>+</button>
                        </td>
                       
                        
                    </tr>
                )
            })


    return (
        <>
        <div className='container border border-primary py-3 body'>
            <div className='row'>
                <div className='column'>
                    <h3 className='text-muted'>Menu</h3>
                </div>
                <div className='mb-3'>
                    <label htmlFor="exampleInputEmail1" className="form-label"><strong>Enter Customer ID</strong></label>
                    <input
                        onChange={OnCustomerChange}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formdata && !formdata.customer_id_mobile && <div className="form-text text-danger">Invalid ID</div>
                    }
                </div>
            </div>
            

            <div className="row">
                <div className='col'>
                    <table className="table table-dark table-hover">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                               
                                <th scope="col">Dish Name</th>
                           
                                <th scope="col">price</th>

                                <th scope="col">Add to Cart</th>

                          
                            </tr>
                        </thead>
                        <tbody>
                            {trItems}
                        </tbody>
                    </table>


                </div>
                
                <div>
                <div className='col-md-6'>
                    <label htmlFor="exampleInputEmail1" className="form-label"><strong>Enter couponcode</strong></label>
                    <input type="text" style={{width:"100px"}} className="form-control" id="inputEmail4" onChange={onChangeCouponCode}></input>
                </div>
                    {<td>
                <strong>Total Items:{qty}</strong>
            </td>}<div></div>
            <td>
                <strong>Total Price:{total}</strong>
            </td>

            <div style={{display:"flex"}}>

      </div>

            <Button variant='primary' onClick={()=>onSubmit()}>Submit</Button>
            </div>
             <Button variant='dark' style={{marginRight:"auto"}} onClick={back}> Back</Button>
                
                
            </div>
            </div>
        
        </>
    )



}
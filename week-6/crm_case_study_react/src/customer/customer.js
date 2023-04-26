import React from "react";
import {useNavigate} from 'react-router-dom'
import { Button } from "react-bootstrap";
import './customer.css'



export function Customer() {
    const navigate=useNavigate()

    return (
        <div className="Container d-flex justify-content-center">
            <div className="reg"> 
                <Button type="submit" className="btn btn-success" size="lg" onClick={()=>navigate('/dash/reg')} >Registration</Button></div>
            <div className=" upd">
                <Button type="submit" className="btn btn-danger"  size="lg" onClick={()=>navigate('/dash/update')} >update</Button>   
            </div>
            <div className="blo">
                <Button type="submit" className="btn btn-warning"  size="lg" onClick={()=>navigate('/dash/block')} >Block</Button>      
            </div>
            <div className="lis">
                <Button type="submit" className="btn btn-primary"  size="lg" onClick={()=>navigate('/dash/list')} >Customer</Button>      
            </div>

        </div>
    )    
    
}
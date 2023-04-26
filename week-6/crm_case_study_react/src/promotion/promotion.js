import React from "react";
import {useNavigate} from 'react-router-dom'
import { Button } from "react-bootstrap";
import './promotion.css'



export function Promotion() {
    const navigate=useNavigate()

    return (
        <div className="Container d-flex justify-content-center">
            <div className="reg"> 
                <Button type="submit" className="btn btn-success" size="lg" onClick={()=>navigate('/dash/insert')} >ADD</Button></div>
            
            <div className="lis">
                <Button type="submit" className="btn btn-primary"  size="lg" onClick={()=>navigate('/dash/promotions')} >Promotion</Button>      
            </div>

        </div>
    )    
    
}
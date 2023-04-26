import React from "react";
import {useNavigate} from 'react-router-dom'
import { Button } from "react-bootstrap";
import './kitchen.css'

export function Kitchen() {
    const navigate=useNavigate()

    return (
        <div className="Container d-flex justify-content-center">
            <div className="reg"> 
                <Button type="submit" variant="success" size="lg" onClick={()=>navigate('/dash/add')} >Add</Button>
            </div>
            <div className="delete">
                <Button type="submit" variant="danger" size="lg" onClick={()=>navigate('/dash/delete')} >Delete</Button>   
            </div>
            <div className="kitchen">
                <Button type="submit" variant="primary" size="lg" onClick={()=>navigate('/dash/kitche')} >Kitchen</Button>      
            </div>

        </div>
    )    
    
}
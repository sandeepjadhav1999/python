import React from "react";
import {useNavigate} from 'react-router-dom'
import { Alert } from "react-bootstrap";


export function Congo() {
    const navigate=useNavigate()

    return (
        <div>
            <Alert variant="success">
                <Alert.Heading>Hurray 💥🥳🤑🤩💥</Alert.Heading>
                <p>
                    Promotion Has Been Successfully Added
                </p>
                <hr />
                <p className="mb-0">
                   Please Do Visit Again
                </p>
            </Alert>
            <div>
                <button type="submit" className="btn btn-primary" onClick={()=>navigate('/dash')} >Return</button>   
            </div>

        </div>
    )
    
}
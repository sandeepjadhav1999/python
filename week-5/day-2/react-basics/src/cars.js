import { Button,Alert } from "react-bootstrap";
import React from "react";
import {useState} from 'react';

function Car() {
    const [showError,setShowError] = useState(false);
    const setShow=()=>setShowError(false);
    const onBtClk=()=>setShowError(true);

    return (
        <div>
            {showError && (
                <Alert
                    className="m-3"
                    variant="danger"
                    onClose={()=>setShow(false)}
                    dismissible
                >
                    <Alert.Heading>oh snap</Alert.Heading>
                    <p>
                        change this and that ddfbdhtstdngbrshsgvfbfb
                    </p>
                </Alert>
            )}
            <Button variant="primary" onClick={onBtClk}>primary</Button>
        </div>
    )
}

export default Car
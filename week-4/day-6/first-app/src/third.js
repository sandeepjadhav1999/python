
import { useState } from 'react' // react hook

// state management 

export default function Third() {

    const [msg, setMsg] = useState('hello welcome to react')

    const onBtClks = () => {
        // msg = 'great react'
        setMsg('great react')
        console.log(msg)
    }

    return (
        <div>
            <div>
                <h1>{msg}</h1>
            </div>
            <div>
                <input type='button' value='Okay' onClick={onBtClks} />
            </div>
        </div>
    );
}
import React from 'react';
import { useState, useEffect, useCallback } from 'react';
import {useNavigate} from 'react-router-dom'

export function Show() {

    const [accounts, setAccounts] = useState([])

    useEffect(() => {
        fetch('http://localhost:5000/kitchen/display')
            .then(res => res.json())
            .then(data => {
                setAccounts(data.res)
            })
            .catch(err => console.log(err))
    }, []) // it will call at the time of loading component only 

    const rows = accounts.map((ac, index) => {
        return (
            <tr key={index}>
                <td >{index + 1}</td>
                {/* <td>{ac.kitchen_id}</td> */}
                <td>{ac.name}</td>
                <td>{ac.price}</td>
                <td>{ac.location}</td>

            </tr>
        )
    })
    const navigate=useNavigate()

    return (
        <div className="container">
            <div className="row">
                <div className="col">
                    <h3> Kitchen LIST </h3>
                </div>
            </div>

            <div className="row">
                <div className="col">
                    <table className="table table-dark table-hover">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                {/* <th scope="col">ID</th> */}
                                <th scope="col">Name</th>
                               
                                <th scope="col">Price</th>
                                <th scope="col">Location</th>
                              
                            </tr>
                        </thead>
                        <tbody>
                            {rows}
                        </tbody>
                    </table>
                </div>
            </div>
            <div>
                <button type="submit" className="btn btn-primary" onClick={()=>navigate('/dash')} >Return</button>
            </div>
        </div>
    )
}
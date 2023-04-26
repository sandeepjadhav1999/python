import React from 'react';
import { useState, useEffect, useCallback } from 'react';
import {useNavigate} from 'react-router-dom'

export function List() {

    const [accounts, setAccounts] = useState([])

    useEffect(() => {
        fetch('http://localhost:5000/customer/display')
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
                <td>{ac.mobile}</td>
                <td>{ac.name}</td>
                <td>{ac.email}</td>
                <td>{ac.dob}</td>
                <td>{ac.location}</td>
                <td>{ac.status ==1 ? '✅' : '❌'}</td>
                <td>{ac.coupon_code}</td>
            </tr>
        )
    })
    const navigate=useNavigate()

    return (
        <div className="container">
            <div className="row">
                <div className="col">
                    <h3> Customer LIST </h3>
                </div>
            </div>

            <div className="row">
                <div className="col">
                    <table className="table table-dark table-hover">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Mobile</th>
                                <th scope="col">Name</th>
                                <th scope="col">Email</th>
                                <th scope="col">DOB</th>
                                <th scope="col">Location</th>
                                <th scope="col">Status</th>
                                <th scope="col">Coupon Code</th>
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
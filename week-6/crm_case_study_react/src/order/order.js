import React from 'react';
import { useState, useEffect, useCallback } from 'react';
import {useNavigate} from 'react-router-dom'

export function Order() {

    const [accounts, setAccounts] = useState([])

    useEffect(() => {
        fetch('http://localhost:5000/order')
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
                {/* <td>{ac.order_id}</td> */}
                <td>{ac.customer_id_mobile}</td>
                <td>{ac.ordered_date}</td>
                <td>{ac.total_quantities}</td>
                <td>{ac.total_price}</td>
               
                
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
                                {/* <th scope="col">ID</th> */}
                                <th scope="col">Customer Mobile</th>
                                <th scope="col">Place Time</th>
                                <th scope="col">Qunatity</th>
                                <th scope="col">Price</th>
                                

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
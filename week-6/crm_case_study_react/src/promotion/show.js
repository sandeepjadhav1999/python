import React from 'react';
import { useState, useEffect, useCallback } from 'react';
import {useNavigate} from 'react-router-dom'

export function PromotionList() {

    const [accounts, setAccounts] = useState([])

    useEffect(() => {
        fetch('http://localhost:5000/promotion')
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
                <td>{ac.promotion_id}</td>
                <td>{ac.title}</td>
                <td>{ac.text}</td>
                <td>{ac.st_dt}</td>
                <td>{ac.end_dt}</td>
                
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
                                <th scope="col">promotion_id</th>
                                <th scope="col">Title</th>
                                <th scope="col">Description</th>
                                <th scope="col">Start Date</th>
                                <th scope="col">End Date</th>
                               
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
import react from 'react'
import { useState, useCallback } from 'react'
import { useNavigate } from 'react-router';

export function Add() {

    const [formData, setFormData] = useState({name:'',location:''})
    const [isRegisterSuccess, setRegisterSuccess] = useState(false)
    const onNameChanged = ev => setFormData({ ...formData, name:ev.target.value }) 
    const onPriceChanged = ev => setFormData({ ...formData, price:parseInt(ev.target.value) }) 
    const onLocationChanged = ev => setFormData({ ...formData, location:ev.target.value })
   
    const navigate=useNavigate()
    
    const onFormSubmit = e => {
        e.preventDefault()
        console.log('form submitted')
        console.log(formData)
        
        
        makePostRequest()
    }

    const makePostRequest = useCallback(() => {
        console.log(JSON.stringify(formData))
        setRegisterSuccess(false)
        fetch('http://localhost:5000/kitchen',{method:'POST',body:JSON.stringify(formData),headers:{'Accept':'application/json','Content-Type':'application/json'}})
            .then(dt => {
                setRegisterSuccess(true)
                console.log(dt)
                if(dt['status']==201){
                    navigate('/dash/kitsuccess')
                }
                
            })
            .catch(err => {
                setRegisterSuccess(false)
                console.log(err)
            })
            
    }, [isRegisterSuccess,formData])

    
    return (
        <div className="container d-flex justify-content-center align-items-center">
            <form onSubmit={onFormSubmit}>
                
                <div className="mb-3">
                    <h2 className="text-muted"> ADD </h2>
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Name</label>
                    <input
                        onChange={onNameChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.name && <div className="form-text text-danger">Invalid Name</div>
                    }
                </div>


                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Price</label>
                    <input
                        onChange={onPriceChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.price && <div className="form-text text-danger">Invalid Price</div>
                    }
                </div>

                
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Location</label>
                    <input
                        onChange={onLocationChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.location && <div className="form-text text-danger">Invalid Location</div>
                    }
                </div>
                <button type="submit" className="btn btn-primary">Submit</button>     
            </form>
        </div>
    )
}

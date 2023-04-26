import react from 'react'
import { useState, useCallback } from 'react'
import { useNavigate } from 'react-router';

export function Update() {

    const [formData, setFormData] = useState({name:'',email:'',dob:'',location:'',status:'',mobile:''})
    const [isRegisterSuccess, setRegisterSuccess] = useState(false)
    const onNameChanged = ev => setFormData({ ...formData, name:ev.target.value })
    const onEmailChanged = ev => setFormData({ ...formData, email:ev.target.value })
    const onDobChanged = ev => setFormData({ ...formData, dob:ev.target.value})
    const onLocationChanged = ev => setFormData({ ...formData, location:ev.target.value })
    const onStatusChanged = ev => setFormData({ ...formData, status: parseInt(ev.target.value) })
    const onMobileChanged = ev => setFormData({...formData,mobile:ev.target.value})

    const navigate=useNavigate()
    const validateEmail = (email) => {
        return String(email)
            .toLowerCase()
            .match(
                /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            )
    };
    
    const onFormSubmit = e => {
        e.preventDefault()
        console.log('form submitted')
        console.log(formData)
        
        
        makePostRequest()
    }

    const makePostRequest = useCallback(() => {
        console.log(JSON.stringify(formData))
        setRegisterSuccess(false)
        fetch('http://localhost:5000/customer/update',{method:'PUT',body:JSON.stringify(formData),headers:{'Accept':'application/json','Content-Type':'application/json'}})
            .then(dt => {
                setRegisterSuccess(true)
                console.log(dt)
                if(dt['status']==201){
                    navigate('/dash/submit')
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
                    <h2 className="text-muted"> Registration </h2>
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Mobile</label>
                    <input
                        onChange={onMobileChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.mobile && <div className="form-text text-danger">Invalid Mobile Number</div>
                    }
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
                    <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                    <input
                        onChange={onEmailChanged}
                        type="email"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {formData && !formData.email && <div className="form-text text-danger">Email Is Required</div>}
                    {formData && (formData.email && !validateEmail(formData.email)) && <div className="form-text text-danger">Invalid Email</div>}
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >DOB</label>
                    <input
                        onChange={onDobChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.dob && <div className="form-text text-danger">Invalid DOB</div>
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
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Status</label>
                    <input
                        onChange={onStatusChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.status && <div className="form-text text-danger">Invalid Status</div>
                    }
                </div>
                
                

                <button type="submit" className="btn btn-primary">Submit</button>     
            </form>
        </div>
    )
}
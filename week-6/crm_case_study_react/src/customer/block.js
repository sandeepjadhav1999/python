import react from 'react'
import { useState, useCallback } from 'react'
import { useNavigate } from 'react-router';

export function Block() {

    const [formData, setFormData] = useState({admin_id:'',user_id:'',status:''})
    const [isRegisterSuccess, setRegisterSuccess] = useState(false)
    const onMobileChanged = ev => setFormData({...formData,admin_id:ev.target.value})
    const onNameChanged = ev => setFormData({ ...formData, user_id:ev.target.value })
    const onStatusChanged = ev => setFormData({ ...formData, status: parseInt(ev.target.value) })

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
        fetch('http://localhost:5000/customer/block',{method:'PUT',body:JSON.stringify(formData),headers:{'Accept':'application/json','Content-Type':'application/json'}})
            .then(dt => {
                setRegisterSuccess(true)
                console.log(dt)
                if(dt['status']==200){
                    navigate('/dash/submits')
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
                    <h2 className="text-muted"> Block </h2>
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Admin Mobile</label>
                    <input
                        onChange={onMobileChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.admin_id && <div className="form-text text-danger">Invalid Mobile Number</div>
                    }
                </div>

                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >User Name</label>
                    <input
                        onChange={onNameChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.user_id && <div className="form-text text-danger">Invalid Mobile Number</div>
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
import react from 'react'
import { useState, useCallback } from 'react'
import { useNavigate } from 'react-router';

export function PromotionAdd() {

    const [formData, setFormData] = useState({promotion_id:'',title:'',text:'',st_dt:'',end_dt:''})
    const [isRegisterSuccess, setRegisterSuccess] = useState(false)
    const onMobileChanged = ev => setFormData({...formData,promotion_id:ev.target.value})
    const onNameChanged = ev => setFormData({ ...formData, title:ev.target.value })
    const onEmailChanged = ev => setFormData({ ...formData, text:ev.target.value })
    const onDobChanged = ev => setFormData({ ...formData, st_dt:ev.target.value})
    const onLocationChanged = ev => setFormData({ ...formData, end_dt:ev.target.value })
    
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
        fetch('http://localhost:5000/promotion',{method:'POST',body:JSON.stringify(formData),headers:{'Accept':'application/json','Content-Type':'application/json'}})
            .then(dt => {
                setRegisterSuccess(true)
                console.log(dt)
                if(dt['status']==201){
                    navigate('/dash/congo')
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
                    <h2 className="text-muted"> Promotion </h2>
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Promotion ID</label>
                    <input
                        onChange={onMobileChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.promotion_id && <div className="form-text text-danger">Invalid ID</div>
                    }
                </div>

                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Title</label>
                    <input
                        onChange={onNameChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.title && <div className="form-text text-danger">Invalid Title</div>
                    }
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label">Description </label>
                    <input
                        onChange={onEmailChanged}
                        type="email"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {formData && !formData.text && <div className="form-text text-danger">Invalid Description</div>}
                   
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Start Date</label>
                    <input
                        onChange={onDobChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.st_dt && <div className="form-text text-danger">Invalid Date</div>
                    }
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >End Date</label>
                    <input
                        onChange={onLocationChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.end_dt && <div className="form-text text-danger">Invalid Date</div>
                    }
                </div>

                <button type="submit" className="btn btn-primary">Submit</button>     
            </form>
        </div>
    )
}
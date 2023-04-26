import react from 'react'
import './depsoit.css'
import { useState, useCallback } from 'react'
import { useNavigate } from 'react-router';
import banner from '../images/reg-banner.jpg'

export function Depsoits() {

    const [formData, setFormData] = useState({acc_num_deposit:'',amt:''})
    const [isRegisterSuccess, setRegisterSuccess] = useState(false)
    const onAccChanged = ev => setFormData({...formData,acc_num_deposit:parseInt(ev.target.value)})
    const onAmtChanged = ev => setFormData({ ...formData, amt: parseInt(ev.target.value) })

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
        fetch('http://localhost:5000/depo',{method:'POST',body:JSON.stringify(formData),headers:{'Accept':'application/json','Content-Type':'application/json'}})
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
        <div className="container d-flex flex-row-reverse align-items-center">
            <form onSubmit={onFormSubmit}>
                
                <div className="mb-3">
                    <h2 className="text-muted"> Deposite </h2>
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Account Number</label>
                    <input
                        onChange={onAccChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.acc_num_deposit && <div className="form-text text-danger">Invalid Account Number</div>
                    }
                </div>

                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Amount</label>
                    <input
                        onChange={onAmtChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.amt && <div className="form-text text-danger">Invalid Amount</div>
                    }
                </div>
                <button type="submit" className="btn btn-primary">Submit</button>     
            </form>
            
            
           
            <div>
                <img src={banner}></img>
            </div>
        </div>
    )
}
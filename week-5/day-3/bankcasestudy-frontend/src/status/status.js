import react from 'react'
import './depsoit.css'
import { useState, useCallback } from 'react'
// import { useNavigate } from 'react-router';
import banner from '../images/reg-banner.jpg'
import {useNavigate} from 'react-router-dom'

export function Status() {
    const [formData, setFormData] = useState({ac_sts:'',ac_num:''})
    const [isRegisterSuccess, setRegisterSuccess] = useState(false)
    const onAccChanged = ev => setFormData({...formData,ac_sts:parseInt(ev.target.value)})
    const onAmtChanged = ev => setFormData({ ...formData,ac_num: parseInt(ev.target.value) })

    const navigate=useNavigate()
    
    const onFormSubmit = e => {
        e.preventDefault()
        console.log('form submitted')
        console.log(formData)
        
        setsubmit(true)
        makePostRequest()
    }

    const makePostRequest = useCallback(() => {
        console.log(JSON.stringify(formData))
        setRegisterSuccess(false)
        fetch('http://localhost:5000/activate',{method:'POST',body:JSON.stringify(formData),headers:{'Accept':'application/json','Content-Type':'application/json'}})
            .then(dt => {
                setRegisterSuccess(true)
                console.log(dt)
            })
            .catch(err => {
                setRegisterSuccess(false)
                console.log(err)
            })
            
    }, [isRegisterSuccess,formData])

    const [submitted,setsubmit]=useState(false)
    return (
        <div className="container d-flex flex-row-reverse align-items-center">
            <form onSubmit={onFormSubmit}>
                {submitted ? <div className="p-3 mb-2 bg-success text-black" >Thanks Your Account has been Activated 💥🥳🤑🤩💥 </div> : null}
               
                <div className="mb-3">
                    <h2 className="text-muted"> Status </h2>
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Acitvate</label>
                    <input
                        onChange={onAccChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.ac_sts && <div className="form-text text-danger">Invalid Account Number</div>
                    }
                </div>

                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Account Number</label>
                    <input
                        onChange={onAmtChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.ac_num && <div className="form-text text-danger">Invalid Amount</div>
                    }
                </div>
                <button type="submit" className="btn btn-primary">Submit</button>     
            </form>
            <div className='box'>
                <button type="submit" className="btn btn-primary" onClick={()=>{navigate('/dash')}}>Back</button>
            </div>
            
           
            <div>
                <img src={banner}></img>
            </div>
        </div>
    )
}
import react from 'react'
import './depsoit.css'
import { useState, useCallback } from 'react'
// import { useNavigate } from 'react-router';
import banner from '../images/reg-banner.jpg'
import {useNavigate} from 'react-router-dom'
export function Transfer() {

    const [formData, setFormData] = useState({src_acc:'',tar_acc:'',amt:''})
    const [isRegisterSuccess, setRegisterSuccess] = useState(false)
    const onSrcccChanged = ev => setFormData({...formData,src_acc:parseInt(ev.target.value)})
    const onTarChanged = ev => setFormData({...formData,tar_acc:parseInt(ev.target.value)})
    const onAmtChanged = ev => setFormData({ ...formData, amt: parseInt(ev.target.value) })

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
        fetch('http://localhost:5000/trans',{method:'POST',body:JSON.stringify(formData),headers:{'Accept':'application/json','Content-Type':'application/json'}})
            .then(dt => {
                setRegisterSuccess(true)
                console.log(dt)
            
            })
            .catch(err => {
                setRegisterSuccess(false)
                console.log(err)
            })
            
    }, [isRegisterSuccess,formData,navigate])

    const [submitted,setsubmit]=useState(false)
    return (
        <div className="container d-flex flex-row-reverse align-items-center">
            <form onSubmit={onFormSubmit}>
                {submitted ? <div className="p-3 mb-2 bg-success text-black" >Thanks Your Amount is Transferred 💥🥳🤑🤩💥 </div> : null}
               
                <div className="mb-3">
                    <h2 className="text-muted"> Transfer </h2>
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Source Account Number</label>
                    <input
                        onChange={onSrcccChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.src_acc && <div className="form-text text-danger">Invalid Account Number</div>
                    }
                </div>


                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >Traget Account Number</label>
                    <input
                        onChange={onTarChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.tar_acc && <div className="form-text text-danger">Invalid Account Number</div>
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
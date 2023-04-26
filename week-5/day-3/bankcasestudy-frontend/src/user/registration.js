import react from 'react'
import './registration.css'
import { useState, useCallback } from 'react'
// import axios from 'axios'
// import {useNavigate} from 'react-router-dom'
import banner from '../images/reg-banner.jpg'

export function UserRegistration() {

    const [formData, setFormData] = useState({user_id:'',user_name:'',password:'',role:''})
    const [isRegisterSuccess, setRegisterSuccess] = useState(false)
    const onUserIdChanged = ev => setFormData({...formData,user_id:ev.target.value})
    const onUserNameChanged = ev => setFormData({ ...formData, user_name: ev.target.value })
    // const onEmailChanged = ev => setFormData({ ...formData, email: ev.target.value })
    const onPasswordChanged = ev => setFormData({ ...formData, password: ev.target.value })
    const onRoleChanged =ev => setFormData({...formData,role:ev.target.value})


    const onFormSubmit = e => {
        e.preventDefault()
        console.log('form submitted')
        console.log(formData)

        makePostRequest()
    }


    // let history=useNavigate()
    // const validateEmail = (email) => {
    //     return String(email)
    //         .toLowerCase()
    //         .match(
    //             /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    //         )
    // };

    const makePostRequest = useCallback(() => {
        console.log(JSON.stringify(formData))
        setRegisterSuccess(false)
        fetch('http://localhost:5000/user',{method:'POST',body:JSON.stringify(formData),headers:{'Accept':'application/json','Content-Type':'application/json'}})
            .then(dt => {
                setRegisterSuccess(true)
                console.log(dt)
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
                    <h2 className="text-muted"> User Registration </h2>
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >User ID</label>
                    <input
                        onChange={onUserIdChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.user_id && <div className="form-text text-danger">Invalid userID</div>
                    }
                </div>

                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >User Name</label>
                    <input
                        onChange={onUserNameChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.user_name && <div className="form-text text-danger">Invalid username</div>
                    }
                </div>
                {/* <div className="mb-3">
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
                </div> */}
                <div className="mb-3">
                    <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                    <input
                        onChange={onPasswordChanged}
                        type="password"
                        className="form-control"
                        required
                    />
                    {formData && !formData.password && <div className="form-text text-danger">Password required</div>}
                </div>

                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >User ID</label>
                    <input
                        onChange={onRoleChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.role && <div className="form-text text-danger">Invalid Role</div>
                    }
                </div>


                <button type="submit" className="btn btn-primary" >Regsiter</button>
            </form>

            <div>
                <img src={banner}></img>
            </div>
        </div>
    )
}
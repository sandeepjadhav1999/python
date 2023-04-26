import './second.css'

export default function Second() {
    // function onclickokay(){
    //     console.log(`hello`)
    // }

    // const btn=()=>{
    //     console.log(`hello sep`)
    // }

    // in react once loaded v cnt change the msg or anything react is immutable
    let msg='welcome'

    const onclk= ()=> {
        msg='bye'
        console.log(msg)
    }


    //to overcme the immutable property checl third.js
    

    // return (
    //     <div>

    //         <h1>{msg}</h1>
    //         <div className="box"></div>
    //         <div>
    //         {/* <input type='button' value='Okay' onClick={onclickokay} />
    //         <input type='button' value='Okay' onClick={() => console.log('hello arrow')} />
    //         <input type='button' value='Okay' onClick={btn} /> */}
    //         </div>
    //     </div>
    // )

    return (
        <div>
            <div>
                <h1>{msg}</h1>
            </div>
            <div>
                <input type='button' value='okay' onClick={onclk}></input>
            </div>

            
        </div>
    )
}

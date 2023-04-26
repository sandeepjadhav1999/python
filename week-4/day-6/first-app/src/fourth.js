import { useState } from 'react'
import './fourth.css'

function Four() {

    const maxColor = 225
    const [red, setRed] = useState(0)
    const [green, setGreen] = useState(0)
    const [blue, setBlue] = useState(0)

    const onClickRedAdd = () => {
        setRed(red + 5)
    }

    const onClickRedSub = () => {
        setRed(red - 5)
    }

    const onClickGreenAdd = () => {
        setGreen(green + 5)
    }

    const onClickGreenSub = () => {
        setGreen(green - 5)
    }

    const onClickBlueAdd = () => {
        setBlue(blue + 5)
    }

    const onClickBlueSub = () => {
        setBlue(blue - 5)
    }

    const stObj = { backgroundColor: `rgb(${red}, ${green}, ${blue})` }
    return (
        <div className='colCont'>
            <div className='colorPanel' style={stObj}>

            </div>
            <div className='red'>
                <input type='button' value='-' onClick={onClickRedSub} />
                <progress value={red} max={maxColor} ></progress>
                <input type='button' value='+' onClick={onClickRedAdd} />
            </div>
            <div className='green'>
                <input type='button' value='-' onClick={onClickGreenSub} />
                <progress value={green} max={maxColor}></progress>
                <input type='button' value='+' onClick={onClickGreenAdd} />
            </div>
            <div className='blue'>
                <input type='button' value='-' onClick={onClickBlueSub} />
                <progress value={blue} max={maxColor}></progress>
                <input type='button' value='+' onClick={onClickBlueAdd} />
            </div>
        </div>
    )
}

export default Four
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  // const onSubmit = async (e) => {
  const onSubmit = async () => {
    // e.preventDefault()

    // const data = {
    //     firstName,
    //     lastName,
    //     email
    // }
    // const url = "http://127.0.0.1:5000/" + (updating ? `update_contact/${existingContact.id}` : "create_contact")
    const url = "http://127.0.0.1:5000/"
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      // // body: JSON.stringify(data)
      body: JSON.stringify({ "hi": "hello" })
    }
    // console.log(options.mode)
    const response = await fetch(url, options)
    // if (response.status !== 201 && response.status !== 200) {
    //   const data = await response.json()
    //   alert(data.message)
    // } // else {
    //     updateCallback()
    // }
  }

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => {
          setCount((count) => count + 1)
          console.log("hi")
          onSubmit()
        }}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App

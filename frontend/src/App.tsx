import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import SignUpForm from "./SignUpForm";

function App() {
  const [count, setCount] = useState(0)
  const [isModalOpen, setIsModalOpen] = useState(false)

  // const onSubmit = async (e) => {
  const onSubmit = async () => {
    // e.preventDefault()

    // const data = {
    //     firstName,
    //     lastName,
    //     email
    // }
    // const url = "http://127.0.0.1:5000/" + (updating ? `update_contact/${existingContact.id}` : "create_contact")
    const url = "http://127.0.0.1:5000/create_guardian"
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

  const openSignUpModal = () => {
    if (!isModalOpen) setIsModalOpen(true)
  }

  const closeModal = () => {
    setIsModalOpen(false)
    // setCurrentContact({})
  }

  const onUpdate = () => {
    closeModal()
    // fetchContacts()
  }

  return (
    <>
      <button onClick={openSignUpModal}>Sign Up</button>
      {isModalOpen && <div className="modal">
        <div className="modal-content">
          <span className="close" onClick={closeModal}>&times;</span>
          <SignUpForm updateCallback={onUpdate} />
          {/* <SignUpForm existingContact={currentContact} updateCallback={onUpdate} /> */}
        </div>
      </div>
      }
    </>
  )
}

export default App

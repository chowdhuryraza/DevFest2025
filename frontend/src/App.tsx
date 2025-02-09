import { useState } from 'react'
import './App.css'
import SignUpForm from "./SignUpForm";
import Dashboard from "./Dashboard";
import { BrowserRouter as Router, Routes, Route } from "react-router";

function App() {
  const [isModalOpen, setIsModalOpen] = useState(false)

  const openSignUpModal = () => {
    if (!isModalOpen) setIsModalOpen(true)
  }

  const closeModal = () => {
    setIsModalOpen(false)
    // setCurrentContact({})
  }

  const onUpdate = () => {
    closeModal()
  }

  const loginRedirect = () => {
    console.log("hi")
    window.location.href = "/dashboard"
  }

  return (
    <Router>
      <Routes>

        <Route path="/" element={
          <>
            <button onClick={openSignUpModal}>Sign Up</button>
            {isModalOpen && <div className="modal">
              <div className="modal-content">
                <span className="close" onClick={closeModal}>&times;</span>
                <SignUpForm updateCallback={onUpdate} />
              </div>
            </div>
            }
            <button onClick={loginRedirect}>Login</button>
          </>
        } />

        <Route path="/dashboard" element={<Dashboard />} />

      </Routes>
    </Router >
  )
}

export default App
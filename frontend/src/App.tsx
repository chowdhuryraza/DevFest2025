// import { useState } from 'react'
// import './App.css'
// import SignUpForm from "./SignUpForm";
// import Dashboard from "./Dashboard";
// import { BrowserRouter as Router, Routes, Route } from "react-router";

// function App() {
//   const [isModalOpen, setIsModalOpen] = useState(false)

//   const openSignUpModal = () => {
//     if (!isModalOpen) setIsModalOpen(true)
//   }

//   const closeModal = () => {
//     setIsModalOpen(false)
//     // setCurrentContact({})
//   }

//   const onUpdate = () => {
//     closeModal()
//   }

//   const loginRedirect = () => {
//     console.log("hi")
//     window.location.href = "/dashboard"
//   }

//   return (
//     <Router>
//       <Routes>

//         <Route path="/" element={
//           <>
//             <button onClick={openSignUpModal}>Sign Up</button>
//             {isModalOpen && <div className="modal">
//               <div className="modal-content">
//                 <span className="close" onClick={closeModal}>&times;</span>
//                 <SignUpForm updateCallback={onUpdate} />
//               </div>
//             </div>
//             }
//             <button onClick={loginRedirect}>Login</button>
//           </>
//         } />

//         <Route path="/dashboard" element={<Dashboard />} />

//       </Routes>
//     </Router >
//   )
// }

// export default App


// import { useState } from 'react';
// import './App.css';
// import SignUpForm from './SignUpForm';
// import Dashboard from './Dashboard';
// import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// function App() {
//   const [isModalOpen, setIsModalOpen] = useState(false);

//   const openSignUpModal = () => {
//     if (!isModalOpen) setIsModalOpen(true);
//   };

//   const closeModal = () => {
//     setIsModalOpen(false);
//   };

//   const onUpdate = () => {
//     closeModal();
//   };

//   const loginRedirect = () => {
//     console.log('Redirecting to Dashboard...');
//     window.location.href = '/dashboard';
//   };

//   return (
//     <Router>
//       <nav className="flex justify-between items-center bg-black text-white p-4">
//         <h1 className="text-xl font-bold">CareLingo</h1>
//         <div className="flex space-x-2">
//           <button
//             className="bg-white text-black px-4 py-2 rounded hover:bg-gray-200"
//             onClick={openSignUpModal}
//           >
//             Sign Up
//           </button>
//           <button
//             className="bg-white text-black px-4 py-2 rounded hover:bg-gray-200"
//             onClick={loginRedirect}
//           >
//             Login
//           </button>
//         </div>
//       </nav>
//       <Routes>
//         <Route
//           path="/"
//           element={
//             <>
//               <div className="p-6 text-center">
//                 <h2 className="text-2xl font-semibold text-black">About Us</h2>
//                 <p className="mt-2 text-gray-800">
//                   Welcome to our application! We provide the best service to
//                   manage your tasks effectively.
//                 </p>
//               </div>
//               {isModalOpen && (
//                 <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
//                   <div className="bg-white p-6 rounded shadow-md w-80">
//                     <span className="float-right text-gray-500 cursor-pointer" onClick={closeModal}>
//                       &times;
//                     </span>
//                     <SignUpForm updateCallback={onUpdate} />
//                   </div>
//                 </div>
//               )}
//             </>
//           }
//         />
//         <Route path="/dashboard" element={<Dashboard />} />
//       </Routes>
//     </Router>
//   );
// }

// export default App;


import { useState } from 'react';
// import './App.css';
import './output.css';
import SignUpForm from './SignUpForm';
import Dashboard from './Dashboard';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const openSignUpModal = () => {
    if (!isModalOpen) setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  const onUpdate = () => {
    closeModal();
  };

  const loginRedirect = () => {
    console.log('Redirecting to Dashboard...');
    window.location.href = '/dashboard';
  };

  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={
            <>
              <nav className="flex justify-between items-center bg-black text-white p-4">
                <h1 className="text-xl font-bold">CareLingo</h1>
                <div className="flex space-x-2">
                  <button
                    className="bg-white text-white px-4 py-2 rounded hover:bg-gray-200"
                    onClick={openSignUpModal}
                  >
                    Sign Up
                  </button>
                  <button
                    className="bg-white text-white px-4 py-2 rounded hover:bg-gray-200"
                    onClick={loginRedirect}
                  >
                    Login
                  </button>
                </div>
              </nav>
              <div className="relative h-screen bg-cover bg-center" style={{ backgroundImage: "url('https://source.unsplash.com/random/1920x1080')" }}>
                <div className="flex items-center justify-center h-full bg-black bg-opacity-60">
                  <div className="text-white text-center p-6">
                    <h2 className="text-4xl font-semibold">About Us</h2>
                    <p className="mt-4 text-lg">
                      Welcome to CareLingo! We provide the best service to manage your tasks effectively. Join us in life-changing communication.
                    </p>
                  </div>
                </div>
                {isModalOpen && (
                  <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-70">
                    <div className="bg-white p-6 rounded shadow-md w-80">
                      <span className="float-right text-gray-500 cursor-pointer" onClick={closeModal}>
                        &times;
                      </span>
                      <SignUpForm updateCallback={onUpdate} />
                    </div>
                  </div>
                )}
              </div>
            </>
          }
        />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </Router>
  );
}

export default App;

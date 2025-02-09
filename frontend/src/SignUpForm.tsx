// import { useState } from "react";

// const SignUpForm = ({ updateCallback }) => {
//     const [name, setName] = useState();
//     const [email, setEmail] = useState();
//     const [phone, setPhone] = useState();
//     const [password, setPassword] = useState();

//     const onSubmit = async (e) => {
//         e.preventDefault()

//         const data = {
//             name,
//             email,
//             phone,
//             password
//         }

//         const url = "http://127.0.0.1:5000/register"

//         const options = {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify(data)
//         }

//         const response = await fetch(url, options)
//         if (response.status !== 201 && response.status !== 200) {
//             const data = await response.json()
//             alert(data.message)
//         } else {
//             updateCallback()
//         }
//     }

//     return (
//         <form onSubmit={onSubmit}>
//             <div>
//                 <label htmlFor="name">Name: </label>
//                 <input
//                     type="text"
//                     id="name"
//                     // value={name}
//                     onChange={(e) => setName(e.target.value)}
//                 />
//             </div>
//             <div>
//                 <label htmlFor="email">Email: </label>
//                 <input
//                     type="text"
//                     id="email"
//                     // value={email}
//                     onChange={(e) => setEmail(e.target.value)}
//                 />
//             </div>
//             <div>
//                 <label htmlFor="phone">Phone: </label>
//                 <input
//                     type="text"
//                     id="phone"
//                     // value={phone}
//                     onChange={(e) => setPhone(e.target.value)}
//                 />
//             </div>
//             <div>
//                 <label htmlFor="password">Password: </label>
//                 <input
//                     type="password"
//                     id="password"
//                     // value={password}
//                     onChange={(e) => setPassword(e.target.value)}
//                 />
//             </div>
//             <button type="submit">{"Create"}</button>
//         </form>
//     );
// };

// export default SignUpForm

import { useState } from "react";

const SignUpForm = ({ updateCallback }) => {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [phone, setPhone] = useState("");
    const [password, setPassword] = useState("");

    const onSubmit = async (e) => {
        e.preventDefault();

        const data = {
            name,
            email,
            phone,
            password,
        };

        const url = "http://127.0.0.1:5000/register";

        const options = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        };

        const response = await fetch(url, options);
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json();
            alert(data.message);
        } else {
            updateCallback();
        }
    };

    return (
        <form onSubmit={onSubmit} className="bg-white p-6 rounded shadow-md space-y-4">
            <div>
                <label htmlFor="name" className="block text-black">
                    Name:
                </label>
                <input
                    type="text"
                    id="name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="w-full border border-gray-300 p-2 rounded text-black" // Added text-black
                    required
                />
            </div>
            <div>
                <label htmlFor="email" className="block text-black">
                    Email:
                </label>
                <input
                    type="email"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="w-full border border-gray-300 p-2 rounded text-black" // Added text-black
                    required
                />
            </div>
            <div>
                <label htmlFor="phone" className="block text-black">
                    Phone:
                </label>
                <input
                    type="tel"
                    id="phone"
                    value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                    className="w-full border border-gray-300 p-2 rounded text-black" // Added text-black
                    required
                />
            </div>
            <div>
                <label htmlFor="password" className="block text-black">
                    Password:
                </label>
                <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-full border border-gray-300 p-2 rounded text-black" // Added text-black
                    required
                />
            </div>
            <button
                type="submit"
                className="bg-black text-white px-4 py-2 rounded hover:bg-gray-800"
            >
                Create
            </button>
        </form>
    );
};

export default SignUpForm;

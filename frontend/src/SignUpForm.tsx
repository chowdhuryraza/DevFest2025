import { useState } from "react";

// const SignUpForm = ({ existingContact = {}, updateCallback }) => {
const SignUpForm = ({ updateCallback }) => {
    const [name, setName] = useState();
    const [email, setEmail] = useState();
    const [phone, setPhone] = useState();
    const [password, setPassword] = useState();

    // const updating = Object.entries(existingContact).length !== 0

    const onSubmit = async (e) => {
        e.preventDefault()

        const data = {
            name,
            email,
            phone,
            password
        }
        const url = "http://127.0.0.1:5000/guardians/create_guardian"
        const options = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
        const response = await fetch(url, options)
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            updateCallback()
        }
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="name">Name: </label>
                <input
                    type="text"
                    id="name"
                    // value={name}
                    onChange={(e) => setName(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="email">Email: </label>
                <input
                    type="text"
                    id="email"
                    // value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="phone">Phone: </label>
                <input
                    type="text"
                    id="phone"
                    // value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="password">Password: </label>
                <input
                    type="password"
                    id="password"
                    // value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
            </div>
            <button type="submit">{"Create"}</button>
        </form>
    );
};

export default SignUpForm
import { useState } from "react";

const AddPrescription = ({ updateCallback }) => {
    const [name, setName] = useState();
    const [email, setEmail] = useState();
    const [phone, setPhone] = useState();
    const [password, setPassword] = useState();

    const onSubmit = async (e) => {
        e.preventDefault()

        const data = {
            medication,
            dosage,
            day,
            time
        }

        const url = "http://127.0.0.1:5000/prescriptions/create"

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
                <label htmlFor="medication">Medication: </label>
                <input
                    type="text"
                    id="medication"
                    // value={name}
                    onChange={(e) => setName(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="dosage">Dosage: </label>
                <input
                    type="text"
                    id="dosage"
                    // value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="day">Day: </label>
                <input
                    type="text"
                    id="day"
                    // value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="time">Time: </label>
                <input
                    type="text"
                    id="time"
                    // value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="status">Status: </label>
                <input
                    type="text"
                    id="status"
                    // value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
            </div>
            <button type="submit">{"Submit"}</button>
        </form>
    );
};

export default AddPrescription
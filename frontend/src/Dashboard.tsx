import { useState } from 'react'

function Dashboard() {

    // const [prescriptions, setPrescriptions] = useState();
    name = "NAME HERE";

    const onSubmit = async () => {
        const data = { email: "123456", password: "123456" }
        const urlLog = "http://127.0.0.1:5000/login"
        const optionsLog = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
        const responseLog = await fetch(urlLog, optionsLog)
        console.log("login response:")
        console.log(await responseLog.json())
        if (responseLog.status !== 201 && responseLog.status !== 200) {
            const data = await responseLog.json()
            alert(data.message)
        }

        const url = "http://127.0.0.1:5000/prescriptions/all"
        const options = { method: "GET" }
        const response = await fetch(url, options)
        console.log(await response.json());
        console.log("!!")
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } // else {
        //     updateCallback()
        // }
    }

    onSubmit()

    const prescriptions = [
        { id: 1, medication: 'Cabbage', dosage: '11', instructions: "A" },
        { id: 2, medication: 'Garlic', dosage: "12", instructions: "A" },
        { id: 3, medication: 'Apple', dosage: "13", instructions: "A" },
    ];

    return (
        <>
            Welcome, {name}
            <p></p>
            <table>
                <thead>
                    <tr>
                        <th>Medication</th>
                        <th>Dosage</th>
                        <th>Instructions</th>
                    </tr>
                </thead>
                <tbody>

                    {prescriptions.map((prescription) => (
                        <tr key={prescription.id}>
                            <td>{prescription.medication}</td>
                            <td>{prescription.dosage}</td>
                            <td>{prescription.instructions}</td>
                            <td>
                                <button onClick={() => updateContact(contact)}>Update</button>
                                <button onClick={() => onDelete(contact.id)}>Delete</button>
                            </td>
                        </tr>
                    ))}

                </tbody>
            </table>
        </>
    )
}

export default Dashboard
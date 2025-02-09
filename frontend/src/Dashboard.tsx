import { useState } from 'react'

function Dashboard() {

    name = "NAME HERE";

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
import React, { useState } from "react";

function SignUpForm({ onLogin }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [passwordConfirmation, setPasswordConfirmation] = useState("");
    const [firstname, setFirstname] = useState("");
    const [lastname, setLastname] = useState("");
    const [errors, setErrors] = useState([]);
    const [loading, setLoading] = useState(false);

    function handleSubmit(e) {
        e.preventDefault();
        setErrors([]);
        setLoading(true);
        fetch("/signup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                
                username,
                password,
                password_confirmation: passwordConfirmation,
                firstname,
                lastname,
                }),
            }).then((r) => {
                setLoading(false);
                if (r.ok) {
                    r.json().then((user) => onLogin(user));
                } else {
                    r.json().then((err) => setErrors(err.errors));
                }
            });
    }

    
}
import React, { useState } from "react";

function LoginForm({ onLogin }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [errors, setErrors] = useState([]);
    const [loading, setLoading] = useState(false);

    function handleSubmit(e) {
        e.preventDefault();
        setErrors([]);
        setLoading(true);
        fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        }).then((r) => {
            setLoading(false);
            if (r.ok) {
                r.json().then((user) => onLogin(user));
            } 
            else {
                r.json().then((err) => setErrors(err.errors));
            }
        });
    }

    return (
        <form onSubmit={handleSubmit}>
            <h1>Login</h1>
            <div>
                <label htmlFor="username">Username</label>
                <input
                    type="text"
                    id="username"
                    autoComplete="off"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="password">Password</label>
                <input
                    type="password"
                    id="password"
                    autoComplete="current-password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
            </div>
            <div>
                <button type="submit">Login</button>
                {loading ? <p>Loading...</p> : null}
            </div>
            <div>
                {errors && errors.length > 0 && (
                    <div>
                        {errors.map((err, index) => (
                            <div key={index}>
                                {err}
                                
                            </div>
                            
                        ))}
                    </div>
                )}
            </div>
        </form>
    );
}

export default LoginForm
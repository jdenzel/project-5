import React, { useState } from "react";

function SignUpForm({ onLogin }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [passwordConfirmation, setPasswordConfirmation] = useState("");
    const [firstname, setFirstname] = useState("");
    const [lastname, setLastname] = useState("");
    const [player_staff, setPlayer_staff] = useState("");
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
                player_staff,
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

    return (
        <form onSubmit={handleSubmit}>
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
                <label htmlFor="passwordConfirmation">Confirm Password</label>
                <input
                    type="password"
                    id="passwordConfirmation"
                    autoComplete="current-password"
                    value={passwordConfirmation}
                    onChange={(e) => setPasswordConfirmation(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="firstname">First Name</label>
                <input
                    type="text"
                    id="firstname"
                    autoComplete="off"
                    value={firstname}
                    onChange={(e) => setFirstname(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="lastname">Last Name</label>
                <input
                    type="text"
                    id="lastname"
                    autoComplete="off"
                    value={lastname}
                    onChange={(e) => setLastname(e.target.value)}
                />
            </div>
            <div>
                <label>Player or Staff</label>
                <div>
                    <label>
                        <input
                            type="radio"
                            value="player"
                            checked={player_staff === "player"}
                            onChange={(e) => setPlayer_staff(e.target.value)}
                        />
                        Player
                    </label>
                </div>
                <div>
                    <label>
                        <input
                            type="radio"
                            value="staff"
                            checked={player_staff === "staff"}
                            onChange={(e) => setPlayer_staff(e.target.value)}
                        />
                        Staff
                    </label>
                </div>
            </div>
            <div>
                <button type="submit">{loading ? "Loading..." : "Sign Up"}</button>
            </div>
            <div>
                {errors.map((err) => (
                    <div key={err}>{err}</div>
                ))}
            </div>
        </form>
    )
}

export default SignUpForm;
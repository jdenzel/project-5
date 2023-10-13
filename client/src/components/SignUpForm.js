import React, { useState } from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";

function SignUpForm({ onLogin }) {
    const signUpValues = {
        username: "",
        password: "",
        passwordConfirmation: "",
        role: "",
        firstname: "",
        lastname: "",
        image_url: "",
        bio: "",
        jersey_number: "",
    };

    const signUpSchema = Yup.object().shape({
        username: Yup.string().required("Username is required"),
        password: Yup.string().required("Password is required"),
        passwordConfirmation: Yup.string()
            .oneOf([Yup.ref("password"), null], "Passwords must match")
            .required("Password confirmation is required"),
        firstname: Yup.string().required("First name is required"),
        lastname: Yup.string().required("Last name is required"),
        role: Yup.string().required("Role is required"),
        image_url: Yup.string().required("Image is required"),
        bio: Yup.string().required("Bio is required"),
        jersey_number: Yup.string().required("Jersey number is required"),
    });
    // const [username, setUsername] = useState("");
    // const [password, setPassword] = useState("");
    // const [passwordConfirmation, setPasswordConfirmation] = useState("");
    // const [firstname, setFirstname] = useState("");
    // const [lastname, setLastname] = useState("");
    // const [role, setRole] = useState("");
    // const [image_url, setImage_url] = useState("");
    // const [bio, setBio] = useState("");
    // const [jersey_number, setJersey_number] = useState("");
    // const [errors, setErrors] = useState([]);
    // const [loading, setLoading] = useState(false);

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
                role,
                first_name: firstname,
                last_name: lastname,
                image_url: image_url,
                bio,
                jersey_number,
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
                <label htmlFor="bio">Biography</label>
                <input
                    type="text"
                    id="bio"
                    autoComplete="off"
                    value={bio}
                    onChange={(e) => setBio(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="image_url">Image</label>
                <input
                    type="text"
                    id="image_url"
                    autoComplete="off"
                    value={image_url}
                    onChange={(e) => setImage_url(e.target.value)}
                />
            </div>
            <div>
                <label>Player or Admin</label>
                <div>
                    <label>
                        <input
                            type="radio"
                            value="player"
                            checked={role === "player"}
                            onChange={(e) => setRole(e.target.value)}
                        />
                        Player
                    </label>
                </div>
                <div>
                    <label>
                        <input
                            type="radio"
                            value="staff"
                            checked={role === "admin"}
                            onChange={(e) => setRole(e.target.value)}
                        />
                        Admin
                    </label>
                </div>
            </div>
            {role === "player" && (
                <div>
                    <label htmlFor="jersey_number">Jersey Number</label>
                    <input
                        type="text"
                        id="jersey_number"
                        autoComplete="off"
                        value={jersey_number}
                        onChange={(e) => setJersey_number(e.target.value)}
                    />
                </div>    
            )}
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
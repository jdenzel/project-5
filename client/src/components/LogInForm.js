import React, { useState } from "react";
import { useFormik, userFormik } from "formik"
import * as Yup from "yup"

function LoginForm({ onLogin }) {
    const loginSchema = Yup.object().shape({
        username: Yup.string().required("Username is required"),
        password: Yup.string().required("Password is required"),
    });

    const formik = useFormik({
        initialValues: {
            username: "",
            password: "",
        },
        validationSchema: loginSchema,
        onSubmit: (values) => {
            fetch("/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(values),
            }).then((r) => {
                if (r.ok) {
                    r.json().then((user) => onLogin(user));
                }
                else {
                    r.json().then((err) => setErrors(err.errors));
                }
            });
        }
    });

    

    // const [username, setUsername] = useState("");
    // const [password, setPassword] = useState("");
    // const [errors, setErrors] = useState([]);
    // const [loading, setLoading] = useState(false);

    // function handleSubmit(e) {
    //     e.preventDefault();
    //     setErrors([]);
    //     setLoading(true);
    //     fetch("/login", {
    //         method: "POST",
    //         headers: {
    //             "Content-Type": "application/json",
    //         },
    //         body: JSON.stringify({ username, password }),
    //     }).then((r) => {
    //         setLoading(false);
    //         if (r.ok) {
    //             r.json().then((user) => onLogin(user));
    //         } 
    //         else {
    //             r.json().then((err) => setErrors(err.errors));
    //         }
    //     });
    // }

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
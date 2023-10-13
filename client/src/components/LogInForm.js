import React from "react";
import { useFormik } from "formik"
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
        onSubmit: (values, {setSubmitting, setErrors}) => {
            fetch("/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(values),
            }).then((r) => {
                setSubmitting(false);
                if (r.ok) {
                    r.json().then((user) => onLogin(user));
                }
                else {
                    r.json().then(() => {
                        setErrors({'login': 'Invalid username or password'});
                    });
                }
            });
        }
    });

    return (
        <form onSubmit={formik.handleSubmit}>
            <h1>Login</h1>
            <div>
                <label htmlFor="username">Username</label>
                <input
                    type="text"
                    id="username"
                    autoComplete="off"
                    {...formik.getFieldProps("username")}
                />
                {formik.touched.username && formik.errors.username ? (
                    <div>{formik.errors.username}</div>
                ) : null}
            </div>

            <div>
                <label htmlFor="password">Password</label>
                <input
                    type="password"
                    id="password"
                    autoComplete="current-password"
                    {...formik.getFieldProps("password")}
                />
                {formik.touched.password && formik.errors.password ? (
                    <div>{formik.errors.password}</div>
                ) : null}
            </div>
            <div>
                <button type="submit">Login</button>
                {formik.isSubmitting ? <p>Loading...</p> : null}
            </div>
            <div>
                {formik.errors && formik.errors.length > 0 && (
                    <div>
                        {formik.errors.map((err, index) => (
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
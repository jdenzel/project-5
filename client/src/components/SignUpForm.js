import { useFormik } from "formik";
import { useEffect, useState } from "react";
import * as Yup from "yup";

const SignUpForm = ({ onLogin }) => {
    const [user, setUser] = useState(null);
    const [refreshPage, setRefreshPage] = useState(false);

    // useEffect(() => {
    //     fetch("/signup")
    //         .then((response) => response.json())
    //         .then((data) => {
    //             setUser(data);
    //             console.log(data);
    //             if (data.ok) {
    //                 onLogin(data);
    //             }
    //         });
    //     }, [refreshPage]);

    const signUpSchema = Yup.object().shape({
        username: Yup.string().required("Username is required"),
        password: Yup.string().required("Password is required"),
        passwordConfirmation: Yup.string()
            .oneOf([Yup.ref("password"), null], "Passwords must match")
            .required("Password confirmation is required"),
        first_name: Yup.string().required("First name is required"),
        last_name: Yup.string().required("Last name is required"),
        role: Yup.string().required("Role is required"),
        image_url: Yup.string().required("Image is required"),
        bio: Yup.string().required("Bio is required"),
        jersey_number: Yup.string().test({
            test: function(value) {
                // Check if the role is "player" and jersey_number is provided
                if (this.parent.role === "player" && !value) {
                    return this.createError({
                        path: 'jersey_number',
                        message: 'Jersey number is required',
                    });
                }
                return true;
            },
        }),
    });

    const formik = useFormik({
         initialValues:  {
            username: "",
            password: "",
            passwordConfirmation: "",
            role: "",
            first_name: "",
            last_name: "",
            image_url: "",
            bio: "",
            jersey_number: "",
        },
        validationSchema: signUpSchema,
        onSubmit: (values) => {
            fetch("/signup", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(values, null, 2),
            }).then((response) => {
                if (response.ok) {
                    response.json().then((user) => {
                        onLogin(user);
                    });
                    setRefreshPage(!refreshPage);
                }
            });
        },
    });

    // const handleSubmit = (values, { setSubmitting, setErrors }) => {
    //     setSubmitting(true);
    //     try {
    //         const r = fetch("/signup", {
    //             method: "POST",
    //             headers: {
    //                 "Content-Type": "application/json",
    //             },
    //             body: JSON.stringify(values),
    //             });
    //             if (r.ok) {
    //                 r.json().then((user) => onLogin(user));
    //             }
    //             else {
    //                 r.json().then((err) => setErrors(err.errors));
    //             }
    //         } catch (error) {
    //             console.error(error);
    //         }
    //         finally {
    //             setSubmitting(false);
    //     }
    // }


    return (
                <form onSubmit={formik.handleSubmit}>
                    <label htmlFor="username">Username</label>
                    <br />
                    <input
                        id = "username"
                        name = "username"
                        onChange={formik.handleChange}
                        value={formik.values.username}
                        />
                    <p>{formik.errors.username}</p>

                    <label htmlFor="password">Password</label>
                    <br />
                    <input
                        id = "password"
                        name = "password"
                        type = "password"
                        onChange={formik.handleChange}
                        value={formik.values.password}
                        />
                    <p>{formik.errors.password}</p>

                    <label htmlFor="passwordConfirmation">Confirm Password</label>
                    <br />
                    <input
                        id = "passwordConfirmation"
                        name = "passwordConfirmation"
                        type = "password"
                        onChange={formik.handleChange}
                        value={formik.values.passwordConfirmation}
                        />
                    <p>{formik.errors.passwordConfirmation}</p>

                    <label htmlFor="first_name">First Name</label>
                    <br />
                    <input
                        id = "first_name"
                        name = "first_name"
                        onChange={formik.handleChange}
                        value={formik.values.first_name}
                        />
                    <p>{formik.errors.first_name}</p>

                    <label htmlFor="last_name">Last Name</label>
                    <br />
                    <input
                        id = "last_name"
                        name = "last_name"
                        onChange={formik.handleChange}
                        value={formik.values.last_name}
                        />
                    <p>{formik.errors.last_name}</p>

                    <label htmlFor="bio">Biography</label>
                    <br />
                    <input
                        id = "bio"
                        name = "bio"
                        onChange={formik.handleChange}
                        value={formik.values.bio}
                        />
                    <p>{formik.errors.bio}</p>

                    <label htmlFor="image_url">Image</label>
                    <br />
                    <input
                        id = "image_url"
                        name = "image_url"
                        onChange={formik.handleChange}
                        value={formik.values.image_url}
                        />
                    <p>{formik.errors.image_url}</p>

                    <label htmlFor="role">Player or Admin</label>
                    <br />
                    <select
                        id = "role"
                        name = "role"
                        onChange={formik.handleChange}
                        value={formik.values.role}
                        >
                        <option value="">Select a role</option>
                        <option value="player">Player</option>
                        <option value="admin">Admin</option>
                    </select>
                    <p>{formik.errors.role}</p>

                    {formik.values.role === "player" ? (
                        <>
                            <label htmlFor="jersey_number">Jersey Number</label>
                            <br />
                            <input
                            id = "jersey_number"
                            name = "jersey_number"
                            onChange={formik.handleChange}
                            value={formik.values.jersey_number}
                            />
                            <p>{formik.errors.jersey_number}</p>
                        </>
                    ): null}

                    <button type="submit">Sign up</button>
                </form>
    )
}

export default SignUpForm;
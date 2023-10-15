import { useFormik } from "formik";
import { useState } from "react";
import * as Yup from "yup";


// SignUpForm component handles user signup
// use of formik and Yup for form validation
const SignUpForm = ({ onLogin }) => {

    // sets state
    const [refreshPage, setRefreshPage] = useState(false);


    // sets schemas for form validation    
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
        position: Yup.string().required("Position is required"),
        jersey_number: Yup.string().test({
            test: function(value) {
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

    // handles inputs for form
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
            position: "",
            jersey_number: "",
        },
        validationSchema: signUpSchema,
        onSubmit: (values, { setSubmitting, setErrors}) => {
            console.log(values)
            setSubmitting(true);
            fetch("/signup", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(values, null, 2),
            }).then((response) => {
                setSubmitting(false);
                if (response.ok) {
                    response.json().then((user) => {
                        onLogin(user);
                    });
                    setRefreshPage(!refreshPage);
                }
                else {
                    response.json().then((err) => {
                        if(err.username) {
                            setErrors({ username: err.username} );
                        } 
                        else {
                            setErrors({ password: err.password });
                        }    
                    });
                }
            });
        },
    });
    


    return (
        <form className="signup-content"  onSubmit={formik.handleSubmit}>
            <div className='user-password'>
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

            </div>

            <div className='user-first-last'>

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
            <input className="bio-input"
                id = "bio"
                name = "bio"
                onChange={formik.handleChange}
                value={formik.values.bio}
                />
            <p>{formik.errors.bio}</p>

            </div>

            <div className='user-image-role'>

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


            {formik.values.role === "player" ? ( // checks to see if value of role is player, if it is render jersey_number and position
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

                    <label htmlFor="jersey_number">Position</label>
                    <br />
                    <select
                    id = "position"
                    name = "position"
                    onChange={formik.handleChange}
                    value={formik.values.position}
                    >
                    <option value="">Select a position</option>
                    <option value="Point Guard">Point Guard</option>
                    <option value="Shooting Guard">Shooting Guard</option>
                    <option value="Center">Center</option>
                    <option value="Small Forward">Small Forward</option>
                    <option value="Power Forward">Power Forward</option>     
                    </select>
                    <p>{formik.errors.position}</p>
                    
                </>
            ): null}
            </div>
            <div className='signup-btn-div'>
            <button className="signup-btn" type="submit">Sign up</button>
            </div>
        </form>
    )
}

export default SignUpForm;
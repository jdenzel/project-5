import { useState } from "react";
import LoginForm from "./LogInForm";
import SignUpForm from "./SignUpForm";


// Login component that displays the login form and signup form
function Login({ onLogin }) {
    const [showLogin, setShowLogin] = useState(true);

    return (
        <div className="forms">
            {showLogin ? (
                <div className="login-form">
                    <LoginForm className="login-card"  onLogin={onLogin} />
                    <div className="signup-switch">
                    <p>Don't have an account?
                    <button className="signup-switch-btn" onClick={() => setShowLogin(false)}>Sign Up</button>
                    </p>
                    </div>
                </div>
            ) : (
                <div className="signup-form">
                    <SignUpForm className='signup-card' onLogin={onLogin} />
                    <h4>Already have an account? 
                    <button className="login-switch-btn" onClick={() => setShowLogin(true)}> Log In</button>
                    </h4>
                </div>
            )}
        </div>
    )
}

export default Login;
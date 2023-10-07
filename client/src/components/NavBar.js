import React from "react";
import { Link } from "react-router-dom/cjs/react-router-dom.min";

function NavBar({ user, setUser }) {
  function handleLogoutClick() {
    fetch("/logout", {
      method: "DELETE",
    }).then((r) => {
      if (r.ok) {
        setUser(null);
      }
    });
  }

    return (
        <div>
            <p>
                <Link to="/">Home</Link>
            </p>
            <nav>
            <span>{user.username}</span>
            <button onClick={handleLogoutClick}>Logout</button>
            </nav>
        </div>
    );
}
export default NavBar;
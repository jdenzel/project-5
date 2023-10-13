import React from "react";
import {  Link, useLocation } from "react-router-dom";


function NavBar({ user, setUser }) {
  const location = useLocation();
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
        <div class='nav-container'>
            <nav class='nav'>
            <Link to="/players" className={location.pathname === "/players" ? "active" : ""}>Players</Link>
            <Link to="/teams" className={location.pathname === "/teams" ? "active" : ""}>Teams</Link>
            <Link to="/" className={location.pathname === "/" ? "active" : ""}><i class ="fa fa-home w3-xxxlarge"></i></Link>
            <Link to="/leagues" className={location.pathname === "/leagues" ? "active" : ""}>Leagues</Link>
            <Link to="/user_profile" className={location.pathname === "/user_profile" ? "active" : ""}>Profile</Link>
            <span>
              {user.username}
              <button onClick={handleLogoutClick}>Logout</button>
            </span>
            </nav>

        </div>
    );
}
export default NavBar;
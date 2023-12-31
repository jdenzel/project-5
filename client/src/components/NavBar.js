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
        <div className='nav-container'>
            <nav className='nav'>
            <Link to="/players" className={location.pathname === "/players" ? "active" : ""}>Players</Link>
            <Link to="/teams" className={location.pathname === "/teams" ? "active" : ""}>Teams</Link>
            <Link to="/" className={location.pathname === "/" ? "active" : ""}><i className ="fa fa-home w3-xxxlarge"></i></Link>
            <Link to="/leagues" className={location.pathname === "/leagues" ? "active" : ""}>Leagues</Link>
            <Link to="/user_profile" className={location.pathname === "/user_profile" ? "active" : ""}>Profile</Link>
              <button className='logout-btn' onClick={handleLogoutClick}>Logout</button>
            </nav>
        </div>
    );
}
export default NavBar;
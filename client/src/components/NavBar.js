import React from "react";
import {  Link } from "react-router-dom";

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
            <nav>
            <span>{user.username}</span>
              <Link to="/">Home</Link>
              <Link to="/players">Players</Link>
              <Link to="/teams">Teams</Link>
              <Link to="/leagues">Leagues</Link>
              <Link to="/user_profile">Profile</Link>
            <button onClick={handleLogoutClick}>Logout</button>
            </nav>
        </div>
    );
}
export default NavBar;
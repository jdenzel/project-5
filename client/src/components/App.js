import React, { useEffect, useState } from "react";
import { Route, BrowserRouter as Router } from "react-router-dom";
import SignUpForm from "./SignUpForm";
import Login from "./Login";
import NavBar from "./NavBar";
import Teams from "./Teams";
import Profiles from "./Profiles";
import League from "./League";
import UserProfile from "./UserProfile";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => setUser(user));
      }
    });
  }, []);

  if (!user) return <Login onLogin={setUser} />;

  return (
    <main>

          <Router>
            <Route exact path="/">
            <div className="main-title">
              <h2>Welcome to</h2>
              <h1>Team Manager</h1>
            </div>
            </Route>
            <NavBar  user={user} setUser={setUser} />
            <Route path="/signup">
              <SignUpForm />
            </Route>
            <Route path="/teams">
              <Teams />
            </Route>
            <Route path="/players">
              <Profiles />
            </Route>
            <Route path="/leagues">
              <League />
            </Route>
            <Route path="/user_profile">
              <UserProfile />
            </Route>
          </Router>
      </main>
  );
}

export default App;

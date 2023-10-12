import React, { useEffect, useState } from "react";
import { Switch, Route, Routes, BrowserRouter as Router } from "react-router-dom";
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
    <>
    <NavBar  user={user} setUser={setUser} />
    <main>
        <div>
          <h1>Project</h1>
        </div>
        <div>
          <Router>
            <Route path="/signup">
              <SignUpForm />
            </Route>
            <Route path="/teams">
              <Teams />
            </Route>
            <Route path="/profiles">
              <Profiles />
            </Route>
            <Route path="/leagues">
              <League />
            </Route>
            <Route path="/user_profile">
              <UserProfile />
            </Route>
          </Router>
        </div>
      </main>
    </>
  );
}

export default App;

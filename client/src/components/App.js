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
    <>
    
    <main>
        
        <div>
          <Router>
            <NavBar  user={user} setUser={setUser} />
            <div>
              <h1>Project</h1>
            </div>
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
        </div>
      </main>
    </>
  );
}

export default App;

import React, { useEffect, useState } from "react";
import { Switch, Route, Routes, BrowserRouter as Router } from "react-router-dom";
import SignUpForm from "./SignUpForm";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => setUser(user));
      }
    });
  }, []);

  return (
    <>
      <div>
        <h1>Project</h1>
      </div>
      <div>
        <Router>
          <Route path="/signup">
            <SignUpForm />
          </Route>
        </Router>
      </div>
    </>
  );
}

export default App;

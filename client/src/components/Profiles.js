import { useEffect, useState } from "react";
import ProfileCard from "./ProfileCard";

function Profiles() {
    const [profiles, setProfiles] = useState([]);

    useEffect(() => {
        fetch("/profiles")
          .then((r) => r.json())
          .then(setProfiles);
      }, []);

    return (
        <div>
            <h2>Profiles</h2>
            <div>
                <ProfileCard profiles={profiles} />
            </div>
        </div>
    );
}

export default Profiles;
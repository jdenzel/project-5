import { useEffect, useState } from "react";
import ProfileCard from "./ProfileCard";

function League() {
    const [leagues, setLeagues] = useState([]);

    useEffect(() => {
        fetch("/leagues")
          .then((r) => r.json())
          .then(setProfiles);
      }, []);

    return (
        <div>
            <h2>Leagues</h2>
            <div>
                <ProfileCard profiles={profiles} />
            </div>
        </div>
    );
}

export default Profiles;
import { useEffect, useState } from "react";
import ProfileCard from "./ProfileCard";

function Profiles() {
    const [profiles, setProfiles] = useState([]);

    useEffect(() => {
        fetch("/players")
          .then((r) => r.json())
          .then(setProfiles);
      }, []);

    return (
        <div>
            <div className='player-filter'>
            <ul>
                <li></li>
            </ul>
            </div>
            <h2>Players</h2>
            <div>
                <ProfileCard profiles={profiles} />
            </div>
        </div>
    );
}

export default Profiles;
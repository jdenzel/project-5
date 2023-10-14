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
        <div className='players-body'>
            <div className='player-title-separator'>Players</div>
            <div>
                <ProfileCard profiles={profiles} />
            </div>
        </div>
    );
}

export default Profiles;
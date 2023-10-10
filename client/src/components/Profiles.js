import { useEffect, useState } from "react";

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
            <ul>
                {profiles.map((profile) => (
                    <li key={profile.id}>{profile.first_name}
                    {profile.last_name}
                    {profile.bio}
                    <img src={profile.image_url} alt={profile.first_name} />
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Profiles;
import { useEffect, useState } from "react";

function UserProfile() {
    const [user_profile, setUser_profile] = useState([]);

    useEffect(() => {
        fetch("/user_profile")
          .then((r) => r.json())
          .then(setUser_profile);
      }, []);

    return (
        <div>
            <h2>Profiles</h2>
            <button>Edit</button>
            <div>
                {user_profile.map((user_profile) => (
                    <div key={user_profile.id}>
                        <img srx={user_profile.image_url}/>
                        <p>{user_profile.first_name} {user_profile.last_name}</p>
                        <p>{user_profile.bio}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Profiles;
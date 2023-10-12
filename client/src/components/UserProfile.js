import { useEffect, useState } from "react";

function UserProfile() {
    const [user_profile, setUser_profile] = useState([]);
    const [isEditing, setIsEditing] = useState(false);
    const [form, setForm] = useState({
        first_name: "",
        last_name: "",
        bio: "",
        image_url: "",
        jersey_number: "",
    });

    useEffect(() => {
        fetch("/user_profile")
          .then((r) => r.json())
          .then(setUser_profile);
      }, []);

    const handleInput = (e) => {
        const key = e.target.name;
        const value = e.target.value;
        setForm({
            ...form,
            [key]: value,
        });
    };

    const handleEdit = () => {
        setForm({
            first_name: user_profile.first_name,
            last_name: user_profile.last_name,
            bio: user_profile.bio,
            image_url: user_profile.image_url,
            jersey_number: user_profile.jersey_number,
        });
        setIsEditing(true);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch("/user_profile", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(form),
        })
        .then((r) => r.json())
        .then((updatedUser) => {
            setUser_profile(updatedUser);
        })
        .catch((error) => {
            console.error(error);
        });
    };
    

    return (
        <div>
            <h2>Profiles</h2>
            <button>Edit</button>
            <div>
                {/* {user_profile.map((user_profile) => ( */}
                    <div key={user_profile.id}>
                        <img src={user_profile.image_url}/>
                        <p>Name: {user_profile.first_name} {user_profile.last_name}</p>
                        <p>Bio: {user_profile.bio}</p>
                    </div>
                {/* ))} */}
            </div>
        </div>
    );
}

export default UserProfile;
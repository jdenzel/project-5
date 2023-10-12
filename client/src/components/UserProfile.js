import { useEffect, useState } from "react";

function UserProfile() {
    const [user_profile, setUser_profile] = useState([]);
    const [isEditing, setIsEditing] = useState(false);
    const [form, setForm] = useState({
        first_name: "",
        last_name: "",
        bio: "",
        image_url: "",
        // jersey_number: "",
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
            // jersey_number: user_profile.jersey_number,
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
        .then((response) => {
            // const updatedProfile = response.updatedProfile
            console.log(response)
            console.log(response.first_name)
            setUser_profile(response);
            setIsEditing(false);
        })
        .catch((error) => {
            console.error(error);
        });
    };
    

    return (
        // <div>
        //     <h2>Profile</h2>
        //     <div>   
        //         <img src={user_profile.image_url} alt={user_profile.first_name} />
        //         <h2>Name: {user_profile.first_name} {user_profile.last_name}</h2>
        //         <p>Bio: {user_profile.bio}</p>
        //         {/* <p>Jersey Number: {user_profile.jersey_number}</p> */}
        //         </div>
        // </div>

        <div>
            <h2>Profiles</h2>
            {!isEditing ?(
                <div>
                    <img src={user_profile.image_url} alt={user_profile.first_name} />
                    <h2>Name: {user_profile.first_name} {user_profile.last_name}</h2>
                    <p>Bio: {user_profile.bio}</p>
                    {/* <p>Jersey Number: {user_profile.jersey_number}</p> */}
                    <button onClick={handleEdit}>Edit</button>
                </div>
            ) : (
                <form onSubmit={handleSubmit}>
                    <label>First Name: 
                        <input 
                            type="text"
                            name="first_name"
                            value={form.first_name}
                            onChange={handleInput}
                        />
                    </label>
                    <label>Last Name: 
                        <input 
                            type="text"
                            name="last_name"
                            value={form.last_name}
                            onChange={handleInput}
                        />
                    </label>
                    <label>Bio: 
                        <input 
                            type="text"
                            name="bio"
                            value={form.bio}
                            onChange={handleInput}
                        />
                    </label>
                    <label>Image URL: 
                        <input 
                            type="text"
                            name="image_url"
                            value={form.image_url}
                            onChange={handleInput}
                        />
                    </label>
                    {/* <label>Jersey Number: 
                        <input 
                            type="text"
                            name="jersey_number"
                            value={form.jersey_number}
                            onChange={handleInput}
                        />
                    </label> */}
                    <button type="submit">Save</button>
                </form>
            )}
        </div>
    );
}

export default UserProfile;
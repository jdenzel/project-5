import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import Login from "./Login";

function UserProfile( {onLogout }) {

    // sets states
    const [user_profile, setUser_profile] = useState({});
    const [isEditing, setIsEditing] = useState(false);
    const [form, setForm] = useState({
        first_name: "",
        last_name: "",
        bio: "",
        image_url: "",
        position: "",
    });
    const history = useHistory();
    const [isLoggedOut, setIsLoggedOut] = useState(false);

    // fetches data of user profile
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
            position: user_profile.position,
        });
        setIsEditing(true);
    };

    // Handles submission of profile for updating values
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
            console.log(response)
            console.log(response.position)
            setUser_profile(response);
            setIsEditing(false);
        })
        .catch((error) => {
            console.error(error);
        });
    };

    // Handles deletion of user profile
    const handleDelete = () => {
        fetch("/user_profile", {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then((r) => {
            if (r.status === 200) {
                setIsLoggedOut(true);
                onLogout();
                history.push("/login");

            }
            else {
                console.log("Failed to delete Account")
            }
        })
        .catch((error) => {
            console.error(error);
        });
    }
    if(isLoggedOut) {
        return <Login onLogin={onLogout} />
    }
    

    return (
        <div>
            <h2>Profiles</h2>
            {!isEditing ?( // condition to see if editing is true, if it is false then display the div called user-profile-container if not display the form-edit
                <div className="user-profile-container">
                    <div className='user-title-separator'>Profile</div>
                        <div className="user-profile">
                        <div className="user-profile-card">
                        <img src={user_profile.image_url} alt={user_profile.first_name} />
                        <h1>Name: {user_profile.first_name} {user_profile.last_name}</h1>
                        <h2>Position: {user_profile.position}</h2>
                        <p>{user_profile.bio}</p>
                        <button className='edit-button' onClick={handleEdit}>Edit</button>
                        </div>
                    </div>
                </div>
            ) : (
                <div className="form-edit">
                <form className='edit-content' onSubmit={handleSubmit}>
                    <div className="edit-fn">
                    <label>First Name: 
                        <input 
                            type="text"
                            name="first_name"
                            value={form.first_name}
                            onChange={handleInput}
                        />
                    </label>
                    </div>
                    <div className="edit-ln">
                    <label>Last Name: 
                        <input 
                            type="text"
                            name="last_name"
                            value={form.last_name}
                            onChange={handleInput}
                        />
                    </label>
                    </div>
                    <div className="edit-bio">
                    <label>Bio: 
                        <input 
                            type="text"
                            name="bio"
                            value={form.bio}
                            onChange={handleInput}
                        />
                    </label>
                    </div>
                    <div className="edit-img">
                    <label>Image URL: 
                        <input 
                            type="text"
                            name="image_url"
                            value={form.image_url}
                            onChange={handleInput}
                        />
                    </label>
                    </div>
                    <div className="edit-pos">
                    <label>Position: 
                        <select 
                            type="text"
                            name="position"
                            value={form.position}
                            onChange={handleInput}
                        >
                        <option value="">Select a position</option>
                            <option value="Point Guard">Point Guard</option>
                            <option value="Shooting Guard">Shooting Guard</option>
                            <option value="Center">Center</option>
                            <option value="Small Forward">Small Forward</option>
                            <option value="Power Forward">Power Forward</option> 
                        </select>
                    </label>
                    </div>
                    <button className="save-btn" type="submit">Save</button>
                    <button className="delete-btn" onClick={handleDelete}>Delete</button>
                </form>
                </div>
            )}
            
        </div>
    );
}

export default UserProfile;
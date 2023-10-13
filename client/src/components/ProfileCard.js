import React from "react";

function ProfileCard({ profiles }) {
    return (
        <div class="player-card">
            {profiles.map((profile, index) => (
                <div key={index} >
                    <img src={profile.image_url} alt={profile.first_name} />
                    <h2>Name: {profile.first_name} {profile.last_name}</h2>
                    <p>Bio: {profile.bio}</p>
                </div>
            ))}

        </div>
    );
}

export default ProfileCard;
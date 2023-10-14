import React from "react";

function ProfileCard({ profiles }) {
    return (
        <div className='player-container'>
            {profiles.map((profile, index) => (
                <div className="player-card" key={index} >
                    <img src={profile.image_url} alt={profile.first_name} />
                    <h2>{profile.first_name} {profile.last_name}</h2>
                    <p>{profile.position ?? 'N/A'}</p>
                </div>
            ))}

        </div>
    );
}

export default ProfileCard;
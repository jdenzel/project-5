import React from "react";

function TeamCard({ teams }) {
    return (
        <div>
            {teams.map((team, index) => (
                <div key={index} >
                    <h2>{team.name}</h2>
                    <img src={team.image_url} alt={team.name} />
                </div>
            ))}

        </div>
    );
}

export default TeamCard;
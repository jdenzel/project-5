import React from "react";

function TeamCard({ teams }) {
    return (
        <div className='team-container'>
            {teams.map((team, index) => (
                <div className='team-card' key={index} >
                    <img src={team.logo} alt={team.name} />
                    <h2>{team.name}</h2>
                </div>
            ))}

        </div>
    );
}

export default TeamCard;
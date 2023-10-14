import React from "react";

function LeagueCard({ leagues }) {
    return (
        <div className="league-container">
            {leagues.map((league, index) => (
                <div className="league-card" key={index} >
                    <img src={league.logo} alt={league.name} />
                    <h2>{league.name}</h2>
                </div>
            ))}

        </div>
    );
}

export default LeagueCard;

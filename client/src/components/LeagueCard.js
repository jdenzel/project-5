import React from "react";

function LeagueCard({ leagues }) {
    return (
        <div>
            {leagues.map((league, index) => (
                <div key={index} >
                    <h2>{league.name}</h2>
                    <img src={league.logo} alt={league.name} />
                </div>
            ))}

        </div>
    );
}

export default LeagueCard;

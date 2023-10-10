import { useEffect, useState } from "react";

function Teams() {
    const [teams, setTeam] = useState([]);

    useEffect(() => {
        fetch("/teams")
          .then((r) => r.json())
          .then(setTeam);
      }, []);

    return (
        <div>
            <h2>Teams</h2>
            <ul>
                {teams.map((team) => (
                    <li key={team.id}>{team.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default Teams;
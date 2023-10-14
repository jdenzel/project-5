import { useEffect, useState } from "react";
import TeamCard from "./TeamCard";

function Teams() {
    const [teams, setTeam] = useState([]);

    useEffect(() => {
        fetch("/teams")
          .then((r) => r.json())
          .then(setTeam);
      }, []);

    return (
        <div>
            <div className="team-title-separator">Teams</div>
            <div>
                <TeamCard teams={teams} />
            </div>
        </div>
    );
}

export default Teams;
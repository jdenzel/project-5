import { useEffect, useState } from "react";
import TeamCard from "./TeamCard";

// fetches team data and returns it to TeamCard for displaying on webpage
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
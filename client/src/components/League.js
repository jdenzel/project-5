import { useEffect, useState } from "react";
import LeagueCard from "./LeagueCard";

function League() {
    const [leagues, setLeagues] = useState([]);

    useEffect(() => {
        fetch("/leagues")
          .then((r) => r.json())
          .then(setLeagues);
      }, []);

    return (
        <div>
            <h2>Leagues</h2>
            <div>
                <LeagueCard leagues={leagues} />
            </div>
        </div>
    );
}

export default League;
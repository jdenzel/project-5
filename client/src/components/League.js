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
        <div className="league-body">
            <div className='league-title-separator'>Leagues</div>
            <div>
                <LeagueCard leagues={leagues} />
            </div>
        </div>
    );
}

export default League;
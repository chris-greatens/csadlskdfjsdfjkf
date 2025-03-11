import { useRouter } from "next/router";
function IndividualSet() {
    const { query } = useRouter();
    console.log(query);
    return (
        <div>
            This is a {query.type} set for {query.player}.
        </div>
    )
};
export default IndividualSet;
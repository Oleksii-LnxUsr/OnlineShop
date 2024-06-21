import classes from "./Header.module.css";
import { Link } from "react-router-dom";


const Header = () => {
    return(
        <div className={classes.Header}>
            <h3 className={classes.Logo}>Online Market</h3>
            <div className={classes.Navigation}>
                <Link to="#" className={classes.NavigationItem}>
                    <span>Phones</span>
                </Link>
                <Link to="#" className={classes.NavigationItem}>
                    <span>Laptops</span>
                </Link>
                <Link to="#" className={classes.NavigationItem}>
                    <span>Headphones</span>
                </Link>
            </div>
        </div>
    )
}

export default Header
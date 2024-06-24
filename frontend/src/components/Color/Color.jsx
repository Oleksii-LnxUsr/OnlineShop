import { Box } from "@mui/material";
import classes from "./Color.module.css";

const Color = ({ color, isActive }) => {
    console.log(isActive)
    return (
        <Box 
            className={classes.ColorContainer} 
            sx={{ border: isActive && "1px solid black", borderRadius: '50%' }}>
            <Box 
                className={`${classes.ColorCircle} ${isActive ? classes.active : ''}`} 
                sx={{ background: color }}
            >
            </Box>
        </Box>
    );
}

export default Color;

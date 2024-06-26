import { List, ListItemText, ListItemButton, Checkbox, FormControlLabel, Box } from "@mui/material"
import Collapse from '@mui/material/Collapse';
import RemoveIcon from '@mui/icons-material/Remove';
import AddIcon from '@mui/icons-material/Add';
import { useState } from "react";
import classes from "./FilterCollapse.module.css"


const FilterCollapse = ({ filterName, filterData }) => {
    const [open, setOpen] = useState(false)

    const handleClick = () => {
        setOpen(!open)
    }

    return(
        <List disablePadding>
            <ListItemButton className={classes.FilterButton} onClick={handleClick}>
                <ListItemText className={classes.FilterButtonText} primary={filterName} />
                {open ? <RemoveIcon /> : <AddIcon />}
            </ListItemButton>
            <Collapse in={open} timeout="auto">
                <List component="div" sx={{ display: 'flex', flexDirection: 'column'}}>
                    {filterData?.map((filter, index) => {
                        return(
                            <Box sx={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: '10px' }}>
                                <FormControlLabel
                                    className={classes.FilterItem}
                                    control={<Checkbox />}
                                    label={filter.name}
                                    key={index} 
                                />
                                {filter?.hex_code && (
                                    <Box 
                                        sx={{ background: filter?.hex_code }} 
                                        className={classes.FilterColor}
                                    />
                                )}
                            </Box>
                        )
                    })}
                </List>
            </Collapse>
        </List>
    )
}

export default FilterCollapse
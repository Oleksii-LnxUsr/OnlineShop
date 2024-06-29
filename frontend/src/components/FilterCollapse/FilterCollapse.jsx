import { List, ListItemText, ListItemButton } from "@mui/material";
import Collapse from '@mui/material/Collapse';
import RemoveIcon from '@mui/icons-material/Remove';
import AddIcon from '@mui/icons-material/Add';
import { useState } from "react";
import FilterItem from './FilterItem';
import classes from "./FilterCollapse.module.css";

const FilterCollapse = ({ filterName, filterData, setSelectedFilters, selectedFilters }) => {
    const [open, setOpen] = useState(false); // Состояние для управления раскрытием списка

    // Обработчик изменения состояния чекбоксов
    const handleCheckboxChange = (filterValue) => (event) => {
        setSelectedFilters((prev) => {
            const currentValues = prev[filterName] || [];
    
            // Проверяем, есть ли filterValue уже в текущих значениях
            const isValueSelected = currentValues.includes(filterValue);
    
            let newValues;
    
            // Если checkbox был отмечен и значение еще не было выбрано, добавляем его
            if (event.target.checked && !isValueSelected) {
                newValues = [...currentValues, filterValue];
            } else {
                // Если checkbox был снят или значение уже было выбрано, удаляем его
                newValues = currentValues.filter((value) => value !== filterValue);
            }
    
            return { ...prev, [filterName]: newValues };
        });
    };

    // Обработчик клика для раскрытия/сворачивания списка
    const handleClick = () => {
        setOpen(!open);
    }

    return (
        <List disablePadding>
            <ListItemButton className={classes.FilterButton} onClick={handleClick}>
                <ListItemText className={classes.FilterButtonText} primary={filterName} />
                {open ? <RemoveIcon /> : <AddIcon />}
            </ListItemButton>
            <Collapse in={open} timeout="auto">
                <List component="div" sx={{ display: 'flex', flexDirection: 'column' }}>
                    {filterData?.map((filter, index) => {
                        const isChecked = selectedFilters?.includes(filter.name) || false;
                        return (
                            <FilterItem
                                key={index}
                                filter={filter}
                                checked={isChecked}
                                onChange={handleCheckboxChange(filter.name)}
                            />
                        );
                    })}
                </List>
            </Collapse>
        </List>
    );
}

export default FilterCollapse;

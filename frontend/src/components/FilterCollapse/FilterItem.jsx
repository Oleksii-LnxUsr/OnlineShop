import { Box, FormControlLabel, Checkbox } from '@mui/material';
import classes from "./FilterCollapse.module.css";

// Компонент для рендеринга одного элемента фильтра
const FilterItem = ({ filter, checked, onChange }) => (
    <Box sx={{ display: 'flex', flexDirection: 'row', alignItems: 'center', marginBottom: '10px' }}>
        <FormControlLabel
            className={classes.FilterItem}
            control={<Checkbox checked={checked} onChange={onChange} />}
            label={filter.name}
        />
        {/* Если у фильтра есть hex-код, показываем цветной блок */}
        {filter?.hex_code && (
            <Box
                sx={{ background: filter?.hex_code }}
                className={classes.FilterColor}
            />
        )}
    </Box>
);

export default FilterItem;

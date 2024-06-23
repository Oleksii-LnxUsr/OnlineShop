import { Container, Grid, Box } from '@mui/material';
import ProductCard from "../../components/ProductCard/ProductCard"
import classes from "./Index.module.css"

const Index = () => {
    return(
        <Container maxWidth="lg" sx={{ marginTop: "10px" }}>
            <Grid container>
                <Grid container item lg={3} md={3}>
                    <Grid item lg={12} md={12}>
                        <Box className={classes.FilterItem}>Filtration</Box>
                        <Box className={classes.FilterItem}>Colors</Box>
                        <Box className={classes.FilterItem}>Brands</Box>
                        <Box className={classes.FilterItem}>Price</Box>
                    </Grid>
                </Grid>
                <Grid container item lg={9} md={9}>
                    <Grid item lg={4} md={4}>
                        <ProductCard />
                    </Grid>
                    <Grid item lg={4} md={4}>
                        <ProductCard />
                    </Grid>
                    <Grid item lg={4} md={4}>
                        <ProductCard />
                    </Grid>
                </Grid>
            </Grid>
        </Container>
    )
}

export default Index
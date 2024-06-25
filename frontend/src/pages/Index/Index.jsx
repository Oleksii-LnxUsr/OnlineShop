import { Container, Grid, Box } from '@mui/material';
import ProductCard from "../../components/ProductCard/ProductCard"
import classes from "./Index.module.css"
import getProducts from '../../api/GetProducts';
import { useEffect, useState } from 'react';

const Index = () => {
    const [data, setData] = useState()
    useEffect(() => {
        getProducts(setData)
    }, [])

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
                    {data?.map((product, index) => (
                        <Grid item lg={4} md={4} key={index}>
                            <ProductCard product={product} />
                        </Grid>
                    ))}
                </Grid>
            </Grid>
        </Container>
    )
}

export default Index
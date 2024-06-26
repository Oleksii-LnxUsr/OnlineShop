import { Container, Grid } from '@mui/material';
import ProductCard from "../../components/ProductCard/ProductCard"
import getProducts from '../../api/GetProducts';
import { useEffect, useState } from 'react';
import FilterCollapse from '../../components/FilterCollapse/FilterCollapse';
import getAvailableFilters from '../../api/GetAvailableFilters';

const Index = () => {
    const [products, setProducts] = useState()
    const [filters, setFilters] = useState()

    useEffect(() => {
        getProducts(setProducts)
        getAvailableFilters(setFilters)
    }, [])

    return(
        <Container maxWidth="lg" sx={{ marginTop: "10px" }}>
            <Grid container>
                <Grid container item lg={3} md={3}>
                    <Grid item lg={12} md={12}>
                        <FilterCollapse filterName='Category' filterData={filters?.categories} />
                        <FilterCollapse filterName='Brand' filterData={filters?.brands} />
                        <FilterCollapse filterName='Color' filterData={filters?.colors} />
                    </Grid>
                </Grid>
                <Grid container item lg={9} md={9}>
                    {products?.map((product, index) => (
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
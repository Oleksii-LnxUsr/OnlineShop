import { Container, Grid } from '@mui/material';
import ProductCard from "../../components/ProductCard/ProductCard"
import getProducts from '../../api/GetProducts';
import { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import FilterCollapse from '../../components/FilterCollapse/FilterCollapse';
import getAvailableFilters from '../../api/GetAvailableFilters';

const Index = () => {
    const [products, setProducts] = useState()
    const [filters, setFilters] = useState()
    const [selectedFilters, setSelectedFilters] = useState([])

    const location = useLocation();
    const navigate = useNavigate();

    useEffect(() => {
        getProducts(setProducts)
        getAvailableFilters(setFilters)

        const searchParams = new URLSearchParams(location.search);

        const initialFilters = {};
        for (const [key, value] of searchParams.entries()) {
            initialFilters[key] = value.split(',');
        }

        setSelectedFilters(initialFilters)
    }, [])

    useEffect(() => {
        const searchParams = new URLSearchParams(location.search);
        Object.entries(selectedFilters).forEach(([key, values]) => {
            if (values.length) {
                searchParams.set(key, values.join(','));
            } else {
                searchParams.delete(key);
            }
        });
        navigate({ search: searchParams.toString() }, { replace: true });
    }, [selectedFilters])

    console.log(selectedFilters)

    return(
        <Container maxWidth="lg" sx={{ marginTop: "10px" }}>
            <Grid container>
                <Grid container item lg={3} md={3}>
                    <Grid item lg={12} md={12}>
                        <FilterCollapse 
                            filterName='Category' 
                            filterData={filters?.categories} 
                            setSelectedFilters={setSelectedFilters}
                            selectedFilters={selectedFilters?.Category}
                        />
                        <FilterCollapse 
                            filterName='Brand' 
                            filterData={filters?.brands} 
                            setSelectedFilters={setSelectedFilters}
                            selectedFilters={selectedFilters?.Brand}
                        />
                        <FilterCollapse 
                            filterName='Color' 
                            filterData={filters?.colors} 
                            setSelectedFilters={setSelectedFilters}
                            selectedFilters={selectedFilters?.Color}
                        />
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
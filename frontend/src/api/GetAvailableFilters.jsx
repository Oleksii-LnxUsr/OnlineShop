import axios from 'axios';

const getAvailableFilters = (setData) => {
  const BASE_URL = import.meta.env.VITE_APP_BASE_URL;

  axios.get(`${BASE_URL}products/filters/`)
    .then(response => {
      setData(response.data)
      console.log(response.data)
    })
    .catch(error => {
      console.log(error)
    });
};

export default getAvailableFilters
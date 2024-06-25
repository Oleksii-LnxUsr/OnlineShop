import axios from 'axios';

const getProducts = (setData) => {
  const BASE_URL = import.meta.env.VITE_APP_BASE_URL;

  axios.get(`${BASE_URL}products/`)
    .then(response => {
      setData(response.data)
    })
    .catch(error => {
      console.log(error)
    });
};

export default getProducts
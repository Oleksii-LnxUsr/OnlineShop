import './App.css'
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { publicRoutes } from "./routes";
import Header from './components/Header/Header';

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        {publicRoutes.map((route_item) => (
          <Route
            key={route_item.path}
            path={route_item.path}
            element={<route_item.component/>}
          />
        ))}
      </Routes>
    </BrowserRouter>
  )
}

export default App

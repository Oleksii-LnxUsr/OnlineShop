import classes from "./ProductCard.module.css";
import phoneImg from "../../media/PhoneImg.webp"
import Color from "../Color/Color";

const ProductCard = () => {
    return(
        <div className={classes.ProductCard}>
            <img 
                draggable={false} 
                src={phoneImg} 
                alt="phone img"
                className={classes.ProductImage} />
            <p>Nothing Phone</p>
            <div className={classes.ProductColors}>
                <Color color={"green"} isActive={true} />
                <Color color={"orange"} isActive={false} />
            </div>
            <p>200$</p>
        </div>
    )
}

export default ProductCard
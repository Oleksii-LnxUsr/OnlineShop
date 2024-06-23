import classes from "./ProductCard.module.css";
import phoneImg from "../../media/PhoneImg.webp"

const ProductCard = () => {
    return(
        <div className={classes.ProductCard}>
            <img src={phoneImg} alt="phone" className={classes.ProductImage} />
            <p>Nothing Phone</p>
            {/* <Colors /> */}
            <p>200$</p>
        </div>
    )
}

export default ProductCard
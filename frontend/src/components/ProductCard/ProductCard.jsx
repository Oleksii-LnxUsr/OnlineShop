import classes from "./ProductCard.module.css";
import phoneImg from "../../media/PhoneImg.webp"
import Color from "../Color/Color";

const ProductCard = (product) => {
    return(
        <div className={classes.ProductCard}>
            <img 
                draggable={false} 
                src={phoneImg} 
                alt="phone img"
                className={classes.ProductImage} />
            <p>{product?.product?.name}</p>
            <div className={classes.ProductColors}>
                {product.product.configuration?.map((configuration, index) => (
                    <Color color={configuration?.color?.hex_code} key={index} />
                ))}
            </div>
            <p>200$</p>
        </div>
    )
}

export default ProductCard
import classes from "./ProductCard.module.css";
import phoneImg from "../../media/PhoneImg.webp"
import Color from "../Color/Color";

const ProductCard = (product) => {
    return(
        <div className={classes.ProductCard}>
            <img 
                draggable={false}
                src={phoneImg}
                alt={product?.product?.name}
                className={classes.ProductImage} />
            <p className={classes.ProductName}>{product?.product?.name}</p>
            <div className={classes.ProductColors}>
                {product?.product?.configuration?.map((configuration, index) => (
                    <Color color={configuration?.color?.hex_code} key={index} />
                ))}
            </div>
        </div>
    )
}

export default ProductCard
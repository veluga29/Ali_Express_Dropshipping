import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link';

import Layout from '../../src/components/layout'

import axios from 'axios'


export default function ProductDetail( { productData } ) {
  let product;
  if (productData) {
    const carouselIndicatorsArray = productData.productImages.map((productImage, idx) => {
      return (      
        <button
          type="button"
          key={idx}
          data-bs-target="#carouselIndicators"
          className={ idx == 0 ? "active" : "" }
          data-bs-slide-to={`${idx}`}
          aria-label={`Slide ${idx + 1}`} />
      )
    });
    const carouselImagesArray = productData.productImages.map((productImage, idx) => {
      return (      
        <div className={`carousel-item ${ idx == 0 ? 'active' : ''}`} key={idx}>
          <Image
            src={productImage}
            className="d-block w-100"
            height={500}
            width={500}
            alt="Product Image" />
        </div>
      )
    });
    const carousel = (
      <div id="carouselIndicators" className="carousel carousel-dark slide" data-bs-ride="carousel">
        <div className="carousel-indicators">
          {carouselIndicatorsArray}
        </div>
        <div className="carousel-inner" >
          {carouselImagesArray}
        </div>
        <button
          className="carousel-control-prev"
          type="button"
          data-bs-target="#carouselIndicators"
          data-bs-slide="prev" 
        >
          <span className="carousel-control-prev-icon" aria-hidden="true"></span>
          <span className="visually-hidden">Previous</span>
        </button>
        <button
          className="carousel-control-next"
          type="button"
          data-bs-target="#carouselIndicators"
          data-bs-slide="next"
        >
          <span className="carousel-control-next-icon" aria-hidden="true"></span>
          <span className="visually-hidden">Next</span>
        </button>
      </div>
    )
    const reviewStar = []
    const limit = Math.floor(productData.reviewsRatings.averageRating)
    for (let i = 0; i < 5; i++) {
      const starImage = i < limit ? (
        <Image 
          src="/images/review_red_star.png"
          key={i}
          width={23}
          height={17}
          alt="Star"
        />
      ) : (
        <Image 
          src="/images/review_empty_star.png"
          key={i}
          width={22}
          height={18}
          alt="Star"
        />
      )
      reviewStar.push(starImage)
    }

    product = (
      <div className="container-fluid d-flex justify-content-center my-5">
        <div className="col-4">
          {carousel}
        </div>
        <div className="offset-1 col-6">
          <div>
            <h3>{productData.title}</h3>
            <p>
              {reviewStar}
              &nbsp;
              {productData.reviewsRatings.averageRating}
              &nbsp;&nbsp;&nbsp;
              {productData.reviewsRatings.totalCount} Review
              &nbsp;
              {productData.totalOrders} Order
            </p>
          </div>
          <br/>
          <div>
            <h4>
              Max discounted price(Web): {productData.currency}
              &nbsp;
              {productData.priceSummary.web.discountedPrice.min.display||productData.price.web.discountedPrice.min.display||'Please go to Ali-Express to check the price'}
            </h4>
            <h4>
              Max discounted price(App): {productData.currency}
              &nbsp;
              {productData.priceSummary.app.discountedPrice.min.display||productData.price.app.discountedPrice.min.display||'Please go to Ali-Express to check the price'}
            </h4>
          </div>
          <br/>
          <div>
            <h5>Total stock: {productData.totalStock} ({productData.unitNamePlural})</h5>
            <h5>Wishlist count: {productData.wishlistCount}</h5>
            <h5>Shipping from: {productData.shipping.shipFrom}</h5>
            <h5>Shipping to: {productData.shipTo}</h5>
            <h5>Delivery processing time: {productData.processingTimeInDays} (Days)</h5>
            <h5>Company: {productData.seller.storeName}</h5>
          </div>
          <br/>
          <div>            
            <a 
              className="btn btn-danger alert-danger"
              href={productData.productUrl}
              target="_blank"
              rel="noreferrer">
                Go to Ali-Express item page
            </a>            
          </div>
        </div>
      </div>
    )
  } else {
    product = (
      <div className="d-flex justify-content-center align-items-center" style={{height: "580px"}}>
        <h2>Sorry, the product is not available at this moment</h2>
      </div>
    )
  }

  return (
    <Layout>
      <Head>
        <title>Product Detail</title>
      </Head>
      <section>
        {product}
      </section>
    </Layout>
  )
}

export async function getServerSideProps({ params, req }) {
  let props = { productData: undefined };
  try {
    const cookieString = req ? req.headers.cookie : '';
    let access_token;
    // cookie parsing
    if (cookieString) {
      const cookieArray = cookieString.split(';');
      for (let cookie of cookieArray) {
        const pureCookie = cookie.trim();
        const key = pureCookie.split('=')[0];
        const value = pureCookie.split('=')[1];
        if (key === 'access_token') {
          access_token = value;
        }
      }
    }

    // authentication of JWT token
    if (!access_token) {
      return {
        redirect: {
          destination: `/signin?retUrl=/product/${params.product_id}`,
          permanent: false,
        },
      }
    }
    try{
      await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/aaa/token`, {
        headers: {
            Authorization: `bearer ${access_token}`
        }
      }); 
    } catch (error) {
      return {
        redirect: {
          destination: `/signin?retUrl=/product/${params.product_id}`,
          permanent: false,
        },
      }
    }
    
    const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/products/${params.product_id}`, {
      headers: {  
        Authorization: `bearer ${access_token}`
      }
    });
    const productData = response.data
    return {
      props: {
        productData,
      }
    }
  } catch {
    props.productData = null;
  }
  return {
    props
  }
}
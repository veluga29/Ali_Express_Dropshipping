import Head from 'next/head'
import Image from 'next/image'

import Layout from '../../src/components/layout'
import styles from '/styles/products.module.css'

import axios from 'axios'

export default function ProductDetail( { productData } ) {
  let product;
  if (productData) {
    product = (
      <>
        <Image
            src={productData.productImages[0]}
            height={200}
            width={200}
            alt="Product Image" />
        <h1>{productData.title}</h1>
        <p>
          {/* {productData.price.web.display || 0} <br /> */}
          {/* {productData.reviewsRatings.averageRating || 0} */}
        </p>
      </>
    )
  } else {
    product = (
        <h2>Sorry, the product is not available at this moment</h2>
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
  let props = {};
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
    const headers = {  
      Authorization: `bearer ${access_token}`
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
      await axios.get('http://localhost:8000/aaa/token', {
        headers: {
          Cookie: `access_token=${access_token}`
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
    
    const response = await axios.get(`http://localhost:8000/products/${params.product_id}`, {
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
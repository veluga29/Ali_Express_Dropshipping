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
        <h2>Sorry, there is no detail.</h2>
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
    const tokenIdx = cookieString.indexOf('access_token') + 13;
    const access_token = cookieString.slice(tokenIdx).split(';')[0];
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
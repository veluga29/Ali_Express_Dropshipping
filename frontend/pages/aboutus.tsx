import Image from 'next/image'
import Head from 'next/head'

import Layout from '../src/components/layout'


export default function Aboutus() {
  return (
    <Layout>
      <Head>
        <title>Aboutus</title>
      </Head>
      <div className="d-flex justify-content-center align-items-center" style={{height: "500px"}}>
        <Image
          src="/images/prepare.png"
          width={650}
          height={400}
          alt="Comming soon" />
      </div>
    </Layout>
  )
}
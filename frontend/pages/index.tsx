import type { NextPage } from 'next'
import Head from 'next/head'
import { useRouter } from 'next/router'

import axios from 'axios'
import { useEffect } from 'react'
import { useCookies } from "react-cookie"


const Home: NextPage = () => {
  const router = useRouter();
  const [ cookies, ,removeCookie ] = useCookies(["access_token"]);
  let access_token = cookies.access_token;

  useEffect(() => {
    if (!access_token) {
      router.push('/signin');
      return;
    }
    const verifyToken = async () => { 
      try{
        const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/aaa/token`, {
          headers: {
              Authorization: `bearer ${access_token}`
          }
        }); 
        if (response.data.valid) {
          router.push('/products');
        }
      } catch (error) {
        // Delete access token cookie
        removeCookie('access_token');
        router.push('/signin');
      }
    }
    verifyToken();
  });

  return (
    <div className="d-flex justify-content-center align-items-center" style={{height: 850}}>
      <Head>
        <title>Index</title>
      </Head>
      <div className="spinner-border text-warning" role="status" style={{width: '8rem', height: '8rem'}}>
        <span className="visually-hidden">Loading...</span>
      </div>
    </div>
  )
}

export default Home

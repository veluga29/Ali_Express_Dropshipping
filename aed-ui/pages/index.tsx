import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import { useRouter } from 'next/router'
import styles from '../styles/Home.module.css'

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
        const response = await axios.get('http://localhost:8000/aaa/token', {withCredentials: true}); 
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
    <div className={styles.container}>
      <Head>
        <title>Index</title>
      </Head>
      <h1>Loading...</h1>
    </div>
  )
}

export default Home

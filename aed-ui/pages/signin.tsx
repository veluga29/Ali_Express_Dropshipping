import Link from 'next/link'
import Head from 'next/head'
import { useRouter } from 'next/router'
import Layout from '../src/components/layout'
import styles from '/styles/signin.module.css'

import { useState } from "react";
import { useEffect } from 'react'
import { useCookies } from "react-cookie"
import axios from 'axios';
import FormData from 'form-data';

export default function Signin() {
  const [cookies, setCookie] = useCookies(["access_token"]);
  const router = useRouter();
  useEffect(() => {
    let access_token = cookies.access_token;
    if (!access_token) {
      return;
    }
    // authentication of JWT token
    const verifyForReturl = async () => { 
      try{
        let retUrl = router.query.retUrl;
        const response = await axios.get('http://localhost:8000/aaa/token', {withCredentials: true}); 
        if (response.data.valid && retUrl) {
          router.push(retUrl);
        } else if (response.data.valid) {
          router.push('/products');
        }
      } catch (error) {
        alert('You have Invalid access token. Please sign-in again.');
      }
    }
    verifyForReturl();
    // if (router.query.retUrl && cookies.access_token) {
    //   router.push(router.query.retUrl);
    // }
    // else if (cookies.access_token) {
    //   router.push('/products');
    // }
  }, [cookies.access_token, router]);

  const [ email, setEmail ] = useState("");
  const [ password, setPassword ] = useState("");
  const [ isInvalid, setIsInvalid ] = useState(false);
  // const [ getToken, setGetToken ] = useState(false);

  const handleEmailChange = ({ target: { value } }) => setEmail(value);
  const handlePasswordChange = ({ target: { value } }) => setPassword(value);
  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('username', email);
    formData.append('password', password);
    try {
      const response = await axios.post('http://localhost:8000/aaa/token',
      formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      // setGetToken(true);
      if (response.status == 200) {
        const accessToken = response.data.access_token;
        const afterOneDay = new Date();
        afterOneDay.setDate(afterOneDay.getDate() + 1);
        setCookie(
          'access_token', 
          accessToken,
          {
            expires: afterOneDay,
          //   secure: true,
          //   httpOnly: true
          }
        );
      }
    } catch (error) {
      if (error.response.status === 401) {
        setIsInvalid(true);
      }
      console.log(error);
    }
  };

  return (
    <Layout>
      <Head>
        <title>Signin</title>
      </Head>
      <div className={styles.signin_container}>
        <main>
          <form className={styles.login_form} onSubmit={handleSubmit}>
            <div className={styles.login_form_items}>
              <input 
                className={styles.login_input} 
                name="email" 
                type="email" 
                onChange={handleEmailChange}
                placeholder="Email" />
            </div>
            <div className={styles.login_form_items}>
              <input 
                className={styles.login_input} 
                name="password" 
                type="password" 
                onChange={handlePasswordChange}
                placeholder="Password" />
            </div>
            <div style={{ 
                display: `${(isInvalid && "block") || "none"}`
            }}>
              You entered wrong email or password, Please try to enter the right email and password!
            </div>
            <div className={`${styles.login_form_items} ${styles.login_content}`}>
              <Link href="/signup">
                <a id={styles.register_button} >
                  <div>
                    Register
                  </div>
                </a>
              </Link>
              <button id={styles.login_button} type="submit">Log-in</button>
            </div>
          </form>
        </main>
      </div>
    </Layout>
  )
}
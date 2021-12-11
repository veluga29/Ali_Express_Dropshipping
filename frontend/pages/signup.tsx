import Link from 'next/link'
import Head from 'next/head'
import { useRouter } from 'next/router'
import Layout from '../src/components/layout'

import { useState } from "react";
import { useEffect } from 'react'
import axios from 'axios';
import { useCookies } from "react-cookie"

export default function Signup() {
  const router = useRouter();
  const [ user, setUser ] = useState({});
  const [ cookies, ,removeCookie ] = useCookies();
  let access_token = cookies.access_token;

  useEffect(() => {
    if (!access_token) {
      return;
    }
    const verifyToken = async () => { 
      try{
        const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/aaa/token`, {
          headers: {
              Authorization: `bearer ${cookies.access_token}`
          }
        }); 
        if (response.data.valid) {
          router.push('/products');
        }
      } catch (error) {
        // Delete access token cookie
        removeCookie('access_token');
      }
    }
    verifyToken();
  })


  const handleChange = ({ target }) => {
    const { name, value } = target;
    setUser({
      ...user,
      [name]: value
    });
  };
  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/me`, user);
      if (response.status == 200) {
        router.push('/signin');
      }
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <Layout>
      <Head>
        <title>Signup</title>
      </Head>
      <div className="container d-flex justify-content-center align-items-center" style={{height: "500px"}}>
        <main>
          <form className="row gy-4" style={{width: "400px"}} onSubmit={handleSubmit}>
            <div>
              <input 
                className="form-control form-control-lg"
                name="email" 
                type="email" 
                onChange={handleChange}
                placeholder="Email" />
            </div>
            <div>
              <input 
                className="form-control form-control-lg"
                name="password" 
                type="password" 
                onChange={handleChange}
                placeholder="Password" />
            </div>
            <div>
              <input 
                className="form-control form-control-lg"
                name="last_name" 
                type="text" 
                onChange={handleChange}
                placeholder="Last name" />
            </div>
            <div>
              <input 
                className="form-control form-control-lg"
                name="first_name" 
                type="text" 
                onChange={handleChange}
                placeholder="First name" />
            </div>
            <div className="d-flex justify-content-between">
              <Link href="/signin">
                <a>
                  <div className="btn btn-danger fs-4">
                    Sign-in
                  </div>
                </a>
              </Link>
              <button className="btn btn-danger fs-4" type="submit">Sign-up</button>
            </div>
          </form>
        </main>
      </div>
    </Layout>
  )
}
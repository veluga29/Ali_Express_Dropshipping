import Link from 'next/link'
import Image from 'next/image'
import { useRouter } from 'next/router'

import { useCookies } from "react-cookie"


export default function Header() {
  const router = useRouter();
  const [cookies, , removeCookie] = useCookies(["access_token"]);
  let access_token = cookies.access_token;

  const handleClickSignout = () => {
    removeCookie('access_token');
    router.push('/signin');
  }

  let dropDownMenu;
  if (router.pathname == "/signin") {
    dropDownMenu = (                    
      <li>
        <Link href="/signup">
          <a className="dropdown-item">Sign-up</a>
        </Link>
      </li>
    )  
  } else if (router.pathname == "/signup") {
    dropDownMenu = (                    
      <li>
        <Link href="/signin">
          <a className="dropdown-item">Sign-in</a>
        </Link>
      </li>
    )  
  } else if (router.pathname == "/aboutus" && !access_token) {
    dropDownMenu = (                    
      <li>
        <Link href="/signin">
          <a className="dropdown-item">Sign-in</a>
        </Link>
      </li>
    )  
  } else {
    dropDownMenu = (
      <li onClick={handleClickSignout}>                  
        <a className="dropdown-item" href="">Sign out</a>                  
      </li>
    )
  }

  return (
    <header className="container-fluid">
      <nav className="navbar navbar-light px-3">
        <Link href="/">
          <a className="navbar-brand">
            <Image 
              src="/images/AED_logo.png"
              height={150}
              width={150}
              alt="Logo of Ali Express Dropshipping"
            />
          </a>
        </Link>
        <ul className="nav">
          <li className="nav-item">
            <Link href="/products">
              <a className="fs-3 btn btn-danger">
                  Products
              </a>
            </Link>
          </li>
          <li className="nav-item">
            <Link href="/aboutus">
              <a className="fs-3 btn btn-danger">
                  About us
              </a>
            </Link>
          </li>
          <li className="nav-item dropdown">          
            <a className="dropdown-toggle fs-3 btn btn-danger" data-bs-toggle="dropdown" role="button" aria-expanded="false">My Info</a>
            <ul className="dropdown-menu">
              {dropDownMenu}
              <li><hr className="dropdown-divider" /></li>
              <li><a className="dropdown-item" href="#">AED service</a></li>              
            </ul>          
          </li>
        </ul>
      </nav>
    </header>
  )
}

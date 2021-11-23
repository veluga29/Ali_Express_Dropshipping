import Link from 'next/link'
import { useRouter } from 'next/router'

import { useCookies } from "react-cookie"


export default function Header() {
  const router = useRouter();
  const [, , removeCookie] = useCookies(["access_token"]);

  const handleClickSignout = () => {
    removeCookie('access_token');
    router.push('/signin');
  }

  return (
    <header className="container-fluid mt-5">
      <nav className="navbar navbar-light bg-light px-3">
        <a className="navbar-brand" href="/">Ali-Express Dropshipping</a>
        <ul className="nav nav-pills">
          <li className="nav-item">
            <Link href="/products">
              <a className="nav-link active fs-3">
                Products
              </a>
            </Link>
          </li>
          <li className="nav-item">
            <Link href="/">
              <a className="nav-link active fs-3">
                About us
              </a>
            </Link>
          </li>
          <li className="nav-item dropdown">
            <a className="nav-link active dropdown-toggle fs-3" data-bs-toggle="dropdown" role="button" aria-expanded="false">My Info</a>
            <ul className="dropdown-menu">
              {router.pathname == "/signin" ? (                    
                <li>
                  <Link href="/signup">
                    <a className="dropdown-item">Sign up</a>
                  </Link>
                </li>) : (
                <li onClick={handleClickSignout}>                  
                  <a className="dropdown-item" href="">Sign out</a>                  
                </li>)
              }
              <li><hr className="dropdown-divider" /></li>
              <li><a className="dropdown-item" href="#">AED service</a></li>              
            </ul>
          </li>
        </ul>
      </nav>
    </header>
  )
}

// export default function Header() {
//   const router = useRouter();

//   return (
//     <header className="container-fluid my-4">
//       <nav className="navbar navbar-expand-lg navbar-light bg-light">
//           <div className="ps-4">
//             <Link href="/">
//               <a className="navbar-brand">
//                 <Image 
//                   src="/images/logo.jpg"
//                   height={100}
//                   width={100}
//                   alt="logo of ali express dropshipping"
//                 />
//               </a>
//             </Link>
//           </div>
//           <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
//             <span className="navbar-toggler-icon"></span>
//           </button>
//           <div className="collapse navbar-collapse offset-8" id="navbarSupportedContent">
//             <ul className="navbar-nav me-auto mb-2 mb-lg-0">
//               <li className="nav-item">
//                 <Link href="/products">
//                   <a className="nav-link active fs-3" aria-current="page">
//                     Products
//                   </a>
//                 </Link>
//               </li>
//               <li className="nav-item">
//                 <Link href="/">
//                   <a className="nav-link active fs-3">
//                     About us
//                   </a>
//                 </Link>
//               </li>
//               <li className="nav-item dropdown">
//                 <a className="nav-link dropdown-toggle active fs-3" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
//                   My Info
//                 </a>
//                 <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
//                   {router.pathname == "/signin" ? (                    
//                     <li>
//                       <Link href="/signup">
//                         <a className="dropdown-item">Sign up</a>
//                       </Link>
//                     </li>) : (
//                     <li>
//                       <Link href="/signup">
//                         <a className="dropdown-item">Sign out</a>
//                       </Link>                    
//                     </li>)
//                   }
//                   <li><hr className="dropdown-divider" /></li>
//                   <li><a className="dropdown-item" href="#">Something else here</a></li>
//                 </ul>
//               </li>              
//             </ul>
//           </div>
//       </nav>
//     </header>
//   )
// }




// export default function Header() {
//   const router = useRouter();

//   return (
//     <header className={styles.header_container}>
//       <div className={styles.logo}>
//         <Link href="/">
//           <a>
//             <Image 
//               src="/images/logo.jpg"
//               height={80}
//               width={80}
//               alt="logo of ali express dropshipping"
//             />
//           </a>
//         </Link>
//       </div>
//       <nav>
//         <ul className={styles.nav_ul}>
//           <li className={styles.nav_li}>
//             <Link href="/products">
//               <a>Products</a>
//             </Link>
//           </li>
//           <li className={styles.nav_li}>
//             <Link href="/">
//               <a>About us</a>
//             </Link>
//           </li>
//           {router.pathname === '/products' &&
//             <li className={styles.nav_li}>
//               <Link href="/signin">
//                 <a>Sign in</a>
//               </Link>
//             </li>
//           }
//         </ul>
//       </nav>
//     </header>
//   )
// }
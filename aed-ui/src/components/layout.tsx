import Header from './header'
import Footer from './footer'
import styles from '/styles/layout.module.css'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className=".container">
      <div className="row">
        <Header />
      </div>
      <div className="row">
        {children}
      </div>
      <div className="row">
        <Footer />
      </div>
    </div>
  )
}

// export default function Layout({ children }: { children: React.ReactNode }) {
//   return (
//     <div className={styles.layout_container}>
//       <div>
//         <Header />
//       </div>
//       <div>{children}</div>
//       <div>
//         <Footer />
//       </div>
//     </div>
//   )
// }
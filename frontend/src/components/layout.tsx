import Header from './header'
import Footer from './footer'
import styles from '/styles/layout.module.css'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div>
      <div className="my-3">
        <Header />
      </div>
      <div className="my-3">
        {children}
      </div>
      <div className="my-3">
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
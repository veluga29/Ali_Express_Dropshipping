import { useState, useEffect } from "react";
import { useCookies } from "react-cookie"
import axios from 'axios';


export default function Pagination({ searchText, totalPages, setProductList }) {
  const [ pageQuotient, setPageQuotient ] = useState(1);
  const [ currentPage, setCurrentPage ] = useState(1);
  const [ cookies ] = useCookies(["access_token"]);
  let access_token = cookies.access_token;

  useEffect(() => {
    setPageQuotient(1)
    setCurrentPage(1)
  }, [totalPages])

  const handleClickPage = async (e) => {
    try {
      const params = { text: searchText, page: e.target.getAttribute('data-value') }
      const headers = {  
        Authorization: `bearer ${access_token}`
      }
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/products/`, { params, headers });
      setProductList(response.data.information.items.slice(0, 12));
      setCurrentPage(Number(e.target.getAttribute('data-value')));
    } catch (error) {
    }
  };
  const handleClickNext = async () => {
    if (pageQuotient + 1 > Math.ceil(totalPages / 5)) {
      return 
    } 
    const nextPage = 1 + 5 * ((pageQuotient + 1) - 1);
    setPageQuotient(prevPageQuotient => prevPageQuotient + 1);
    setCurrentPage(nextPage);
    try {
      const params = { text: searchText, page: nextPage }
      const headers = {  
        Authorization: `bearer ${access_token}`
      }      
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/products/`, { params, headers });      
      setProductList(response.data.information.items.slice(0, 12));
    } catch (error) {
    }
  }
  const handleClickPrevious = async () => {
    if (pageQuotient <= 1) {
      return 
    }
    const prevPage = 5 + 5 * ((pageQuotient - 1) - 1)
    try {
      const params = { text: searchText, page: prevPage }
      const headers = {  
        Authorization: `bearer ${access_token}`
      }
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/products/`, { params, headers });
      setProductList(response.data.information.items.slice(0, 12));
      setPageQuotient(prevPageQuotient => prevPageQuotient - 1)
      setCurrentPage(prevPage)
    } catch (error) {
    }
  }

  const pageIdxs = []
  const skip = 5 * (pageQuotient - 1)
  const limit = (totalPages - skip < 5) ? totalPages - skip : 5
  for (let i = 1; i < limit + 1; i++) {
    pageIdxs.push(i)
  }
  const pageIdxsList = pageIdxs.map((pageIdx) => {
    return (
      <li className="page-item" onClick={handleClickPage} key={pageIdx}>
        <a className={`page-link ${pageIdx % 5 == currentPage % 5 ? "bg-warning text-white"  : "text-secondary"}`} href="#" data-value={ skip + pageIdx }>
          <div>
            { skip + pageIdx }
          </div>
        </a>
      </li>
    )
  })

  return (
    <nav aria-label="Page navigation">
      <ul className="pagination pagination-lg justify-content-center">
        <li className={`page-item ${pageQuotient == 1 ? "disabled"  : ""}`} key="previous" onClick={handleClickPrevious}>
          <a className="page-link" href="#" aria-label="Previous">
            <span className={`${pageQuotient == 1 ? ""  : "text-warning"}`} aria-hidden="true">&laquo;</span>
          </a>
        </li>
        {pageIdxsList}
        <li className={`page-item ${pageQuotient == Math.ceil(totalPages / 5) ? "disabled"  : ""}`} key="next" onClick={handleClickNext}>
          <a className="page-link" href="#" aria-label="Next">
            <span className={`${pageQuotient == Math.ceil(totalPages / 5) ? ""  : "text-warning"}`} aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
  )
}
import axios from 'axios';
import { useEffect, useState } from 'react';
import { useCookies } from 'react-cookie';

export default function Autocomplete({ searchText }) {
  const [ cookies ] = useCookies(["access_token"]);
  let access_token = cookies.access_token;
  let [ textData, setTextData ]= useState([]);
  const autocompleteSearchText = async () => {
    try {
      const params = { search: searchText }
      const headers = {  
        Authorization: `bearer ${access_token}`
      }
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/products/search`, { params, headers});
      setTextData(response.data.items);  // data = response.data.items가 안되는 이유...
    } catch (error) {
    }
  };
  useEffect(() => {
    if (!searchText) {
      return;
    }
    autocompleteSearchText();
  }, [searchText]);

  return (
    <datalist id="datalistOptions">
      { 
        textData && textData.map(({ text }) => {
          return (
            <option key={text} value={text} />
          )
      })
      }
    </datalist> 
  )
}
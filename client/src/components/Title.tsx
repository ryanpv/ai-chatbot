import React from 'react'
import axios from "axios";

type Props = {
  setMessages: any;
}

export default function Title({ setMessages }: Props) {
  const [isResetting, setIsResetting] = React.useState(false);

  // Reset conversation
  const resetConversion = async() => {
    setIsResetting(true);
console.log("");

    await axios.get("http://localhost:8000/reset").then((response) => {
      if (response.status === 200) {
        setMessages([]);
      } else {
        console.error("Error with API request")
      }
    }).catch((error) => {
      console.error(error);
    })

    setIsResetting(false);
  };


  return (
    <div className=''>
      <button onClick={ resetConversion } className='bg-indigo-500 border-2'>RESET</button>
    </div>
  )
}

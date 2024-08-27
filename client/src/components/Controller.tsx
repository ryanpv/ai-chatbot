import { useState } from 'react';
import Title from './Title';
import RecordMessage from './RecordMessage';
import axios from 'axios';

function Controller() {
  const [loading, setLoading] = useState(false);
  const [messages, setMessages] = useState<any[]>([]);

  const createBlobUrl = (data: any) => {
    const blob = new Blob([data], { type: "audio/mpeg" });
    const url = window.URL.createObjectURL(blob);
    return url;
  };

  const handleStop = async(blobUrl: string) => {
    try {
      setLoading(true);
  
      // append recorded message to messages array
      const myMessage = { sender: "me", blobUrl };
      const messagesArr = [...messages, myMessage];
  
      // convert blob url to blob object
      fetch(blobUrl)
        .then((res) => res.blob())
        .then(async (blob) => {
          const formData = new FormData();
          formData.append("file", blob, "myFile.wav");
  
          // Send form data to server
          await axios.post("http://localhost:8000/audio", formData, { 
            headers: { "Content-Type": "audio/mpeg" },
            responseType: "arraybuffer" 
          }).then((res: any) => {
            const blob = res.data
            const audio = new Audio();
            audio.src = createBlobUrl(blob);
  
            const botMessage = { sender: "bot", blobUrl: audio.src };
            messagesArr.push(botMessage);
  
            setMessages(messagesArr);
          }).catch((err) => {
            console.log(err);
          })
  
        });
  
  
      } catch (error) {
        console.log("RECORDING ERROR: ", error);
      } finally {
        setLoading(false);
    }
  };


  return (
    <div className='h-screen overflow-y-hidden'>
      <div>
        <Title setMessages={ setMessages } />
      </div>
      <div className='flex flex-col justify-between h-full overflow-y-scroll pb-96'>

        {/* Recorder  */}
        <div className='fixed bottom-0 w-full py-6 border-t text-center bg-gradient-to-r from-sky-500 to-green-500'>
          <div className='flex justify-center items-center w-full'>
            <RecordMessage handleStop={ handleStop } />
          </div>
        </div>
      </div>
    </div>
  )
}

export default Controller
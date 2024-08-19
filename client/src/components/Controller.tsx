import { useState } from 'react';
import Title from './Title';

function Controller() {
  const [loading, setLoading] = useState(false);
  const [messages, setMessages] = useState<any[]>([]);

  const createBlobUrl = (data: any) => {

    const handleStop = async() => {

    };


  }


  return (
    <div className='h-screen overflow-y-hidden'>
      <div>
        <Title setMessages={ setMessages } />
      </div>
      <div className='flex flex-col justify-between h-full overflow-y-scroll pb-96'>
        Placeholder
      </div>
    </div>
  )
}

export default Controller
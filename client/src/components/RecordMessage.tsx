import { ReactMediaRecorder } from "react-media-recorder";
import RecordIcon from "./RecordIcon";


type Props = {
  handleStop: any;
}

function RecordMessage({ handleStop }: Props) {
  return (
    <ReactMediaRecorder 
      audio 
      onStop={ handleStop } 
      render={ ({ status, startRecording, stopRecording }) => {
        return (
          <div className="mt-2">
            <button 
              onMouseDown={ startRecording } 
              onMouseUp={ stopRecording }
              className="bg-sky-100 p-4 rounded-full shadow-lg"
            >
              <RecordIcon 
                classText={ status === "recording" ? "animate-pulse text-red-500" : "text-sky-500" } 
              />
            </button>
            <p className="mt-2 text-white font-semibold">{ status[0].toUpperCase() + status.slice(1) }</p>
          </div> 
        )
      }
    } 
    />
  )
}

export default RecordMessage
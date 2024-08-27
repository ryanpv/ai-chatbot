import Controller from "./components/Controller"
import { Routes, Route } from "react-router-dom";
import { TestElement } from "./components/TestElement";

function App() {

  return (
    <div>
      {/* <Controller /> */}
      <Routes>
        <Route path="/" element={ <Controller /> } />
        {/* <Route path="/test" element={ <TestElement/> } /> */}
      </Routes>

    </div>
  )
}

export default App

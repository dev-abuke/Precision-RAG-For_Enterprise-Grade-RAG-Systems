import { useState } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div class="flex items-center justify-start mb-4">
      <label class="w-64 flex flex-col items-center px-2 py-2 rounded-lg shadow-lg border border-blue cursor-pointer hover:bg-blue hover:text-white">
        <img class="w-16 h-16" src={"/upload.svg"} alt="Upload" />
        <span class="mt-2 ">Select a Document</span>
        <input type="file" class="hidden" />
      </label>
    </div>
  );
}

export default App;

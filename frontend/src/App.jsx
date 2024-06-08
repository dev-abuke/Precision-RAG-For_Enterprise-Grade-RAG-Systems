import { useState } from "react";
import "./App.css";

import ListPrompt from "./ListPrompt";
import Header from "./Header";
import UploadDoc from "./UploadDoc";

function App() {
  const [question, setQuestion] = useState("When is the deadline for the interim report submission?");
  const [prompts, setPrompts] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  async function onClickGenerate(){
    console.log("Generate clicked :: ", question);
    setIsLoading(true);
    const response = await fetch("http://localhost:5000/generate", {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
      },
      body: JSON.stringify({
          question: question,
      }),
    });

    const data = await response.json();
    console.log("The Generated Data :: ", data);

    setPrompts(data.message);
    setIsLoading(false);
  }

  return (
    <header class="relative">
      <Header />
      <img
        src="https://uploads-ssl.webflow.com/646f65e37fe0275cfb808405/646f66cdeeb4ddfdae25a26e_Background%20Hero.svg"
        alt=""
        class="absolute -z-10 block h-full w-full object-cover"
      />

      <div class="mx-auto w-full px-5 py-16 md:px-10 md:py-24 lg:py-32">
        <div class="mx-auto text-center">
          <h1 class="mb-6 pb-4 text-4xl font-bold text-white md:text-6xl">
            Prompt Generator
            <br />
            and
            <br />
            Evaluator
          </h1>
          <p class="mx-auto mb-5 max-w-[528px] text-xl text-[#636262] lg:mb-8">
            This project enhances business interactions with Language Models
            (LLMs) through automated prompt engineering and evaluation.
          </p>
          <div class="flex mb-8 flex-row justify-center gap-3">
            <div class="p-4 flex-col w-[50%] overflow-hidden bg-white shadow dark:bg-gray-800 sm:rounded-md">
              {/* <div class="mb-10 align-left">
                <label
                  for="helper-text"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white text-left"
                >
                  What do you want to do
                </label>
                <input
                  type="email"
                  id="helper-text"
                  aria-describedby="helper-text-explanation"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Enter what you want to do"
                />
                <p
                  id="helper-text-explanation"
                  class="mt-2 text-sm text-gray-500 dark:text-gray-400 text-left"
                >
                  Could be anything like{" "}
                  <a
                    href="#"
                    class="font-medium text-blue-600 hover:underline dark:text-blue-500"
                  >
                    When is the submission?
                  </a>
                  .
                </p>
              </div> */}
              <UploadDoc/>
              <div class=" align-left">
                <label
                  for="helper-text"
                  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white text-left"
                >
                  What do you want to know about the document?
                </label>
                <input
                  type="text"
                  id="helper-text"
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                  aria-describedby="helper-text-explanation"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Enter what you want to know about the document"
                />
                <p
                  id="helper-text-explanation"
                  class="mt-2 text-sm text-gray-500 dark:text-gray-400 text-left"
                >
                  Could be anything like{" "}
                  <a
                    href="#"
                    class="font-medium text-blue-600 hover:underline dark:text-blue-500"
                  >
                    When is the interim submission?
                  </a>
                  .
                </p>
              </div>
            </div>
            <ListPrompt prompts={prompts}/>
          </div>

          {isLoading ? (
            <a
            class="inline-block rounded-lg w-full bg-gray-200 px-8 py-4 text-center font-bold text-black transition"
          >
            {"Generating...."}
          </a>
          ) : 
          (<a
            onClick={onClickGenerate}
            class="inline-block rounded-lg w-full bg-[#c9fd02] px-8 py-4 text-center font-bold text-black transition hover:border-black hover:bg-white"
          >
            Generate
          </a>)}
        </div>

        <div class="mx-auto mt-16 grid max-w-[1040px] grid-cols-2 gap-8 py-20 sm:grid-cols-3 sm:gap-12 md:grid-cols-5">
          <div class="mx-auto">
            <img
              src="https://uploads-ssl.webflow.com/646f65e37fe0275cfb808405/646f66cdeeb4ddfdae25a267_Microsoft%20Logo.svg"
              alt=""
              class="inline-block"
            />
          </div>
          <div class="mx-auto">
            <img
              src="https://uploads-ssl.webflow.com/646f65e37fe0275cfb808405/646f66cdeeb4ddfdae25a26a_PayPal%20Logo.svg"
              alt=""
              class="inline-block"
            />
          </div>
          <div class="mx-auto">
            <img
              src="https://uploads-ssl.webflow.com/646f65e37fe0275cfb808405/646f66cdeeb4ddfdae25a268_Google%20Logo.svg"
              alt=""
              class="inline-block"
            />
          </div>
          <div class="mx-auto">
            <img
              src="https://uploads-ssl.webflow.com/646f65e37fe0275cfb808405/646f66cdeeb4ddfdae25a269_Chase%20Logo.svg"
              alt=""
              class="inline-block"
            />
          </div>
          <div class="mx-auto">
            <img
              src="https://uploads-ssl.webflow.com/646f65e37fe0275cfb808405/646f66cdeeb4ddfdae25a26b_Walmart%20Logo.svg"
              alt=""
              class="inline-block"
            />
          </div>
        </div>
      </div>
    </header>
  );
}

export default App;

import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <header class="relative">
      <div>
        <nav class="bg-white dark:bg-gray-800  shadow ">
          <div class=" mx-auto max-w-7xl">
            <div class="flex items-center  h-16">
              <div class="w-full justify-between flex items-center">
                <a class="flex-shrink-0" href="/">
                  <img class="w-8 h-8" src={"/rocket.svg"} alt="Workflow" />
                </a>
                <div class="hidden md:block">
                  <div class="flex items-baseline  ">
                    <a
                      class="text-gray-300 px-4 hover:text-gray-800 dark:hover:text-white py-2 rounded-md text-sm font-medium"
                      href="/#"
                    >
                      Generate
                    </a>
                    
                  </div>
                </div>
              </div>
              <div class="flex -mr-2 md:hidden">
                <button class="text-gray-800 dark:text-white hover:text-gray-300 inline-flex items-center justify-center p-2 rounded-md focus:outline-none">
                  <svg
                    width="20"
                    height="20"
                    fill="currentColor"
                    class="w-8 h-8"
                    viewBox="0 0 1792 1792"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path d="M1664 1344v128q0 26-19 45t-45 19h-1408q-26 0-45-19t-19-45v-128q0-26 19-45t45-19h1408q26 0 45 19t19 45zm0-512v128q0 26-19 45t-45 19h-1408q-26 0-45-19t-19-45v-128q0-26 19-45t45-19h1408q26 0 45 19t19 45zm0-512v128q0 26-19 45t-45 19h-1408q-26 0-45-19t-19-45v-128q0-26 19-45t45-19h1408q26 0 45 19t19 45z"></path>
                  </svg>
                </button>
              </div>
            </div>
          </div>
          <div class="md:hidden">
            <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
              <a
                class="text-gray-300 hover:text-gray-800 dark:hover:text-white block px-3 py-2 rounded-md text-base font-medium"
                href="/#"
              >
                Generate
              </a>
              
            </div>
          </div>
        </nav>
      </div>

      <img
        src="https://uploads-ssl.webflow.com/646f65e37fe0275cfb808405/646f66cdeeb4ddfdae25a26e_Background%20Hero.svg"
        alt=""
        class="absolute -z-10 block h-full w-full object-cover"
      />

      <div class="mx-auto w-full max-w-7xl px-5 py-16 md:px-10 md:py-24 lg:py-32">
        <div class="mx-auto max-w-3xl text-center">
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
          <div class="mb-12 align-left">
            <label for="helper-text" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white text-left">What do you want to do</label>
            <input type="email" id="helper-text" aria-describedby="helper-text-explanation" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Enter what you want to do"/>
            <p id="helper-text-explanation" class="mt-2 text-sm text-gray-500 dark:text-gray-400 text-left">Could be anything like <a href="#" class="font-medium text-blue-600 hover:underline dark:text-blue-500">When is the submission?</a>.</p>
          </div>
          <div class="mb-12 align-left">
            <label for="helper-text" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white text-left">How do you want the output</label>
            <input type="email" id="helper-text" aria-describedby="helper-text-explanation" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Enter how you want the ouptput"/>
            <p id="helper-text-explanation" class="mt-2 text-sm text-gray-500 dark:text-gray-400 text-left">Could be anything like <a href="#" class="font-medium text-blue-600 hover:underline dark:text-blue-500">ALL IN CAPITAL</a>.</p>
          </div>
          <a
            href="#"
            class="inline-block rounded-full bg-[#c9fd02] px-8 py-4 text-center font-bold text-black transition hover:border-black hover:bg-white"
          >
            Generate
          </a>
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

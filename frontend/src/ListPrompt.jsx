import { useState } from "react";

function App(props) {

  const prompts = props.prompts

  console.log("The props in List Prompt are :: ",props)

  return (
    <div class="rounded-t  w-[50%] h-full">
      <div class="overflow-hidden bg-white shadow dark:bg-gray-800 sm:rounded-md">
        <ul class="divide-y divide-gray-200">
          {prompts.map((prompt) => (
            <li>
            <a class="block hover:bg-gray-50 dark:hover:bg-gray-900">
              <div class="px-4 py-4 sm:px-6">
                <div class="flex items-center justify-between">
                  <p class="text-gray-700 text-md dark:text-white text-start md:newline">
                    {prompt['prompt']}
                  </p>
                  <div class="flex flex-shrink-0 ml-2">
                  {prompt['accuracy'] > 70 ? 
                  prompt['accuracy'] < 90 ? <p class="inline-flex px-2 text-xs font-semibold leading-5 text-yellow-800 bg-yellow-300 rounded-full">Score : {prompt['accuracy']}</p> :
                   <p class="inline-flex px-2 text-xs font-semibold leading-5 text-green-800 bg-green-300 rounded-full">Score : {prompt['accuracy']}</p>: 
                  <p class="inline-flex px-2 text-xs font-semibold leading-5 text-red-800 bg-red-300 rounded-full"> Score : {prompt['accuracy']}</p>}
                    {/* <p class="inline-flex px-2 text-xs font-semibold leading-5 text-green-800 bg-green-100 rounded-full">
                      Score : {prompt['accuracy']}
                    </p> */}
                  </div>
                </div>
                <div class="mt-2 sm:flex sm:justify-between">
                  <div class="sm:flex">
                    <p class="flex items-center font-light text-gray-500 text-md dark:text-gray-300">
                      Classification: {prompt['classification']}
                    </p>
                  </div>
                </div>
              </div>
            </a>
          </li>
          ))}
          
          {/* <li>
            <a class="block hover:bg-gray-50 dark:hover:bg-gray-900">
              <div class="px-4 py-4 sm:px-6">
                <div class="flex items-center justify-between">
                  <p class="text-gray-700 text-md dark:text-white md:truncate">
                    Increase newsletter subscribers by 500
                  </p>
                  <div class="flex flex-shrink-0 ml-2">
                    <p class="inline-flex px-2 text-xs font-semibold leading-5 text-green-800 bg-green-100 rounded-full">
                      To do
                    </p>
                  </div>
                </div>
                <div class="mt-2 sm:flex sm:justify-between">
                  <div class="sm:flex">
                    <p class="flex items-center font-light text-gray-500 text-md dark:text-gray-300">
                      Jun 14, 2020
                    </p>
                  </div>
                </div>
              </div>
            </a>
          </li>
          <li>
            <a class="block hover:bg-gray-50 dark:hover:bg-gray-900">
              <div class="px-4 py-4 sm:px-6">
                <div class="flex items-center justify-between">
                  <p class="text-gray-700 text-md dark:text-white md:truncate">
                    Increase customer satisfaction rating by 10 points
                  </p>
                  <div class="flex flex-shrink-0 ml-2">
                    <p class="inline-flex px-2 text-xs font-semibold leading-5 text-green-800 bg-green-100 rounded-full">
                      Backlog
                    </p>
                  </div>
                </div>
                <div class="mt-2 sm:flex sm:justify-between">
                  <div class="sm:flex">
                    <p class="flex items-center font-light text-gray-500 text-md dark:text-gray-300">
                      December 10, 2020
                    </p>
                  </div>
                </div>
              </div>
            </a>
          </li> */}
        </ul>
      </div>
    </div>
  );
}

export default App;

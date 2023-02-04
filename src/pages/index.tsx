import { type NextPage } from "next";

const Home: NextPage = () => {
  const uploadFiles = () => {
    console.log("Clicked");
  };

  const decryptFiles = () => {
    console.log("Decrypt");
  };

  return (
    <>
    <div className="relative w-70 h-20 text-white overflow-hidden cursor-pointer transition-all duration-700 card">
      <FrontOfCard />
      <BackOfCard />
    </div>

    <div className="grid grid-cols-4 p-16 bg-slate-600 text-white font-LibreBask">
      <div className="flex flex-col items-center">
        <h2 className="text-xl">Developers</h2>
        <ul>
          <li>
            <a href="https://github.com/Skumbl">
            Jan Arvik
            </a>
          </li>
          <li>
          <a href="https://github.com/Skumbl">
            Jack Savage
            </a>
          </li>
          <li>
          <a href="https://github.com/Skumbl">
            Michael Peters
            </a>
          </li>
          <li>
          <a href="https://github.com/Skumbl">
            Truman DeWalch
            </a>
          </li>
        </ul>
      </div>


      <div className="col-span-2 flex h-screen flex-col items-center">
        <label htmlFor="text-input">Type to encrypt:</label>
        <textarea
          id="text-input"
          cols={30}
          rows={3}
          className="rounded border border-black p-1 text-black"
        />
        <label htmlFor="image-input" className="mt-4">
          Upload an image:
        </label>
        <input type="file" id="image-input" className="mb-4" />

        <button
          onClick={uploadFiles}
          className="rounded-full border border-black bg-white px-4 text-black hover:bg-black hover:text-white"
        >
          Encrypt
        </button>
        <div className="h-1/5" />
        <label htmlFor="decrypt-input">Upload a file to decrypt</label>
        <input type="file" id="decrypt-input" />
        <button
          onClick={decryptFiles}
          className="rounded-full border border-black bg-white px-4 text-black hover:bg-black hover:text-white"
        >
          Decrypt
        </button>
      </div>


      <div className="flex flex-col items-center">
        <h2>Explanation of encryption:</h2>
        {/* TODO: Jan you got this one */}
        <p>TODO</p>
      </div>
    </div>
    </>
  );
};

function FrontOfCard() {
    return (
      <div className="absolute inset-0 w-full h-full flex justify-center items-center font-LibreBaskBold text-3xl bg-gray-900 transition-all duration-100 delay-200 z-20 hover:opacity-0">
        nojjkt_ot_vrgot_yomnz.tech
      </div>
    );
}

function BackOfCard() {
    return (
      <div className="absolute inset-0 w-full h-full flex justify-center items-center font-LibreBaskBold text-3xl bg-gray-800 transition-all z-10 card-back">
        hidden_in_plain_sight.tech
      </div>
    );
}

export default Home;

import { type NextPage } from "next";

const Home: NextPage = () => {
  const uploadFiles = () => {
    console.log("Clicked");
  };

  return (
    <div className="grid grid-cols-4 p-16">
      <div className="flex flex-col items-center">
        <h2>Developers</h2>
        <ul>
          <li>
            Jan Arvik -{" "}
            <a href="#" className="text-blue-600 underline">
              Link
            </a>
          </li>
          <li>
            Jack Savage -{" "}
            <a href="#" className="text-blue-600 underline">
              Link
            </a>
          </li>
          <li>
            Michael Peters -{" "}
            <a href="#" className="text-blue-600 underline">
              Link
            </a>
          </li>
          <li>
            Truman DeWalch -{" "}
            <a href="#" className="text-blue-600 underline">
              Link
            </a>
          </li>
        </ul>
      </div>
      <div className="col-span-2 flex flex-col items-center">
        <label htmlFor="text-input">Type to encrypt:</label>
        <textarea
          id="text-input"
          cols={30}
          rows={3}
          className="rounded border border-black p-1"
        />
        <label htmlFor="image-input" className="mt-4">
          Upload an image:
        </label>
        <input type="file" id="image-input" className="mb-4" />

        <button
          onClick={uploadFiles}
          className="rounded-full border border-black bg-white px-4 text-black hover:bg-black hover:text-white"
        >
          Upload
        </button>
      </div>
      <div className="flex flex-col items-center">
        <h2>Explanation of encryption:</h2>
        {/* TODO: Jan you got this one */}
        <p>TODO</p>
      </div>
    </div>
  );
};

export default Home;

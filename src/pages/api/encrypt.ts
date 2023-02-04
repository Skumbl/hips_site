import { type NextApiHandler } from "next";
import z from "zod";
import { spawn } from "child_process";

const inputSchema = z.object({
  text: z.string(),
  file: z.instanceof(File),
});

type Input = z.infer<typeof inputSchema>;

const handle: NextApiHandler = (req, res) => {
  if (!inputSchema.safeParse(req.body)) {
    res.status(400).json({ message: "Please provide text and a file" });
    return;
  }

  const input = req.body as Input;
  const pythonProcess = spawn("python3", [
    "/src/scripts/script.py",
    input.text,
    input.file.webkitRelativePath,
  ]);
  pythonProcess.stdout.on("data", (data) => {
    //
  });
};

export default handle;

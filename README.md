# H.I.P.S
### hidden in plain sight
HIPS is a web app built using python using the flask framework, and hosted on AWS servers. 
we also built it out as a terminal utilty that can be downloaded using PIP3 and run locally.

## What Inspired Us 
We were inspired about reading about an older hack that hide data inside of sound files.
We thought the idea was cool  but we wanted to do something a bit more interesting, and we wanted to build a utility that was built as a web app.

We also made our domain a fun easter egg

> http://nojjktotvrgotyomnz.tech

its a cypher 

## Story of HIPS
*The issue started with it being a web app :)*

We split our team into 2 parts, the front end and the back end. The front end team built out a web app using next.js and the backend team started building the algorithm using python.

For the first half of the day the two teams worked independenly, it then dawned on us that file management from a serverless web app was not going to work. This meant scrapping the fully built out next.js website.

We then decided to learn on the job and picked up flask and spun up a fiends AWS server. We spent the next 12 hours trouble shooting and banging our heads against the wall, until we finally figured out how both flask and DNS forwarding to Domian we registered.

## The Terminal Tool
The terminal tool we built out which can be found here
> [HIPS terminal tool](https://github.com/Skumbl/hips-hack "HIPS terminal tool")

The server runs this terminal tool on the back end and the website mearly servers the returned data, and parses in the parameters.

The terminal tool can be downloaded and used independently of the site

## The Web App

The web app is built out using a aws ec2 server. And is built on the Flask framework. We went with flask because our encryption algorythim is built in python.
The reason we went with python was ease of access for packages, as well as it being built on C allowing use easy binary manipulation.

We tried using tailwind without a react front-end, but that ended being a real pain, and not something we could work out given the time restraint. So we ended up just using a plain CSS sheet.

## How Encryption Works

One primary challenge of encoding text into images is making sure the image doesn’t look different after being encoded. We accomplished this by taking each individual, red, green, blue value, and changing the last, or least significant bit, to represent a bit in ASCII text. 

We started by doing this on the first X RGB values in the image, X being the number of binary bits required to represent the ASCII message typed in. However, this makes it pretty easy to figure out the encoded text, making the encoding useless. We needed a way to make it much more difficult to decipher the message (without using the decode method), and make the message more secure. 

In order to solve this, we encrypted parts of the message throughout the message by indexing all the R, G, B values and randomly choosing which ones to write parts of the message to. So how will the decode message identify where these randomly chosen locations are (and how much text is stored starting at each one)? Well, after each piece of text (starting at a randomly chosen location), we include 8 zeroes, representing the null terminator string. This tells the decoder to stop reading the current set of encoded bits. But how does it know where these locations actually are? Well, in reverse order at the end of the file we encode the locations of the bits. When decoding, this information is pulled to start decoding the image. 

This stenography tool was packaged into a pip package, which can be installed by any user into their python installation. We used a flask server, running on AWS, as flask is python and can natively run our stenography package. 

# base64decoder [![Build Status](https://travis-ci.org/ltblueberry/base64-decoder.svg?branch=master)](https://travis-ci.org/ltblueberry/base64-decoder)
It's a simple python script that takes specified input file (where base64 supposed to be stored) and decode it to specified output file.

# Make executable
```
chmod a+x base64decoder.py
```

# Usage
```
./base64decoder.py -i [input file] -o [output file]
```
or
```
./base64decoder.py --input [input file] --output [output file]
```

# Example
Let's imagine we have **text.b64** file with next content (*Hello World!* string)
```
SGVsbG8gV29ybGQh
```
We want to decode it to **result.txt** text file. We execute next command
```
./base64decoder.py -i text.b64 -o result.txt
```
And we get result output file.

## License
**[MIT License](LICENSE)**
Copyright (c) 2019 [ltblueberry](https://github.com/ltblueberry)
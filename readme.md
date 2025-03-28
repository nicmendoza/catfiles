# catfiles

`catfiles` is a command-line utility that concatenates the contents of multiple files into a single output file. Each file is prefixed with its path (relative to their shared common directory) and separated by a `---` delimiter.

I use this regularly to feed my LLM of choice a selection of files to consider. Hopefully it's useful


## 📦 Features

- Computes the lowest common ancestor of input files
- Includes each file’s relative path in the output
- Inserts a delimiter (`---`) before each file block
- Preserves original file contents (line endings and formatting)
- Aborts if any input file is invalid
- Optional clipboard output (with `pyperclip`)


## 🛠️ Installation

Clone this repo and install using `pip`:

```
git clone https://github.com/nicmendoza/catfiles.git
cd catfiles
pip install --user .
```

If you’re actively developing it, install in editable mode:

```
pip install --user -e .
```

Make sure your Python user `bin` directory is in your `PATH` (e.g., `~/.local/bin` on Linux/macOS).


## 🚀 Usage

### Clipboard-Only Mode (Default)

By default, `catfiles` will process your files and copy the output to your clipboard without writing any file:

```bash
catfiles file1.txt dir2/file2.txt another/dir/file3.txt
```

### File-Writing Mode

If you want to save the output to a file (in addition to copying it to the clipboard), use the `--write` flag followed by the output file path:

```bash
catfiles --write output.txt file1.txt dir2/file2.txt another/dir/file3.txt

```

### Output Format

```
---
relative/path/to/file1.txt
<contents of file1>

---
relative/path/to/file2.txt
<contents of file2>
```


## ⚠️ Error Handling

- The script will **abort** if any input file does not exist or cannot be read.  
- All paths are resolved **absolutely**, and relative paths in output are based on the common ancestor directory.  


## ✅ Requirements

- Python 3.7+  
- `pyperclip` for clipboard support  


## 📄 License

MIT License
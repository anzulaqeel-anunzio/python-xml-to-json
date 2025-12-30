# XML to JSON Converter

A simple CLI tool to convert XML files into formatted JSON. It handles attributes (prefixed with `@`) and text content effectively.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Zero Dependencies**: Uses Python's standard `xml.etree.ElementTree`.
*   **Structure Preservation**: Maintains hierarchy, attributes, and lists of repeated elements.
*   **Pretty Print**: Outputs readable, indented JSON.

## Usage

```bash
python run_converter.py [file] [options]
```

### Options

*   `--output`, `-o`: Save the result to a JSON file.

### Examples

**1. Convert and Print to Console**
```bash
python run_converter.py data.xml
```

**2. Convert and Save**
```bash
python run_converter.py config.xml -o config.json
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.

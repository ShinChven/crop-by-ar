# Crop-by-AR

A command-line tool to crop images to a specified aspect ratio.

## Installation

### From GitHub

To install the package directly from GitHub, use the following command:

```sh
pip install git+https://github.com/ShinChven/crop-by-ar.git
```

### From Source

1. Clone the repository:
    ```sh
    git clone https://github.com/ShinChven/crop-by-ar.git
    cd crop-cli
    ```

2. Install the dependencies:
    ```sh
    pip install -r src/requirements.txt
    ```

3. Install the CLI tool:
    ```sh
    pip install .
    ```

## Usage

To crop an image or all images in a directory to a specified aspect ratio:

```sh
crop-by-ar <path> <aspect_ratio>
```

- `<path>`: Path to an image file or directory containing images.
- `<aspect_ratio>`: Target aspect ratio in the format `W:H` (e.g., `16:9`).

Example:

```sh
crop-by-ar /path/to/image.jpg 16:9
crop-by-ar /path/to/images_directory 4:3
```

## Updating

To update the package to the latest version from GitHub, use the following command:

```sh
pip install --upgrade git+https://github.com/ShinChven/crop-by-ar.git
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

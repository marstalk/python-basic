# How to Install Python 3 on Mac Using Terminal

To install Python 3 on your Mac using the Terminal, follow these steps:

1. **Open Terminal**: You can open Terminal by searching for it in Spotlight or by navigating to `Applications > Utilities > Terminal`.

2. **Install Homebrew**: Homebrew is a package manager for macOS. If you don't have Homebrew installed, you can install it by running the following command in Terminal:
    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

3. **Install Python 3**: Once Homebrew is installed, you can install Python 3 by running:
    ```sh
    brew install python
    ```

4. **Verify Installation**: After the installation is complete, you can verify that Python 3 is installed by checking the version:
    ```sh
    python3 --version
    ```

You should see the version of Python 3 that was installed.

5. **Set Up Environment**: Optionally, you can set up a virtual environment for your Python projects:
    ```sh
    python3 -m venv myenv
    source myenv/bin/activate
    ```

That's it! You now have Python 3 installed on your Mac.
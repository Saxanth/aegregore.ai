## Installation Instructions
   We are actively seeking improvements to the installation process and will update these instructions as things chage. For now, we work in a windows environment, with plans to support Linux and MacOS in the future.

1. **Install Conda:**
   If you haven't installed Conda yet, you can download it from [Anaconda's official website](https://www.anaconda.com/products/individual). Follow the installation instructions based on your operating system.

2. **Create a New Conda Environment:**
   Open your terminal or command prompt and run the following command to create a new environment named 'aegregore.ai':

    ```powershell
    conda create --name aegregore.ai "python>3.11,<3.12" -y
    ```

3. **Activate the Conda Environment:**
   Activate the environment using the following command (for Windows):

    ```powershell
    conda activate aegregore.ai
    ```

4. **Install Dependencies:**

    Navigate to the directory containing your project and install the required dependencies by running the following command:

    ```powershell
    pip install -r requirements.txt
    ```

    This will install all the necessary python libraries for the application to run smoothly. If you encounter any issues, please ensure that you have the latest version of pip installed and try again. If the problem persists, feel free to reach out for assistance on our [Discord Server](https://discord.gg/Wfdfgkg968).
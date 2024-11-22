The error message indicates that the `tgbot.service` file is not found by `systemctl`. This could be because the service file is not placed in the correct directory. To resolve this, you need to place the `tgbot.service` file in the `/etc/systemd/system/` directory and then reload the systemd daemon.

Here are the steps to do this:

1. Copy the `tgbot.service` file to the `/etc/systemd/system/` directory:
    ```sh
    sudo cp /home/projects/oson_bot/tgbot.service /etc/systemd/system/
    ```

2. Reload the systemd daemon to recognize the new service:
    ```sh
    sudo systemctl daemon-reload
    ```

3. Start the `tgbot.service`:
    ```sh
    sudo systemctl start tgbot.service
    ```

4. Enable the service to start on boot:
    ```sh
    sudo systemctl enable tgbot.service
    ```

This should resolve the issue and allow the `tgbot.service` to start successfully.
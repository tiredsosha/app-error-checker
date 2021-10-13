# Apps error checker

This is Windows lib that compare given image with your Desktop and kills apps which containes in setting file


Plus it logs RAM and OS Uptime

## Installation


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install wheel.

```bash
pip install vr-2.0.0-py3-none-any.whl
```

## Usage
Checkes ram and kills apps if it's high
```
can be changes in configs/settings.yaml

max_ram: 27.0 # must be float
```
Checkes for any error message on the screen in real time
```
put you own error photo in configs/images/ folder and add to configs/settings.yaml
error_name: red.png
```
Add apps that must be terminated in configs/settings.yaml
```
apps:
  - exes.exe
  - OculusClient.exe
```
Add delay between next eteration
```
delay: 60
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



## License
[MIT](https://choosealicense.com/licenses/mit/)

# practice_python

```
python -m venv venv
```

```
venv\Scripts\activate.bat
```

```
pip install -r requirements.txt
```

終了
```
deactivate
```


# 調査中
- gRPC
- webrct
- fraphQL

## vscode settings.json

```
{
    "python.pythonPath": "venv\\Scripts\\python.exe",
    "python.jediEnabled": false,
    "python.autoComplete.extraPaths": [
        "venv\\Lib\\site-packages"
    ],
    "python.languageServer": "Microsoft"
}
```
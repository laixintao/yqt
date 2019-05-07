# Yu Que Tools

A command line tools for yuque.com.

## Install 

```
pip install yqt
```

## Usage

1. Get a token from https://yuque.com/settings/tokens
2. `export YUQUE_TOKEN=your-token`
3. `yqt filename.md`

File format:

```
https://yuque.com/me/kzzkgl/asdfas

# Title

you content here...
```

- The first line must be url to sync to.
- The next none blank line will be doc's title.

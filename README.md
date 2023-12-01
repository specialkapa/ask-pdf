# README

This is a proof of concept repository for querying `pdf` files. It allows the 
user to interrogate a `pdf` file on the CLI and returns a response in the CLI. 

# Pre-requisites 

1. You will need `python` 3.11 or greater.
2. You will need `pipx`. Install it using the following commands in your CLI.

```PowerShell
> py -3 -m pip install --user pipx
> py -3 -m pipx ensurepath
```
3. You will need `poetry`. Install it using the following commands in your CLI.

```PowerShell
> pipx install poetry
> poetry config virtualenvs.in-project = true
```

4. You will need to use your `openai` API key. For now set it as an environment 
   variable through your CLI. For some reason using `.env` file along with 
   `python-dotenv` does not work. 

```PowerShell
>$end:$env:OPENAI_API_KEY="your-key-here"
```

> **Note**: All the CLi commands stated assume you are `Windows` with `PowerShell`.

# Installation 

Use the following command in your CLI.

```PowerShell
poetry install
```

# Environment activation

Use the following command in your CLI.

```PowerShell
poetry shell
```

# Use instructions

In your CLI do the following. 


```PowerShell
askpdf --file "<path-to-pdf-file>" --question "Your question here"
# or use abbreviations
askpdf -f "<path-to-pdf-file>" -q "Your question here"
# if you ommit the --f parameter then the sample pdf file in this repository 
# will be used
askpdf -q "Your question here"
# get help 
askpdf -h
askpdf --help 
```

# TODOs
- [ ] Fix issue with `openai` API KEY not being recognised when using `python-dotenv`
  along with a .env file. 
- [ ] Use local large language model rather than sending requests to `openai`. 


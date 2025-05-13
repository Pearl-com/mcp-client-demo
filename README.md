# MCP Client Demo

This Python sample shows how to use the Pearl [MCP server](https://www.pearl.com/post/bridge-your-ai-agents-to-human-experts-fast) with the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/). The sample gets an AI answer to a legal question and then a second opinion from a human lawyer. The MCP server supports lawyers, doctors, mechanics, veternarians, tech support and hundreds of other professional specialties. You can verify information and directly interact wtih professionals via MCP or REST API. 

To get started create a virtual environment and install the Agents SDK:

```
pip install openai-agents
```

Your OpenAI API key should be set in an environment variable called OPENAI_API_KEY (or modify the code to pass this directly). You also need a Pearl API Key, which you can obtain [here](https://www.pearl.com/contact).


# Best practices for using the experimental Amazon Bedrock Runtime client for Python<a name="best-practices"></a>

The following are best practices for using the experimental Amazon Bedrock Runtime client for Python. 

## Reuse SDK clients when possible<a name="bp-reuseClient"></a>

Depending on how an SDK client is constructed, creating a new client may result in each client maintaining its own HTTP connection pools, identity caches, and so on. We recommend sharing a client when possible to avoid the overhead of expensive resource creation. 

## Use virtual environments<a name="bp-virtualEnvironments"></a>

This is a general Python development recommendation, but it's a good one that bears repeating. It's good to use a separate [virtual environment](https://docs.python.org/3/library/venv.html) for every project you work on. This helps to maintain version compatibility with your dependencies without risking breaking other applications using the same libraries and packages.
from langserve import RemoteRunnable

remote_chain = RemoteRunnable('http://localhost:8000/chain/')

response = remote_chain.invoke({"language": "japanese", "text": "I am Jose. Nice to meet you!"})

print(response)
[] Determine cost for resource usage    
[] Determine currency for resource providers
[] Secure currency via web3 transaction ledger

* every provider should charge the same based on the resource requested
* every provider should be credited the same based on the resource provided
* every provider will have a single login solution, this login solution will be useable for every 'node' they provide to the network.
* every node must supply atleast 'embeding' resources to the network. Luckily embedding is fast (gpu or cpu)
* providers that provide faster resources, will be utilized more often (allowing for the accural of credits).
* providers should be credited as soon as it's possible to verify the transaction, because of the verification process, it may take time before the credits are recieved.

** Embedding **
    The price for embedding should be consistent accross 'available models'. The plan is to cache all embedding (the cost will still apply (ie. Embedding cost)), so a cached result is quicker. A provider can choose to provide any embedding model they like, however they must provide atleast 'nomic-embedding' and cache embedding results Retrieved cache embedding will yield far less (0.01c / billion tokens) credits for the provider.

** Storage **
    Storage is a unique cost/credit situation. Since storage will be distributed, it's imparitive that we can 'get' / 'store' data in a distributed way. I think that we should 'credit' a provider for 'storage' space, at the going rate (5.35e-5 / GB / day), however we will need to determine 'how to validate' the work that was providing storage to other users. 

    *Note - we can credit the provider based on the amount of data they served to other nodes. ie. If they are storing 10GB and serve 200KB, they will recieve a portion of their storage cost. However if they provide 10GB or more, they will recieve the full credit for their contribution (ie, 1.5c) this may be paid out daily. This also means that we need to keep track of 'data rates' outgoing data rates and have ledger verification.

** Code Generation **
-- [todo] --

** Image Generation **
-- [todo] --

** Chat/Text Generation **
-- [todo] --
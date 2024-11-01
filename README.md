# Decentralized AI Content Generation Project

## Overview
This project focuses on deserializing AI-generated content in various forms such as chat, text to speech, text to image, text to video, image to image, image to video, and image summarization. The project utilizes SurrealDB as the datastore and Libp2p as the decentralized peer networking framework to ensure data security, availability, and scalability. The idea of this project is to spread resources across a network of peers, allowing for efficient resource management, load balancing, and improved performance for the network.

The entire system works on a credit system, the more resources you allow on the network, the more credits you receive. These credits can be used to use other nodes resources in the network. This ensures that all nodes are incentivized to contribute to the network and share their resources with others. Additionally, the project includes a decentralized generative caching system to optimize resource usage and improve performance for the network. You have the ability to opt-in to specific resource sharing, allowing you to choose which resources you want to make available to other nodes in the network.

## Features
- Decentralized storage and retrieval of AI-generated content using SurrealDB and Libp2p
- Decentralized generative caching system to optimize resource usage and improve performance for the network
- Decentralized content generation and distribution using a peer-to-peer network
- Support for various forms of AI-generated content such as chat, text to speech, text to image, text to video, image to image, image to video, and image summarization
- Scalable and efficient data processing and management using SurrealDB and Libp2p
- Secure and private data transmission and storage using end-to-end encryption and decentralized peer networking
- Resource scalability and load balancing using a distributed network of peers
- Credit based contribution and resource sharing system to incentivize nodes to contribute to the network and share their resources with others

## Technologies Used
Our dependency list is exhuastive and we recommend installing all of them to ensure the project runs smoothly. However, if you're experiencing issues with installation, try installing only the necessary dependencies for your specific use case. Here are some common ones:

[Surrealdb](https://surrealdb.com/docs/install) - A scalable, distributed, transactional, and embeddable database for the realtime web.

[libP2P](https://libp2p.io/) - The modular peer-to-peer networking stack that enables Web3.

[FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints

[ELL](https://github.com/MadcowD/ell) - A lightweight, functional prompt engineering framework

[PyTorch](https://pytorch.org/get-started/locally/) - An open source machine learning framework that accelerates the path from research prototyping to production deployment. 
    - We recommend using pytorch with cuda support for faster training and inference.

[Lightning.AI](https://lightning.ai/docs/pytorch/stable/installation.html) - The most intuitive and scalable way to train PyTorch models and researchers

[LLamaParse](https://docs.llamaindex.ai/en/stable/module_guides/loading/connector/llama_parse/) - Building applications with LLMs through composability. LangChain provides an easy-to-use interface for developing applications powered by language models. Additionally, the Langchain expression language (LCEL) provides a powerful way to combine prompts and chains.

[Transformers](https://huggingface.co/docs/transformers/installation) - State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX. \[Optional\] If you want to use GPU for training, please install Transformers with CUDA support. You can find installation instructions [here](https://huggingface.co/docs/transformers/installation).

[Diffusion](https://github.com/huggingface/diffusers) - State-of-the-art diffusion models for image and audio generation in PyTorch. 
\[Optional\] If you want to use GPU for training, please install Diffusion with CUDA support. You can find installation instructions [here](https://github.com/huggingface/diffusers).

[Sentence Transformers](https://www.sbert.net/) - Sentence Embeddings using BERT / RoBERTa / XLM-R / DistilBERT / MiniLM / T5 / MPNet / etc. 100+ pretrained models!

[Pydantic](https://docs.pydantic.dev/) - Data validation using Python type hints\[Optional\] If you want to use GPU for training, please install Pydantic with CUDA support. You can find installation instructions [here](https://docs.pydantic.dev/).  

[Hydra](https://hydra.cc/) - A framework for elegantly configuring complex applications. It works with any scale of the application and provides a unified configuration interface. \[Optional\] If you want to use GPU for training, please install Hydra with CUDA support. You can find installation instructions [here](https://hydra.cc/).

## Community
Join our community to stay updated on the latest developments, ask questions, and share your ideas. We have a discord server where you can connect with other contributors, users, and enthusiasts. 

discord: https://discord.gg/Wfdfgkg968

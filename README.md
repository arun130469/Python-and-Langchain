
# Syllabus

# Session 1 :Python Brush-Up and Setup

---

### 1.1. Introduction to Python

#### 1.1.1 Python Overview (10 minutes)
- **Wide Range of Applications:**
  - Web Development, Data Science, Automation, Game Development, Desktop Applications.
- **Career Opportunities:**
  - Roles such as Python Developer, Data Scientist, Automation Engineer.
- **Extensive Libraries and Frameworks:**
  - Overview of Python's standard library and popular third-party libraries.
- **Integration Capabilities:**
  - Integrating Python with other languages and platforms (e.g., C/C++, Java, .NET).

#### 1.1.2 Implementations of Python (20 minutes)
- **CPython:** The default implementation of Python.
- **Jython:** Python for the Java platform.
- **IronPython:** Python for the .NET framework.
- **PyPy:** A faster implementation of Python with JIT compilation.
- **Python.NET:** Embedding Python in .NET applications.

---

### 1.2. Setting Up the Python Development Environment

#### 1.2.1 Development Tools Overview (10 minutes)
- **IDLE:** Integrated Development and Learning Environment.
- **Codespace setup** 
- **Jupyter notebook:**
  - Setting up Jupyter notebooks.
  - Writing and executing Python code in notebooks.

---

### 1.3. Python Language Fundamentals

#### 1.3.1 Basic Syntax Rules (10 minutes)
- Indentation, variables, and comments.
- Naming conventions.

#### 1.3.2 Variables, Data Types, and Type Conversion (15 minutes)
- Working with different data types (int, float, string, etc.).
- Type conversion and casting.

#### 1.3.3 Input and Output (10 minutes)
- Reading user input.
- Formatting and printing output.

---

### 1.4. Control Structures and Operations

#### 1.4.1 Conditional Statements (15 minutes)
- `if`, `elif`, `else` constructs.

#### 1.4.2 Operators (15 minutes)
- Arithmetic, comparison, logical, and bitwise operators.

#### 1.4.3 Strings and String Manipulation (30 minutes)
- Strings as read-only arrays
- String concatenation
- String internal representation
- Interning ( Implicit Interning, Explicit Interning )
- String methods
- F-Strings for formatting strings.
- Replacement Field {} specification.
- The optional conversion operators “!”, ":".
- Fill + Align + Sign+Width.
- Grouping Options.
- The 0 (zero) Character
- Presentation Types & the character #

#### 1.4.4 Data Structures: 
##### Container Tyes
  - Sequences (Strings, Tuples, Bytes, Lists and ByteArrays)
  - Sets ( set(), frozenset() )
  - Mapping
##### **List :
- Working ( memory allocation )
- List Methods
- List Comprehension
##### **Tuples
- Packing and unpacking tuples
- Returning tuple from a function
- Copying a tuple
- Reversing a Tuple
- Comparing Tuples
- Loop a tuple
- Tuple in memory
##### **Sets 
- Set functions
- Set Methods
- Frozenset
##### **Dictionaries
- Using tuples as keys
- Create using dict comprehension
- Dictionary methods
- Loop over a dict


#### 1.4.5 Control Structures: Advanced Loops and Conditionals 
- For loop, while loop, do while
- Range, Break and Continue
- Nested loops, comprehensions, and conditionals.
- Working with complex logical conditions.

#### 1.4.6 Variable Scopes 
- Namespaces: understanding them as dictionaries
- Scopes
- Local, global, and nonlocal variables.
- Scope resolution and the `global` keyword.

---

### 1.5. Functions and Modules

#### 1.5.1 Functions: Arguments, Return Values, and Lambda Functions (20 minutes)
- Defining functions, passing arguments, and returning values.
- Process Map of a program.
- Formal vs. Actual Parameters
- Annotations
- Positional and Keyword Arguments
- Variable number of arguments
- Function object (__globals__, __name__, __class__, __call__, etc.)
- Anonymous functions with `lambda`.

#### 1.5.2 Working with Files 
- Reading and writing files.
- Working with different file formats.

#### 1.5.3 Exception Handling 
- Handling Exceptions
- Getting the instance of the Exception
- Raising Exceptions
- Another way to get the instance of the Exception
- Nesting Try…Except
- try-except-else
- User Defined Exceptions
- The finally block

#### 1.5.4 Collections Module 
- Using specialized container datatypes like `defaultdict`, `deque`, `Counter`, etc.

#### 1.5.5 Modules and Packages 
- Creating and importing custom modules.
- Understanding Python packages and namespaces.
- Variations of import statement.
- How are modules loaded?

---
# Session 2 : object-oriented programming and introduction to usecases in python
### 2.1 Object-Oriented Programming in Python

#### 2.1.1 Classes and Objects 
- Class vs. Functions
- Data Attributes of Classes
- Function Object vs Method Object
- Bound Method Object vs Function Object
- Initial State of a Class
- Play around with Class’s __init__
- What about __init__ on instance object
- Calling methods/functions within an instance or a class.
- Creating classes dynamically.
- Metaclass
- 

#### 2.1.2 Inheritance 
- Single and multiple inheritance.
- Overriding methods.
- Check instance and class inheritance.

#### 2.1.3 Polymorphism 
- Polymorphic functions and operator overloading.

#### 2.1.4 Encapsulation and Abstraction 
- Using private and protected members.
- Abstract base classes.

#### 2.1.5 Magic Methods and Operator Overloading
- Special methods like `__init__`, `__str__`, `__len__`, and custom operator overloading.
- Static Method
- Class Method
- Nuances about Instance Methods
- Class super
- Private Attributes

---

### 2.2 Advanced Python Concepts

#### 2.2.1 Iterators and Generators 
- Implementing custom iterators.
- Using generators for lazy evaluation.

#### 2.2.2 Decorators 
- Creating and using decorators to modify function behavior.

#### 2.2.3 Context Managers 
- Using `with` statements and implementing custom context managers.

#### 2.2.4 Multithreading and Multiprocessing 
- Basics of parallel processing.
- Working with the `threading` and `multiprocessing` modules.

#### 2.2.5 Asyncio for Asynchronous Programming 
- Introduction to asynchronous programming in Python.
- Using `async` and `await` for non-blocking code.

---

### 2.3 Working with External Libraries

#### 2.3.1 Installing Packages with pip 
- Installing and managing external libraries.

#### 2.3.2 Data Analysis with pandas 
- Introduction to `pandas` for data manipulation.

#### 2.3.3 Web Scraping with BeautifulSoup and requests 
- Extracting data from websites.
- Handling HTTP requests.

#### 2.3.4 Working with APIs 
- Making API calls and handling responses.

---

### 2.4 Testing and Debugging

#### 2.4.1 Debugging in Python 
- Using debugging tools (`pdb`, breakpoints).

#### 2.4.2 Unit Testing 
- Writing and running tests with `unittest`.

#### 2.4.3 Test-Driven Development (TDD) 
- Introduction to TDD practices.

#### 2.4.4 Continuous Integration (CI) Basics 
- Setting up CI for automated testing.

---

### 2.5 Python in Practical Applications

#### 2.5.1 Python for Data Science and Machine Learning 
- **Introduction to NumPy:**
  - Basics of numerical operations with `NumPy`.
- **Data Visualization with Matplotlib and Seaborn:**
  - Creating visualizations for data analysis.
- **Introduction to scikit-learn:**
  - Basic machine learning tasks.

#### 2.5.2 Python for Web Development
- **Introduction to Flask:**
  - Building a simple web application.
- **Introduction to Django:**
  - Overview of Django for full-stack development.
- **Working with Databases:**
  - Basic database operations using `SQLAlchemy` or Django ORM.

#### 2.5.3 Python in DevOps 
- **Automation with Python:**
  - Writing scripts for task automation.
- **Python and Docker:**
  - Creating Docker containers for Python applications.
- **Working with Cloud Services:**
  - Using Python with cloud platforms like AWS, Azure.

---

### 2.6 Summary and Q&A (20 minutes)
- Recap of the key topics covered in the session.
- Open floor for questions and clarification.
---
---

# **Session 3: Introduction to LangChain and Prompting Techniques**

**Duration:** 4-5 hours

---

#### **3.1 Introduction to LangChain (30-45 minutes)**

- **3.1.1 Overview of LangChain:**
  - What is LangChain and why use it?
  - Key concepts: Chains, Agents, Prompts, and LLMs (Large Language Models).
  - Use cases: Applications in AI-driven workflows (text generation, Q&A systems, conversation agents, etc.).

- **3.1.2 Understanding LangChain Components:**
  - Chains: Connecting various LLMs for complex tasks.
  - Agents: Dynamic decision-makers that use chains.
  - Prompts: Inputs that guide LLMs toward desired outputs.
  - Models: Types of LLMs that LangChain can interface with.

- **3.1.3 Hands-On Activity: Setting Up a LangChain Project (15 minutes)**
  - Step-by-step guide to setting up a new LangChain project environment.
  - Installing necessary packages and dependencies.
  - Configuring API keys and services (e.g., OpenAI, Cohere).

#### **3.2 Demo: Creating a Simple Chain to Connect Multiple LLMs (30-45 minutes)**

- **3.2.1 Creating a Simple Chain:**
  - Understanding the flow of data between multiple LLMs.
  - Building a basic chain to connect two or more LLMs for sequential tasks.
  - Practical example: Constructing a chain for content summarization followed by text generation.

- **3.2.2 Hands-On Exercise: Implementing a Basic Chain (20 minutes)**
  - Participants create a simple chain using the LangChain library.
  - Experiment with chaining different LLMs to handle tasks like translating text, generating summaries, and creating questions.

#### **3.3 Introduction to Prompting Techniques (45 minutes - 1 hour)**

- **3.3.1 Foundations of Prompting:**
  - What are prompts and why are they crucial?
  - Key elements of an effective prompt: Context, Instructions, and Expected Output.
  - Different types of prompts: Text generation, Q&A, summarization, data extraction, etc.

- **3.3.2 Hands-On Exercise: Writing Effective Prompts (30 minutes)**
  - Practice writing prompts for various tasks:
    - Text generation: Crafting creative and informative content.
    - Q&A: Designing prompts for factual responses.
    - Summarization: Creating prompts for concise summaries.
  - Participants refine prompts through trial and error with different models.

- **3.3.3 Demo: Testing and Refining Prompts with Different Models (15 minutes)**
  - Demonstration of how different models respond to various prompt types.
  - Techniques to adjust prompts for better performance and accuracy.
  - Using prompt tuning methods to handle ambiguous or complex tasks.

#### **3.4 Advanced Prompt Engineering (1 - 1.5 hours)**

- **3.4.1 Advanced Techniques in Prompt Design:**
  - Overview of few-shot learning: Using multiple examples in prompts to guide LLMs.
  - Context management: Maintaining relevance and coherence in multi-turn conversations.
  - Handling user-specific and context-specific nuances.

- **3.4.2 Hands-On Activity: Implementing Few-shot Learning and Context Management (45 minutes)**
  - Participants implement few-shot learning prompts for specific tasks (e.g., text classification, decision making).
  - Practice techniques to manage context in long conversations or multi-turn dialogues.

#### **3.5 Demo: Building a Context-Aware Conversation Agent (30-45 minutes)**

- **3.5.1 Creating a Context-Aware Agent:**
  - Combining chains, agents, and prompts for dynamic interactions.
  - Designing an agent that adapts responses based on conversation history and context.
  - Key challenges: Memory management, avoiding repetition, maintaining engagement.

- **3.5.2 Live Demo: Context-Aware Agent in Action (20 minutes)**
  - Showcasing a conversation agent that uses advanced prompt engineering to handle various user inputs.
  - Discussing real-world applications of context-aware agents (customer service bots, virtual assistants, etc.).

- **3.5.3 Q&A and Wrap-up (10-15 minutes):**
  - Open floor for questions, clarifications, and discussions.
  - Summary of key takeaways and additional resources for further learning.

---
---

# **Session 4: Embedding and Vector Databases**

**Duration:** 4-5 hours

---

#### **4.1 Understanding Embeddings (45 minutes - 1 hour)**

- **4.1.1 Overview of Embeddings:**
  - What are embeddings and their role in Natural Language Processing (NLP)?
  - Types of embeddings: Word2Vec, GloVe, BERT, Sentence Transformers, etc.
  - Applications of embeddings in various NLP tasks (text similarity, clustering, classification).

- **4.1.2 Hands-On Activity: Generating Embeddings Using Different Models (30 minutes)**
  - Generate embeddings using BERT, Sentence Transformers, and other popular models.
  - Practical example: Embedding sentences, paragraphs, and documents.
  - Comparing the embeddings generated by different models.

- **4.1.3 Demo: Visualizing Embeddings and Understanding Their Structure (15 minutes)**
  - Visualizing high-dimensional embeddings using techniques like PCA (Principal Component Analysis) and t-SNE (t-Distributed Stochastic Neighbor Embedding).
  - Interpreting embedding clusters and distances.

#### **4.2 Introduction to Vector Databases (30-45 minutes)**

- **4.2.1 Overview of Vector Databases:**
  - What are vector databases, and why use them?
  - Key concepts: Vector similarity, approximate nearest neighbors (ANN), indexing.
  - Commonly used vector databases: Pinecone, FAISS, Milvus, etc.

- **4.2.2 Hands-On Activity: Setting Up a Vector Database (30 minutes)**
  - Step-by-step guide to setting up a vector database like Pinecone or FAISS.
  - Basic configuration and connection to your Python environment.

- **4.2.3 Demo: Storing and Retrieving Data Using Embeddings (15 minutes)**
  - Storing embeddings in a vector database.
  - Performing simple retrieval tasks using vector similarity search.
  - Practical example: Finding similar documents or sentences.

#### **4.3 Practical Use Cases (1 - 1.5 hours)**

- **4.3.1 Implementing a Simple Search Engine Using Embeddings and Vector Databases (45 minutes)**
  - Building a search engine that leverages embeddings for similarity-based searches.
  - End-to-end implementation: Data preprocessing, embedding generation, storing, and searching.

- **4.3.2 Demo: Scaling Up the Search with More Complex Queries and Datasets (30 minutes)**
  - Handling larger datasets and optimizing for performance.
  - Demonstrating complex search queries: Multi-vector searches, filtering, and ranking.
  - Real-world use cases: Semantic search, recommendation systems, and clustering.

#### **4.4 Q&A and Wrap-up (10-15 minutes)**

- **4.4.1 Open Floor for Questions, Clarifications, and Discussions:**
  - Addressing participant queries and providing additional insights.
  - Discussing challenges and best practices when working with embeddings and vector databases.

- **4.4.2 Summary of Key Takeaways and Additional Resources:**
  - Recap of key concepts covered in the session.
  - Providing resources for further learning (articles, tutorials, documentation).

---
---

# **Session 5: Retrieval-Augmented Generation (RAG)**

**Duration:** 5-6 hours

---

#### **5.1 Introduction to RAG (45 minutes - 1 hour)**

- **5.1.1 Overview of Retrieval-Augmented Generation (RAG):**
  - What is RAG, and why use it?
  - Key components of RAG: Knowledge retrieval and generation.
  - Applications of RAG in real-world scenarios (question answering, document retrieval, personalized chatbots).

- **5.1.2 Hands-On Activity: Building a Basic RAG System Using Python (30-45 minutes)**
  - Step-by-step guide to implementing a simple RAG system.
  - Using Python libraries and frameworks (e.g., PyTorch, Hugging Face Transformers) to create a basic RAG model.
  - Integrating a pre-trained language model with a knowledge retrieval module.

- **5.1.3 Demo: Integrating Embeddings and Vector Databases for Knowledge Retrieval (15 minutes)**
  - Demonstrating how embeddings and vector databases (e.g., Pinecone, FAISS) are used in the retrieval component of a RAG system.
  - Practical example: Retrieving relevant documents or context for a given query.

#### **5.2 Data Preparation for RAG (1 - 1.5 hours)**

- **5.2.1 Importance of Data Preparation in RAG:**
  - Why data preparation is crucial for effective RAG systems.
  - Types of data needed for RAG: Structured vs. unstructured data.
  - Key considerations: Data quality, relevance, and diversity.

- **5.2.2 Hands-On Activity: Preparing and Cleaning Data for Embedding and Storage (45 minutes)**
  - Techniques for data cleaning and preprocessing (e.g., removing noise, normalizing text).
  - Preparing data for embedding generation: Tokenization, formatting, and embedding techniques.
  - Storing data in vector databases for fast retrieval.

- **5.2.3 Demo: Optimizing Data Storage for Fast Retrieval (15-20 minutes)**
  - Demonstration of techniques for optimizing data storage in vector databases.
  - Indexing strategies for faster search and retrieval.
  - Practical example: Setting up a highly performant retrieval system.

#### **5.3 Advanced RAG Scenarios (2 - 2.5 hours)**

- **5.3.1 Overview of Advanced RAG Scenarios:**
  - Different use cases and scenarios for advanced RAG applications.
  - Examples: Document retrieval, personalized response generation, domain-specific knowledge augmentation.

- **5.3.2 Hands-On Activity: Implementing Different RAG Scenarios (1 - 1.5 hours)**
  - Building RAG systems for specific use cases:
    - Document retrieval: Finding and generating summaries from large datasets.
    - Personalized responses: Tailoring responses based on user profiles or preferences.
  - Configuring retrieval modules and generation models for specific tasks.

- **5.3.3 Demo: Fine-Tuning RAG Models for Specific Tasks (30-45 minutes)**
  - Demonstrating how to fine-tune a RAG model for a particular task or domain.
  - Using domain-specific data to improve retrieval and generation performance.
  - Practical example: Fine-tuning a RAG model for customer support or medical consultation.

#### **5.4 Q&A and Wrap-up (15-20 minutes)**

- **5.4.1 Open Floor for Questions, Clarifications, and Discussions:**
  - Addressing participant queries and providing additional insights.
  - Discussing challenges and best practices when working with RAG systems.

- **5.4.2 Summary of Key Takeaways and Additional Resources:**
  - Recap of key concepts covered in the session.
  - Providing resources for further learning (articles, tutorials, documentation).
---
---




# **Session 6: Agents, Workflows, and Automation**

**Duration:** 5-6 hours

---

#### **6.1 Introduction to Agents (45 minutes - 1 hour)**

- **6.1.1 Overview of Agents:**
  - What are agents in the context of LangChain and AI-driven systems?
  - Types of agents: Task-oriented, conversational, and reactive agents.
  - Use cases: Automating tasks, decision-making, and handling complex workflows.

- **6.1.2 Hands-On Activity: Building Simple Agents Using LangChain (30-45 minutes)**
  - Step-by-step guide to creating a simple agent using the LangChain library.
  - Defining agent behaviors: How agents perceive inputs and make decisions.
  - Practical example: Building an agent to automate simple tasks like scheduling or data retrieval.

- **6.1.3 Demo: Integrating Agents with External APIs for Task Automation (15 minutes)**
  - Demonstration of integrating agents with external APIs (e.g., weather data, email services).
  - Practical example: Automating email notifications based on data changes or external triggers.

#### **6.2 Workflow Automation (1 - 1.5 hours)**

- **6.2.1 Overview of Workflow Automation:**
  - What is workflow automation, and why is it important?
  - Key components: Triggers, actions, conditions, and agents.
  - Use cases: Streamlining business processes, reducing manual intervention, and improving efficiency.

- **6.2.2 Hands-On Activity: Designing and Implementing Workflows Using Python (45 minutes)**
  - Building a workflow from scratch using Python and LangChain.
  - Practical examples: Automating repetitive tasks, such as data processing or report generation.
  - Incorporating agents to handle decision-making within workflows.

- **6.2.3 Demo: Automating Complex Tasks with Agents and Chains (30 minutes)**
  - Demonstration of automating a complex, multi-step task using agents and chains.
  - Real-world example: Automating a data pipeline or customer onboarding process.

#### **6.3 Advanced Automation Techniques (2 - 2.5 hours)**

- **6.3.1 Advanced Techniques in Automation:**
  - Overview of advanced automation methods: Error handling, logging, and monitoring.
  - Best practices for robust and scalable automation.

- **6.3.2 Hands-On Activity: Implementing Error Handling, Logging, and Monitoring in Workflows (1 - 1.5 hours)**
  - Techniques for adding error handling and logging to workflows.
  - Implementing monitoring tools to track workflow performance and detect issues.
  - Practical example: Creating a robust automation system that handles failures gracefully.

- **6.3.3 Demo: Deploying a Fully Automated System with Real-World Applications (30-45 minutes)**
  - Demonstrating the deployment of an end-to-end automated system.
  - Real-world application examples: Customer service bots, automated reporting systems, and AI-driven decision-making.

#### **6.4 Q&A and Wrap-up (15-20 minutes)**

- **6.4.1 Open Floor for Questions, Clarifications, and Discussions:**
  - Addressing participant queries and providing additional insights.
  - Discussing challenges and best practices in building agents, workflows, and automation.

- **6.4.2 Summary of Key Takeaways and Additional Resources:**
  - Recap of key concepts covered in the session.
  - Providing resources for further learning (articles, tutorials, documentation).

---
---




<hr>
# Setting Up and Using Jupyter Notebooks in GitHub Codespace

This guide provides step-by-step instructions for setting up and using Jupyter notebooks within a GitHub Codespace.

## 1. Open Your Codespace

- Start by creating or opening a Codespace from your GitHub repository.

## 2. Install Jupyter Notebook

If Jupyter is not already installed in your Codespace, you'll need to install it:

```bash
pip install notebook
```

## 3. Create a New Jupyter Notebook
To create a new Jupyter notebook:
1. Open the command palette in CodeSpace by pressing `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS).
2. Type `Jupyter: Create New Blank Notebook` and select it from the options.
3. Choose the kernel you want to use for the notebook (e.g., Python).
4. A new notebook will open, and you can start adding code cells.

## 4. Use an Existing Notebook

If you already have a `.ipynb` file in your repository:

- Open the file directly from the file explorer in Code by clicking on it.
- The notebook will open in the notebook editor, and you can start working with it.

## 5. Run the Jupyter Notebook

- To run cells within the notebook, click the "Run" button next to each cell or use the `Shift + Enter` shortcut to run the current cell and move to the next one.
- First time you will need to select kernal, your codespace might not have Kernal and the shortcut was to do that is adding follwing jupyter extension.
```
Name: Jupyter
Id: ms-toolsai.jupyter
Description: Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more.
Version: 2024.7.0
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
```

## 6. Save and Commit Your Work

- Save your notebook regularly by pressing `Ctrl + S` (or `Cmd + S` on macOS).
- To commit your changes to GitHub, use the standard Git commands in the terminal or the Source Control panel in Codespace.


## Summary

- **Install Jupyter Notebook** using `pip install notebook`.
- **Create a new Jupyter notebook** using the VS Code command palette.
- **Open and edit existing notebooks** directly from the file explorer.
- **Run your cells** directly in the notebook editor in the Codespace.
- **Save and commit** your work to your GitHub repository.

This setup allows you to work seamlessly with Jupyter notebooks within your Codespace environment.



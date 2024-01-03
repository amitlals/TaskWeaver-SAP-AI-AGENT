<h1 align="center">
    <img src="./.asset/logo.color.svg" width="45" /> TaskWeaver - AI Agent with SAP HANA DB Plugin
</h1>

A **code-first** agent framework for seamlessly planning and executing data analytics tasks. 
This innovative framework interprets user requests through coded snippets and efficiently 
coordinates a variety of plugins in the form of functions to execute 
data analytics tasks. 


**Rationale and Prerequisites for TaskWeaver, SAP S/4HANA and HANA DB custom Plugin:**
- [x] Using Custom **SAP HANA Plugins**: TaskWeaver should support custom plugins for doing things like getting data from SAP S/4HANA product and sales or custom tables, using specific SAP data extraction algorithms, and making the connection plugin with the ‘hdbcli’ python package deployment.
- [x] Handling Complex Data Structures: It must handle complex data formats, like pandas DataFrame, for advanced data processing and facilitate easy data transfer between plugins.
- [x] Stateful Execution: TaskWeaver should maintain state across conversations, processing user inputs and executing tasks in an iterative manner throughout the session.
- [x] Data Schema Inspection and Action: Prior to executing tasks, TaskWeaver needs to inspect the data schema in the database and use this information for actions before analyzing the SAP product and sales data.
- [x] Natural Language Responses: The system should provide user-friendly responses in natural language, summarizing execution results, such as the amount of sales order per product details.
- [x] Dynamic Code Generation: TaskWeaver must generate code on-the-fly to meet ad-hoc user requests, including tasks not covered by existing plugins, like visualizing SAP data related to Sales and product tables.
- [x] Incorporating Domain Knowledge: The framework should integrate domain-specific knowledge to enhance LLM's planning and tool usage, ensuring accurate and reliable results in complex domains.
- [x] Persisting Results: It should offer a mechanism to save outcomes, such as DataFrames or images, to persistent storage, with options for business users to download these artifacts.

<!-- - [2023-11-30] TaskWeaver is released on GitHub🎈.  -->



## Highlights

- [x] **Rich data structure** - TaskWeaver allows you to work with rich data structures in Python, such as DataFrames, instead of dealing with strings.
- [x] **Customized algorithms** - TaskWeaver allows you to encapsulate your own algorithms into plugins and orchestrate them.
- [x] **Incorporating domain-specific knowledge** - TaskWeaver is designed to incorporat domain-specific knowledge easily to improve the reliability.
- [x] **Stateful execution** - TaskWeaver is designed to support stateful execution of the generated code to ensure consistent and smooth user experience.
- [x] **Code verification** - TaskWeaver is designed to verify the generated code before execution. It can detect potential issues in the generated code and provide suggestions to fix them.
- [x] **Easy to use** - TaskWeaver is easy to use with sample plugins, examples and tutorials to help you get started. TaskWeaver offers an open-box experience, allowing users to run it immediately after installation.
- [x] **Easy to debug** - TaskWeaver is easy to debug with detailed and transparent logs to help you understand the entire process, including LLM prompts, the code generation, and execution process.
- [x] **Security consideration** - TaskWeaver supports a basic session management to keep different users' data separate. The code execution is separated into different processes to avoid mutal interference.
- [x] **Easy extension** - TaskWeaver is easy to extend to accomplish more complex tasks with multiple agents as the plugins.

## Quick Start


### 1. Installation & Setup SAP S/4HA for TaskWeaver and Plugin Deployment
TaskWeaver requires **Python >= 3.10**. It can be installed by running the following command:
```bash
# [optional to create conda environment]
# conda create -n taskweaver python=3.10
# conda activate taskweaver

# clone the repository
git clone https://github.com/microsoft/TaskWeaver.git
cd TaskWeaver
# install the requirements
pip install -r requirements.txt
```


### 2. Configure the LLMs
Before running TaskWeaver, you need to provide your LLM configurations. Taking OpenAI as an example, you can configure `taskweaver_config.json` file as follows. 

#### OpenAI
```json
{
"llm.api_key": "the api key",
"llm.model": "the model name, e.g., gpt-4"
}
```

💡 TaskWeaver also supports other LLMs and advanced configurations, please check the [documents](https://microsoft.github.io/TaskWeaver/docs/overview) for more details. 


#### 3. To establish a connection with TaskWeaver, input your SAP HANA Database connection details into the hana-connect.ymal and validate hana-connect.py plugin details.
#configurations: # fill below details, please ensure SAP system and HANA DB are fully operational and connected. 
 ```
hana_host: "xx.xx.xx.xx"
hana_port: "30xx"
hana_user: "xxx"
hana_password: "xxx"
api_type: openai
api_base: https://api.openai.com
api_key: ""
Deployment_name: "gpt-4*"
```

![image](https://github.com/amitlals/TaskWeaver-SAP-AI-AGENT/assets/37605691/fdbf2a2b-9dba-4771-b278-6131fc048d7b)

 ```
## SAP Custom Table for Products and Sales Order View 
Select * from ZDEMO_S0I
 ```
![image](https://github.com/amitlals/TaskWeaver-SAP-AI-AGENT/assets/37605691/2c041d98-d318-47a2-b490-8eae8dd012fa)



#### 4. Install chainlit package prior to triggering TaskWeaver Web UI, please refers to [web UI docs](https://microsoft.github.io/TaskWeaver/docs/usage/webui) for more details.
Install the chainlit package by **pip install chainlit** if you don't have it in your env.

#### 5. Start the service by running the following command.
```
cd playground/UI/
chainlit run app.py
```
Open the browser with http://localhost:8000 and you can start the TaskWeaver App connected with SAP 

![image](https://github.com/amitlals/TaskWeaver-SAP-AI-AGENT/assets/37605691/b8eda88a-bf85-4011-b7b0-35213afe392d)

##

## Documentation

More documentations can be found on [TaskWeaver Website](https://microsoft.github.io/TaskWeaver).


> 💡 If you have any feedback or issues, please don't hesitate to contact Amit Lal https://www.linkedin.com/in/amitlal/ 


---

## Other Demo Examples

The demos were made based on the [web UI](https://microsoft.github.io/TaskWeaver/docs/usage/webui), which is better for displaying the generated artifacts such as images. 
The demos could also be conducted in the command line interface. 

#### Example 1: Pull data from a database and apply an anomaly detection algorithm
In this example, we will show you how to use TaskWeaver to pull data from a database and apply an anomaly detection algorithm.

[Anomaly Detection](https://github.com/microsoft/TaskWeaver/assets/7489260/248b9a0c-d504-4708-8c2e-e004689ee8c6)

If you want to follow this example, you need to configure the `sql_pull_data` plugin in the `project/plugins/sql_pull_data.yaml` file.
You need to provide the following information:
```yaml
api_type: azure or openai
api_base: ...
api_key: ...
api_version: ...
deployment_name: ...
sqlite_db_path: sqlite:///../../../sample_data/anomaly_detection.db
```
The `sql_pull_data` plugin is a plugin that pulls data from a database. It takes a natural language request as input and returns a DataFrame as output.

This plugin is implemented based on [Langchain](https://www.langchain.com/).
If you want to follow this example, you need to install the Langchain package:
```bash
pip install langchain
pip install tabulate
```



For more examples, please refer to our [paper](http://export.arxiv.org/abs/2311.17541). 

> 💡 The planning of TaskWeaver are based on the LLM model. Therefore, if you want to repeat the examples, the execution process may be different
> from what you see in the videos. For example, in the second demo, the assistant may ask the user which prediction algorithm should be used.
> Typically, more concrete prompts will help the model to generate better plans and code.


## Citation
Our paper could be found [here](http://export.arxiv.org/abs/2311.17541). 
If you use TaskWeaver in your research, please cite our paper:
```
@article{taskweaver,
  title={TaskWeaver: A Code-First Agent Framework},
  author={Bo Qiao, Liqun Li, Xu Zhang, Shilin He, Yu Kang, Chaoyun Zhang, Fangkai Yang, Hang Dong, Jue Zhang, Lu Wang, Minghua Ma, Pu Zhao, Si Qin, Xiaoting Qin, Chao Du, Yong Xu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang},
  journal={arXiv preprint arXiv:2311.17541},
  year={2023}
}
```


## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

> 💡Disclaimer: Before adopting any connection plugin for SAP HANA DB, please review your SAP HANA DB licensing details carefully. Additionally, all SAP-related keywords, logos, and trademarks are the property of SAP SE. 
Their use in this context does not imply any affiliation with or endorsement by SAP SE.

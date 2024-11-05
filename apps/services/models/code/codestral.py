import ell, openai

ollama_client = openai.OpenAI(base_url="http://10.1.1.208:11434/v1", api_key='ollama') 

class CodestralModel():
    def __init__(self) -> None:
        pass

    @staticmethod
    @ell.simple(model="codestral:latest", client=ollama_client, exempt_from_tracking=True, temperature=0.5)
    def generate_code(user_message:str) -> ell.Message:
        f"""
        You are the worlds greatest coding agent. You will be given a task. This task may be a coding task or a problem to solve. Your job is to write code in the most appropriate programming language that solves the problem or completes the task as requested by the 3rd party. If the programming language is not selected, you will use python. If you don't know how to do it, just say "I don't know". Do not explain your code. Your response MUST be enclosed in markdown format with the appropriate suffix for the programming language used.
        """.replace('\n', '', 1).replace('        ', ' ').replace('    ', ' ').replace('\t', ' ').replace('  ', ' ')
        return \
        f"""        
        REQUIREMENTS: Ensure that you read the prompt several times to gather the necessary context. Your output should match the requested response. Do not assume anything, If it's not clear in the prompt. Re-read the prompt if needed. If there is any ambiguity or uncertainty, ask for clarification. Do not make assumptions about what values to plug into functions. Ask for clarification if a required value is not specified. Do not write code that you have not tested. If you are unsure how to test your code, ask for help. Do not use placeholders in your code. Use actual values or variables. Do not include any explanations or apologies in your responses. Always output code that can be executed with the provided inputs. Do not output images or diagrams. Do not include multiple solutions in one response.
        
        {user_message}

        Follow the Requirements precisely and generate only code in markdown format. THAT IS YOUR ONLY TASK! Do not include any explanations or apologies in your responses. If you are unsure about the programming language to use, use Python. Your response should be enclosed in markdown format with the appropriate suffix for the programming language used. If the problem is not related to coding or requires a non-coding solution, respond with "I don't know".
        """
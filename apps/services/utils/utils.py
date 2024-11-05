import os, ell, openai, datetime, asyncio
from typing import List, Literal
from pydantic import BaseModel, Field

ell.init(verbose=False)

MODEL_NAME = "llama3.2:latest" # "llama3.2:latest" "nemotron:latest" "nemotron-mini"
EVALUATOR_MODEL = "nemotron-mini"

API_KEY = "ollama"
BASE_URL = "http://10.1.1.208:11434/v1"

test_client = openai.Client(base_url=BASE_URL, api_key=API_KEY)
production_client = openai.Client(base_url=BASE_URL, api_key=API_KEY)

TEST_SYSTEM_PROMPT = \
f"""
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. Your sole responsibility is to reply with a single 1-word response of 'Pong' if the user message is 'Ping'.

ENSURE THAT THE USER MESSAGE IS A CASE INSENTIVE COMPARISON TO 'PING'. IF IT IS NOT, THEN YOU MUST RESPOND WITH 'ERROR'.
"""

SHORT_STORY_PROMPT = \
f"""
Generate a unique and original authored short story based on the provided ideas. Do not include any explanations or apologies in your response. Only provide the story itself. Unless specified, do not generate a title for the short story, or explain what the response is.

ENSURE THAT YOU RE-READ ALL THE IDEAS IN THE PROVIDED STATEMENT. IF THE STATEMENT DOES NOT PROVIDE ANY IDEAS, OR THEY DON'T MAKE SENSE; THEN YOU MUST RESPOND WITH 'ERROR'. 
YOU MUST ONLY RESPOND WITH A STORY OR 'ERROR' AND NOTHING ELSE.
"""

@ell.simple(model=MODEL_NAME, exempt_from_tracking=True, client=test_client, temperature=0)
def Test(message: str) -> list[ell.Message]:    
    return [ ell.system(TEST_SYSTEM_PROMPT), ell.user(message) ]

@ell.simple(model=MODEL_NAME, exempt_from_tracking=True, client=production_client)
def Generate_ShortStory(message: str) -> list[ell.Message]:    
    return [ ell.system(SHORT_STORY_PROMPT), ell.user(message) ]



# The 'Character' model defines a character in a short story with its name, age, gender, occupation, backstory, and persona as fields. This allows for easy creation and management of characters within the story generation process. 
class Character(BaseModel):
    name:       str = Field(description=f"The story character's name")
    age:        int = Field(description="The story character's age")
    gender:     str = Field(description="The story character's gender (male, female, non-binary etc.)")
    occupation: str = Field(description="The story character's occupation or role in the story.")
    backstory:  str = Field(description="A brief summary of the story character's background and history.")
    persona:    str = Field(description="A description of the story character's personality, values, and motivations.")

# The 'ShortStory' model represents a short story with its title, author, characters, and description as fields. This allows for easy creation and management of stories within the story generation process. It also provides a structured format to store and retrieve information about each story. Additionally, it can be used to validate input data when generating or processing stories, ensuring that all required information is provided and in the correct format
class ShortStory(BaseModel):
    title:       str = Field(description="The title of the short story.", default="")
    author:      str = Field(description="The name of the author who wrote the short story.", default="")   
    description: str = Field(description="A brief summary of the main events and themes of the short story.", default="")
    content:     str = Field(description="The generated content of the short story.", default="")
    setting:     str = Field(description="The setting or location where the short story takes place.", default="")
    theme:       str = Field(description="The main theme or message that is explored in the short story.", default="")
    conflict:    str = Field(description="The primary conflict or obstacle that the characters face in the short story.", default="")
    resolution:  str = Field(description="How the conflict is resolved or concluded at the end of the short story.", default="")

    characters:  list[Character] = Field(description=f"A list of characters that appear in the short story. using the following json schema for each character: {Character.model_json_schema()}", default=[])

# evaluate the user's ideas and extract relevant information to define the story
class EvaluationRating(BaseModel):
    rating: int = Field(description="A score from 1-5 indicating how well the idea meets the criteria for a short story. A higher score indicates a more novel and original idea.", default=1)
    reasoning: str = Field(description="An explanation of why the idea was given its score, including any specific strengths or weaknesses that were considered.", default="")

@ell.simple(model=MODEL_NAME, client=production_client, exempt_from_tracking=True)
def GenerateImprovedPrompt(prompt: str, evaluation: EvaluationRating) -> ell.Message:
    f"""You are the worlds greatest AI Prompt Generation Assistant. Generate a System Prompt that will improve the user's idea for a short story based on the provided prompt and evaluation report. The system prompt should be designed to help the user create a more engaging, original, and well-developed short story by addressing any weaknesses in their initial idea and building upon its strengths.

    ENSURE THAT YOU RE-READ THE EVALUATION REPORT SEVERAL TIMES IN CONJUNCTION WITH THE PROMPT TO ESTABLISH THE CONTEXT OF YOUR TASK.
    DO NOT INCLUDE YOUR REASONING, OR WHY YOU ARE GENERATING THE IMPROVED PROMPT. THE SYSTEM PROMPT WILL BE VALIDATED BY ANOTHER AI MODEL AND SHOULD BE YOUR BEST WORK.
    """.replace('        ', ' ').replace('    ', ' ').replace('\n', '', 1).replace('  ', '', 1)

    return f"""Here is the original Prompt: '{prompt}'\nHere is the AI Evaluators Report:\n```json {evaluation.model_dump_json()}```
    REMINDER, YOU ARE NOT GENERATING A SHORT STORY, ONLY A PROMPT TO BE USED FOR ANOTHER LARGE LANGUAGE MODEL TO USE. ENSURE THAT YOU GENERATE A COMPREHENSIVE AND ENCOMPASSING SYSTEM PROMPT BASED ON THE INFORMATION ABOVE, USE 10-15 SENTENCES TO IMPROVE THE ORIGINAL PROMPT. DO NOT PROVIDE NAMES FOR CHARACTERS, PLACES, OR ITEMS. DO NOT INCLUDE ANY EXPLANATIONS OR JUSTIFICATION FOR YOUR SYSTEM PROMPT, DO NOT REPEAT ANY OF THE INFORMATION FROM THE EVALUATION REPORT, ONLY IMPROVE THE ORIGINAL PROMPT BASED ON THE EVALUATION REPORT AND YOUR UNDERSTANDING OF HOW TO GENERATE A BETTER SHORT STORY. RE-READ THE ORIGINAL PROMPT AND EVALUATION REPORT TO FULLY COMPREHEND THE CONTEXT. DO NOT PROVIDE CONTEXT FOR WHAT OR WHY YOU ARE GENERATING THE PROMPT"""

@ell.simple(model=MODEL_NAME, client=production_client, exempt_from_tracking=True)
def GenerateStoryElements(prompt: str) -> ShortStory:
    f"""
    You are a highly skilled and creative AI Assistant that specializes in generating engaging and original short stories based on provided prompts. Your goal is to create a unique and captivating narrative by focusing on character development, plot twists, and emotional depth.
    
    TASKS:
    1. YOUR STORY SHOULD BE APPROXIMATELY 10-20 SENTENCES LONG AN BE BASED ON THE PROVIDED USER PROMPT.
    2. YOU ARE REQUIRED TO RETURN A JSON OBJECT STRUCTURED USING THE FOLLOWING JSON SCHEMA: { ShortStory.model_json_schema() }
    3. RE-READ THE PROMPT SEVERAL TIMES TO GATHER ALL THE CONTEXT REQUIRED FOR GENERATING A COMPELLING AND ENGAGING SHORT STORY. DO NOT INCLUDE ANY EXPLANATIONS OR JUSTIFICATION FOR YOUR STORY, ONLY RETURN THE JSON OBJECT WITH THE FIELDS FILLED OUT BASED ON THE PROMPT AND YOUR CREATIVITY.
    """
    return prompt

# The 'ShortStoryGenerator' class provides a framework for generating short stories based on provided ideas. It includes methods to define the story, generate the story content, evaluate, refine and critique the generated story output, and finally express the story in a presentable format. This allows for customization of each step of the story generation process, and ensures that the final product meets quality standards. Additionally, it can be used as a base class to create more specialized story generators with additional features or functionality.
class ShortStoryGenerator():    
    def __init__(self):
        self.story: ShortStory = ShortStory()
        self.user_ideas = ""
        self.complexity = 4
    
    async def Generate(self, ideas: str, title: str = "", author: str = "", complexity: int = 4) -> ShortStory:
        self.story = ShortStory(title=title, author=author)
        self.user_ideas = ideas
        self.complexity = max(1, complexity)        
        evaluation: EvaluationRating = EvaluationRating()        
        
        while True:
            try:
                result : ell.Message = self._EvaulateIdea(content=ideas)[0]
                evaluation = result.parsed
                print (f"Idea Evaluation: {evaluation.rating}\nReasoning: {evaluation.reasoning}")   
                break                
            except Exception as e: continue
        
        for _ in range(self.complexity):
            self.user_ideas = GenerateImprovedPrompt(
                prompt=self.user_ideas, 
                evaluation=evaluation, 
                api_params={
                    "model" : "llama3.2:latest",
                    "temperature": 0.9,
                    "max_tokens": 100_000,
                    "seed": datetime.datetime.utcnow().microsecond,                
                    "top_p": 0.9185, 
                    "presence_penalty": 0.6, 
                    "frequency_penalty": 1.2
                }
            )[0]

            for _ in range(3):
                try:
                    result = self._EvaulateIdea(content=self.user_ideas)[0]
                    evaluation = result.parsed
                    break
                except Exception as e: continue

            if evaluation.rating == 5: 
                print (f"Idea Evaluation: {evaluation.rating}\nReasoning: {evaluation.reasoning}")        
                break

        print(self.user_ideas)        

        return None

    @ell.complex(model=EVALUATOR_MODEL, client=production_client, exempt_from_tracking=True, response_format=EvaluationRating, temperature=0.5, max_tokens=4_096)
    def _EvaulateIdea(self, content: str) -> ell.Message:
        system_prompt = f"""
        You are a creative assistant at a fortune 500 company. Your boss have given you a task to do evaluations of ideas that have come through the office. You will be given a short statment containing an idea for a short story. Your task is to evaluate the idea and rate it on a scale of 1-5 based on its originality, novelty, and potential for creating a compelling narrative. A higher score indicates a more unique and promising idea.

        TASKS:
        1. YOU ARE REQUIRED TO RETURN A JSON OBJECT STRUCTURED USING THE FOLLOWING JSON SCHEMA: { EvaluationRating.model_json_schema() }
            WHERE 'rating' IS AN INTEGER BETWEEN 1 AND 5, WITH 1 BEING THE LOWEST RATING AND 5 BEING THE HIGHEST.
            WHERE 'reasoning' IS THE REASONING YOU USED FOR PROVIDING THE RATING. YOUR REASONING MUST PROVIDE CONTEXT AND UNDERSTANDING FOR A PERSON WHO KNOWS NOTHING ABOUT CREATIVE STORY-TELLING.        
        2. DO NOT INFER OR MAKEUP IDEAS NOT INCLUDED IN THE PROVIDED CONTEXT. 
        3. ONLY USE THE INFORMATION PRESENTED TO DRAW YOUR CONCLUSION FOR EVALUATION.
        4. IF YOU HAVE IDENTIFIED WEEKNESSES, PROVIDE EPOSITION AND DETAILED EXPLAINATION FOR IMPROVEMENTS.
        5. RE-READ THE STATEMENT MULTIPLE TIMES BEFORE EVALUATING IT.
        
        PROVIDE DETAILED EXPLAINATIONS DESCRIBING THE IDENTIFIED WEEKNESSES AND HOW TO IMPROVE THEM IN YOUR REASONING.
        """.replace('        ', ' ').replace('    ', ' ').replace('\n', '', 1).replace(' ', '', 1)
        return [ ell.system(content=f"{system_prompt}"), ell.user(content=content) ]

    async def _Refine(self) -> list[ell.Message]:
        pass

    async def _Criticize(self) -> list[ell.Message]:
        pass

    async def _RequestContent(self, type: Literal['character', 'setting', 'theme', 'conflict', 'resolution'] = 'character', complexity: int = 4) -> ell.Message:
        current_theme       = self.story.theme
        current_setting     = self.story.setting
        current_conflict    = self.story.conflict
        current_resolution  = self.story.resolution
        current_characters  = self.story.characters

        match type:
            case 'character':
                # Add your logic for generating character details here
                pass

            case 'setting':
                # Add your logic for generating setting details here
                pass

            case 'theme':
                # Add your logic for generating theme details here
                pass

            case 'conflict':
                # Add your logic for generating conflict details here
                pass

            case 'resolution':
                # Add your logic for generating resolution details here
                pass

async def main():
    story_generator = ShortStoryGenerator()
    story = await story_generator.Generate(ideas="A detective, a cat, a mysterious painting, and an old mansion on a hilltop.")

if __name__ == "__main__": asyncio.run(main())
import commands
import importlib.util
import os
import re

def load_script(scriptname):
    module_path = os.path.join(os.path.dirname(__file__), "commands_callable", f"{scriptname}.py")
    spec = importlib.util.spec_from_file_location(scriptname, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main(LLM_Output, scriptname):
    try:
        script_module = load_script(scriptname)
        commands = extract_commands(LLM_Output)
        results = execute_commands(commands, script_module)
        return results
    except Exception as e:
        return f"Error: {e}"

def extract_commands(text):
    return re.findall(r'\{([^}]*)\}', text)

def execute_commands(commands, script_module):
    results = []
    for command_string in commands:
        # Split command_string into command name and parameters
        parts = command_string.split(maxsplit=1)
        if len(parts) > 0:
            command_name = parts[0]
            parameters = parts[1] if len(parts) > 1 else ""

            try:
                func = getattr(script_module, command_name)
                if parameters:
                    # Evaluate parameters to handle numbers and other literals
                    parameters = eval(parameters)
                    result = func(parameters)  # Execute the function with parameters
                else:
                    result = func()  # Execute the function without parameters
                results.append((command_string, result))
            except AttributeError:
                results.append((command_string, "Command not recognized"))
            except Exception as e:
                results.append((command_string, f"Error: {e}"))
        else:
            results.append((command_string, "Invalid command format"))

    return results
    

if __name__ == "__main__":
    
    output = "Test - {Roll_Dice 15} and {Roll_Dice 10}. {Next}"
    results = main(output,"Conversation_Commands")
    print(results)

    
import json
import os
import sys

# Define the mandatory schema for a production-grade prompt
REQUIRED_KEYS = ["prompt_metadata", "system_instructions", "few_shot_examples"]
METADATA_KEYS = ["name", "version", "target_models"]

def validate_prompt_file(filepath):
    """
    Validates a single prompt JSON file against production standards.
    """
    print(f"Checking: {filepath}")
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            
        # 1. Check for core top-level keys
        for key in REQUIRED_KEYS:
            if key not in data:
                print(f"FAILURE: Missing required key '{key}' in {filepath}")
                return False
                
        # 2. Validate metadata depth
        for key in METADATA_KEYS:
            if key not in data["prompt_metadata"]:
                print(f"FAILURE: Missing metadata field '{key}'")
                return False
        
        # 3. Ensure Few-Shot examples exist (Mandatory for quality)
        if not isinstance(data["few_shot_examples"], list) or len(data["few_shot_examples"]) == 0:
            print(f"FAILURE: No Few-Shot examples provided in {filepath}")
            return False

        print(f"SUCCESS: {filepath} passed validation.")
        return True

    except json.JSONDecodeError:
        print(f"FAILURE: {filepath} is not a valid JSON file.")
        return False
    except Exception as e:
        print(f"FAILURE: An unexpected error occurred: {e}")
        return False

def main():
    prompt_dir = "prompts"
    all_passed = True
    
    if not os.path.exists(prompt_dir):
        print(f"Error: Directory '{prompt_dir}' not found.")
        sys.exit(1)

    for filename in os.listdir(prompt_dir):
        if filename.endswith(".json"):
            if not validate_prompt_file(os.path.join(prompt_dir, filename)):
                all_passed = False

    if not all_passed:
        print("\nValidation Failed. Please correct the errors above before merging.")
        sys.exit(1)
    
    print("\nAll prompts are production-ready.")
    sys.exit(0)

if __name__ == "__main__":
    main()
  

apply-build-your-first-safety-test-suite

Lab

Apply: Build Your First Safety Test Suite
Instructions
Build Your First Safety Test Suite
Overview
In this hands-on "Apply" lab, you will work within a Coursera Lab (VSCode) environment featuring a basic LLM service. Your primary task is to write a pytest suite that enforces a specified safety policy. This lab will provide you with the opportunity to practice the skills demonstrated in the accompanying video while ensuring that the LLM service adheres to safety standards.

Dataset Information
This lab does not require a specific dataset, as the focus is on writing and implementing test cases for an LLM service. The tests will evaluate the service's compliance with predefined safety policies based on the code you write.

Learning Outcomes
By the end of this lab, you will be able to:

Write a pytest suite to enforce a safety policy for an LLM service.

Understand how to integrate testing frameworks into your projects.

Evaluate the effectiveness of your safety tests.

---Step 1
Lab instructions
0 of 5 completed


inLabInstructionsPart~B1E9K9LqEfCpaxIiEu81Hw
​
Overview
In this hands-on "Apply" lab, you will work within a Coursera Lab (VSCode) environment featuring a basic LLM service. Your primary task is to write a pytest suite that enforces a specified safety policy. This lab will provide you with the opportunity to practice the skills demonstrated in the accompanying video while ensuring that the LLM service adheres to safety standards.

Dataset Information
This lab does not require a specific dataset, as the focus is on writing and implementing test cases for an LLM service. The tests will evaluate the service's compliance with predefined safety policies based on the code you write.

Learning Outcomes
By the end of this lab, you will be able to:

Write a pytest suite to enforce a safety policy for an LLM service.

Understand how to integrate testing frameworks into your projects.

Evaluate the effectiveness of your safety tests.

Prerequisites
Access to the Coursera Lab environment with VSCode.

Basic understanding of Python programming and pytest framework.

Familiarity with safety policies relevant to LLM services.

Starting Point
Access the starter files: You can find the starter code (llm_service.py) file in the Coursera Lab environment under the Project folder section. This file contains the LLM service code and should not be modified for this lab.

Create a new test file: To complete this lab, you are expected to create a new Python file for your pytest tests (for example, test_llm_service.py). All test cases for enforcing the safety policy should be written in this new test file.

Required tools/setup: Ensure that you have pytest installed in your VS Code environment. If not, you can install it using the command:

1 pip install pytest

---Step 2
Activity 1: Writing Your First Test (10 minutes)

Context: You will begin by writing a simple test case to check a safety policy.

Steps:

Open the starter file llm_service.py and review how it behaves:

 Unsafe prompts contain keywords like "dangerous code", "harmful instruction", etc. 

 Safe prompts include greetings like "hello" or "greet". 

 Neutral prompts are anything that does not trigger safety or greetings.

Create a new test file (for example, test_llm_service.py) in the same workspace.

In your new file test_llm_service.py, import the function and constants:

1
from llm_service import generate_response, POLICY_REFUSAL_MESSAGE
In your new test file, write a pytest test function that validates the safety policy:  

12
def test_safety_policy():
    # Your test code here
Note: The code snippet above is provided as a reference example, not as starter code.

Try It Yourself: Consider different scenarios that might violate the safety policy and how you can test for them.

Expected behavior: You should have a functional test that checks whether the safety policy is enforced correctly.

Tip: Ensure that your test checks for both compliance and non-compliance scenarios.

---Step 3
Activity 2: Expanding Your Test Suite (10 minutes)

Context: Now that you have a basic test in place, you will expand your test suite to cover additional scenarios.

Steps: 

Continue working in your test file (e.g., test_llm_service.py).

Add additional test functions to cover different scenarios and edge cases:

1234
def test_additional_safety_policy():

# Additional safety checks
assert # Replace with your safety check
Try It Yourself: Think about edge cases, such as unexpected inputs or boundary conditions, and how they might affect your tests.

Expected behavior: Your test file should now contain multiple pytest test functions validating different aspects of the safety policy.

Tip: Use assertions to validate expected outcomes and ensure comprehensive coverage of the safety policy; you may add more tests for other scenarios (like neutral or empty prompts), but only one safe prompt test is required to complete Activity 2.

---Step 4
Test Your Work
Run your pytest suite using the command:

1
python3 -m pytest test_llm_service.py
Expected Output: All tests should pass without errors.

Success Checklist
You have written at least two test functions.

Your tests cover different scenarios of the safety policy.

The pytest suite runs without errors.

Common Issues & Solutions
Problem: Tests fail due to incorrect assertions.

Solution: Double-check your conditions and ensure they align with the safety policy.

Problem: Pytest is not recognized.

Solution: Ensure pytest is installed and properly configured in your environment.

Summary
In this lab, you learned how to write and expand a pytest suite to enforce a safety policy for an LLM service. You practiced integrating testing frameworks and evaluated the effectiveness of your safety tests. This experience will enhance your ability to ensure that LLM services operate within established safety parameters.

By completing this lab, you have taken a significant step toward understanding how to implement and test safety measures in AI systems.

---Step 5
Reference against test_llm_service_reference.py. Get good stuff from it and add to test_llm_service.py
